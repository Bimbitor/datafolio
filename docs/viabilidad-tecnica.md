# Viabilidad técnica del stack

> Revisión hecha el 2026-11-05 contra documentación de Vercel y Supabase, antes de escribir la primera spec.
> Criterio: buscar lo que sea **más barato cambiar ahora que después**. No es una lista de todo lo que puede fallar, sino de lo que obligaría a rehacer trabajo si se descubre tarde.
> Cada hallazgo indica su nivel de confianza: documentación oficial, o fuente secundaria por verificar.

---

## 1. CRÍTICO — Un proyecto de Vercel o dos decide si el login funciona

**El problema.** La sesión del administrador es una cookie `HttpOnly`, `Secure`, `SameSite=Strict` (RS-05). Esa cookie **solo viaja si el frontend y la API están en el mismo origen**. Si el sitio queda en `datafolio.vercel.app` y la API en `datafolio-api.vercel.app`, la cookie pasa a ser de terceros: los navegadores la bloquean y el panel no puede autenticarse. Las salidas serían degradar a `SameSite=None` y depender de cookies de terceros, que Chrome restringe, o cambiar a un token en memoria, que obliga a volver a entrar en cada recarga. Las dos son peores y las dos implican reescribir la autenticación.

**Lo que hay que conseguir.** Un solo proyecto de Vercel: Astro desplegado con su adaptador y las funciones Python en una carpeta `api/` en la raíz. Mismo origen, cookie de primera parte, nada que degradar.

**El riesgo real.** Vercel documenta por separado que soporta funciones Python en `/api` de proyectos existentes, y que soporta Astro. **No encontré un ejemplo confirmado de las dos cosas en el mismo proyecto**, y sí hay un reporte antiguo de Astro donde una carpeta `/api` en la raíz devolvía 404 en vez de desplegarse como funciones. Puede estar resuelto; no lo doy por hecho.

**Acción, al inicio de la feature 01 y antes de escribir nada de autenticación:** desplegar una prueba mínima — un Astro vacío más un `api/index.py` que responda "ok" — y comprobar que las dos rutas contestan en el mismo dominio. Media hora de trabajo.

**Plan B si falla:** dos proyectos de Vercel desde el mismo monorepo, y en el frontend una reescritura que haga de proxy de `/api/*` hacia el backend. El navegador sigue viendo un solo origen y la cookie sigue siendo de primera parte. Cuesta un salto de red extra por petición, nada más.

Lo caro no es elegir mal: es descubrirlo cuando el login ya esté escrito.

> Confianza: alta en el comportamiento de las cookies, media en el estado actual de Astro + Python en un proyecto. Por eso la prueba.

## 2. ALTO — Supabase se pausa sola a los 7 días sin actividad

**El problema.** La página de precios de Supabase lo dice sin rodeos: los proyectos del plan gratuito se pausan tras **una semana de inactividad**. Un portafolio recién publicado pasa semanas enteras sin una sola visita. Pausado significa que proyectos, blog y comentarios dejan de responder.

Y el momento en que se nota es el peor posible: la primera visita después de una semana tranquila, que es justo la del reclutador que abrió tu CV.

**Mitigación.** Una tarea programada de Vercel que una vez al día llame a un endpoint que haga una consulta trivial. El plan gratuito de Vercel permite tareas programadas **una vez al día**, y el umbral de Supabase es de siete, así que sobra con mucho margen.

**Cuándo.** En la feature 01 o, a más tardar, en la 03 cuando exista la base de datos. No es algo que se añada "después": si se olvida, el fallo aparece solo cuando ya hay alguien mirando.

> Confianza: alta. Página de precios oficial de Supabase. Un análisis de terceros advierte que el umbral ha cambiado antes, así que conviene no apurarlo: una vez al día está bien.

## 3. MEDIO — El SMTP sí funciona, con dos condiciones

Esta era la duda que originó la revisión, y la respuesta es buena.

**Vercel bloquea solo el puerto 25.** El 587, que es el que usa Gmail con STARTTLS, está abierto. Lo dice la propia base de conocimiento de Vercel. Hay fuentes de terceros que afirman lo contrario, pero son de 2020 o reflejan políticas viejas.

**Dos condiciones que hay que respetar al escribir el código:**

1. **Hay que esperar al envío antes de devolver la respuesta.** Cuando una función serverless devuelve su respuesta HTTP, el trabajo que siga en curso se pausa y puede no reanudarse nunca. Un envío lanzado sin esperar se pierde en silencio: el usuario ve "mensaje enviado" y el correo no llega jamás. Es el fallo típico y es invisible en desarrollo.
2. **No puede correr en el runtime Edge**, que no tiene sockets TCP. Nuestra función Python no lo usa, así que no aplica, pero queda escrito para que nadie la mueva allí por rendimiento.

El límite de duración del plan gratuito es de 300 segundos, de sobra para un intercambio SMTP incluso con arranque en frío.

**Riesgo residual:** Google puede limitar o marcar autenticaciones SMTP desde direcciones de centro de datos. Si diera problemas, la salida es un servicio de correo por HTTP, que es además lo que Vercel recomienda. Eso sería cambiar la implementación de una función, no la arquitectura, así que **es barato cambiarlo después** y no hay que decidirlo ahora.

> Confianza: alta. Base de conocimiento oficial de Vercel, actualizada hace poco.

## 4. RESUELTO — Qué páginas son estáticas y cuáles se renderizan en servidor

La tabla de rutas quedó decidida y vive en `historico/project-brief.md`, §7: estáticas el home, la experiencia, el contacto, la política, el 404 y los archivos de SEO; renderizadas en servidor con caché de CDN de 60 segundos el catálogo de proyectos, las fichas, el índice del blog y los artículos; sin caché el panel y la API.

## 5. RESUELTO — La versión de Node

`package.json` fija ahora `"node": "26.x"`. Node 26 es la LTS activa desde el 28 de octubre de 2026 y es la versión por defecto de Vercel; Node 24 pasó a mantenimiento el 20 de ese mes, con fin de vida en abril de 2028, frente a abril de 2029 de la 26.

## 6. BAJO — La analítica obliga a un poco de JavaScript en páginas públicas

Una página estática no puede registrar nada por sí sola: hace falta una llamada desde el navegador a un endpoint. Consecuencias:

- El ideal de "cero JavaScript en páginas públicas" se rompe un poco. Hay que mantener ese script por debajo de 1 KB y que no bloquee nada.
- Cada visita consume una invocación. El plan gratuito da del orden de un millón al mes y 4 horas de CPU activa: para un portafolio es irrelevante.
- Efecto secundario útil: esas llamadas escriben en la base de datos, así que ayudan a mantener despierta a Supabase. No sustituyen a la tarea programada del punto 2, porque el problema aparece precisamente cuando no hay visitas.

## 7. Notas menores

- **Inter Display no está en Google Fonts.** Ya anotado en `design-tokens.md`: se autoaloja desde la distribución oficial de Inter, o se sustituye.
- **Astro i18n con slugs traducidos** funciona, pero la correspondencia entre `/es/experiencia` y `/en/experience` se define a mano. Es trabajo previsto, no una sorpresa.
- **El plan gratuito de Vercel es para uso no comercial.** Un portafolio personal lo es. Si algún día aparece una página ofreciendo servicios con tarifas, deja de serlo.
- **Vercel no soporta WebSockets** según una fuente de terceros que no pude confirmar en la documentación oficial. No los necesitamos.

## Resumen

| #   | Hallazgo                                                 | Gravedad | ¿Caro de arreglar después?                                       |
| --- | -------------------------------------------------------- | -------- | ---------------------------------------------------------------- |
| 1   | Un proyecto o dos decide si la cookie de sesión funciona | Crítico  | **Sí.** Obligaría a reescribir la autenticación                  |
| 2   | Supabase se pausa a los 7 días sin actividad             | Alto     | **Sí.** El fallo aparece ante el primer visitante tras una pausa |
| 3   | SMTP funciona si se espera el envío y no se usa Edge     | Medio    | No. Cambiar a correo por HTTP es local a una función             |
| 4   | Tabla de rutas estáticas contra renderizadas             | Medio    | **Resuelta.** La tabla está en el brief, §7                      |
| 5   | Versión de Node sin fijar                                | Bajo     | **Resuelta.** Fijada en `26.x`                                   |
| 6   | La analítica mete algo de JavaScript en páginas públicas | Bajo     | No                                                               |

**Veredicto: el stack es viable tal como está definido.** Nada obliga a cambiar de tecnología. Lo único que cambia es el orden del trabajo: la prueba de despliegue del punto 1 pasa a ser lo primero de la feature 01, antes que cualquier otra cosa.

## Fuentes

- [Can I use SMTP with Vercel?](https://vercel.com/kb/guide/serverless-functions-and-smtp) · [Sending emails from an application on Vercel](https://vercel.com/kb/guide/sending-emails-from-an-application-on-vercel)
- [Vercel Limits](https://vercel.com/docs/limits) · [Supported Node.js versions](https://vercel.com/docs/functions/runtimes/node-js/node-js-versions) · [Python runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) · [Deploy a FastAPI app on Vercel](https://vercel.com/docs/frameworks/backend/fastapi)
- [Supabase Pricing](https://supabase.com/pricing)
- [@astrojs/vercel API routes support (issue antiguo)](https://github.com/withastro/astro/issues/5451)

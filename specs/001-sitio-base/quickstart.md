# Fase 1 — Guía de verificación: Sitio base

**Feature**: `001-sitio-base` | **Fecha**: 2026-11-05

Cómo comprobar que esta feature está hecha. Las seis historias se verifican por separado y en orden de
prioridad: la P1 primero, porque si falla, lo demás se construye sobre arena.

No hay pila local ni base de pruebas: la verificación se hace **sobre el sitio desplegado**, como fija
la constitución.

---

## Antes de empezar

Lo que tiene que estar hecho por el titular, y que ningún comando puede hacer por él:

- [ ] Cuenta de Vercel, plan gratuito, con el repositorio conectado.
- [ ] Cuenta de Supabase, plan gratuito, con el proyecto creado.
- [ ] Segunda cuenta de Gmail, **nunca publicada**, que recibirá los avisos de fallo.
- [ ] Contraseña de aplicación **nueva** de la cuenta que envía el correo. La contraseña que se pegó en
      una conversación está quemada y hay que revocarla.
- [ ] Las seis variables de entorno del contrato HTTP, §6, configuradas en Vercel. Ninguna en un
      archivo del repositorio.

---

## Historia P1 — El sitio y su API conviven bajo un mismo dominio

**Esto se verifica primero y solo.** Un despliegue con una página y un endpoint, nada más.

```bash
git push origin 001-sitio-base
```

Vercel genera un despliegue de vista previa para la rama. Sobre su dirección:

| Paso | Qué se comprueba                                                  | Resultado esperado                                                                        |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1    | Abrir `/` en el navegador                                         | Responde la página del sitio                                                              |
| 2    | Abrir `/api/estado`                                               | Responde `200` con el JSON del contrato, **bajo el mismo dominio**, sin salto a otro host |
| 3    | Abrir `/api/cookie-prueba` y mirar las herramientas de desarrollo | Llega una cookie `datafolio_prueba` con `SameSite=Strict`                                 |
| 4    | Recargar `/api/estado` y mirar la petición                        | El navegador **envía de vuelta** la cookie                                                |

El paso 4 es el que importa. Si la cookie no vuelve, el origen no es común y hay que bajar al plan B
de la investigación —funciones en una carpeta `/api`— y repetir los cuatro pasos antes de seguir.

```bash
# Comprobación equivalente desde la terminal, sin navegador
curl -i https://<dominio-de-vista-previa>/api/estado
curl -i -c cookies.txt https://<dominio-de-vista-previa>/api/cookie-prueba
curl -i -b cookies.txt https://<dominio-de-vista-previa>/api/estado
```

**No se avanza a ninguna otra historia hasta que estos cuatro pasos pasen.**

---

## Historia P2 — Un visitante recorre el sitio publicado

```bash
npm run test --workspace web   # mapa de rutas: slugs completos, sin duplicados
```

Sobre el sitio desplegado:

- [ ] Las dieciocho direcciones del contrato HTTP, §1, responden al abrirlas directamente.
- [ ] Desde cualquier página, el menú lleva a todas las secciones.
- [ ] Desde cualquier página se alcanza un canal de contacto en un clic.
- [ ] Una dirección inventada devuelve la página de error con estado **404** y salida al inicio.
- [ ] En móvil, tableta y escritorio no hay desbordes horizontales. Se comprueba también con el texto
      ampliado al 200 %.
- [ ] Las secciones sin contenido muestran su armazón y la indicación de contenido pendiente. **No**
      hay texto de relleno que parezca real.

---

## Historia P3 — El visitante lee el sitio en su idioma

```bash
npm run test --workspace web   # negociación: español, inglés, idioma desconocido, cabecera ausente
```

Sobre el sitio desplegado:

- [ ] Con el navegador en español, `/` acaba en `/es/`.
- [ ] Con el navegador en cualquier otro idioma, `/` acaba en `/en/`.
- [ ] El selector de idioma desde `/es/experiencia/` lleva a `/en/experience/`, **no** al inicio.
- [ ] Tras elegir idioma a mano, navegar a otra sección y recargar mantiene esa elección.
- [ ] El código fuente de cualquier página trae `canonical`, los dos `alternate` y `x-default`.
- [ ] `/sitemap.xml` lista las dieciséis direcciones indexables de los dos idiomas.
- [ ] La respuesta de cualquier página trae la cabecera `X-Robots-Tag: noindex`.

```bash
curl -s -H 'Accept-Language: es-CO,es;q=0.9' -o /dev/null -w '%{redirect_url}\n' https://<dominio>/
curl -s -H 'Accept-Language: de-DE' -o /dev/null -w '%{redirect_url}\n' https://<dominio>/
curl -sI https://<dominio>/en/ | grep -i x-robots-tag
```

---

## Historia P4 — El visitante elige cómo se ve el sitio

- [ ] Con el sistema en oscuro, la primera visita se ve en oscuro.
- [ ] El botón flotante de abajo a la derecha cambia el tema al instante, en todas las secciones.
- [ ] Tras cambiarlo, recargar respeta la elección por encima de la del sistema.
- [ ] **Sin destello**: con el tema oscuro guardado, recargar con la caché vacía no muestra ningún
      fogonazo claro. Se comprueba con red lenta simulada, que es donde el destello se ve.
- [ ] El contraste de texto y de bordes cumple las reglas de `docs/design-tokens.md` en los dos temas.
      Las tres reglas no negociables de ese documento se revisan una por una.
- [ ] **Prueba del archivo único**: cambiar un color en `web/src/styles/tokens.css`, desplegar, y
      comprobar que el cambio se ve en todas las secciones **sin haber tocado ningún componente**. Es
      el criterio de aceptación del principio "un valor, un solo lugar". Se revierte después.

---

## Historia P5 — El sitio se puede usar solo con el teclado

Con el ratón apartado, literalmente:

- [ ] Se recorre el sitio entero con tabulador y entrada, y se alcanza todo elemento interactivo.
- [ ] El orden de tabulación sigue el orden visual.
- [ ] El foco se ve siempre, en los dos temas.
- [ ] El menú móvil se abre, se recorre y se cierra sin ratón, y el foco no queda atrapado dentro.
- [ ] Toda imagen con contenido tiene texto alternativo en el idioma de la página; las decorativas
      están marcadas para que un lector de pantalla las omita.
- [ ] Con la preferencia de movimiento reducido activada no hay ninguna diferencia perceptible, porque
      no hay animaciones.

---

## Historia P6 — El sitio se mantiene en pie sin vigilancia

```bash
pytest api/tests/test_salud.py
```

Sobre el proyecto desplegado:

- [ ] La tarea programada aparece registrada con el intervalo de seis horas.
- [ ] Su historial muestra al menos una ejecución correcta.
- [ ] La fila de `salud` en la base de datos tiene la fecha de esa ejecución y `resultado` en
      `correcto`.
- [ ] **Fallo provocado**: se invalida temporalmente la clave de la base en las variables de entorno,
      se dispara la tarea a mano desde el panel, y llega el correo de aviso al titular con la causa.
      Se restaura la clave después.
- [ ] Si el envío del correo también falla, el fallo original queda en el registro de la plataforma.

---

## Puerta de rendimiento, antes de integrar código a `main`

PageSpeed Insights sobre la dirección pública, perfil de móvil, **tres ejecuciones**, se toma la
mediana:

- [ ] Contenido principal del inicio por debajo de **2,5 s**.
- [ ] Desplazamiento involuntario por debajo de **0,1**.
- [ ] Menos de **100 KB** de JavaScript por página pública.

Un resultado fuera de presupuesto se revisa antes de seguir, no se promedia a la baja hasta que pase.

---

## Definición de hecho de esta feature

- [ ] Las seis historias verificadas, en orden.
- [ ] Vitest y pytest en verde.
- [ ] La puerta de rendimiento superada.
- [ ] El endpoint temporal `/api/cookie-prueba` **eliminado**.
- [ ] Ningún secreto en el repositorio. El gancho de pre-commit lo comprueba en cada commit.
- [ ] El sitio publicado, con la cabecera `noindex` puesta, y el coste mensual en cero.

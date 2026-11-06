# Fase 0 — Investigación: Sitio base

**Feature**: `001-sitio-base` | **Fecha**: 2026-11-05

Todas las incógnitas técnicas de la spec quedan resueltas aquí, con la fuente oficial consultada.
Lo que no se pudo confirmar en documentación se marca como **riesgo** y se resuelve en el despliegue
de prueba de la historia P1, no suponiendo.

---

## D-01. El sitio y la API conviven bajo un mismo dominio

**Decisión**: se usan **Vercel Services**. Un solo proyecto declara dos servicios en `vercel.json`
—el sitio Astro y la API de Python— cada uno con su raíz y su propio build, y dos reglas de reescritura
de nivel superior reparten el tráfico: `/api/*` a la API, el resto al sitio.

```json
{
  "services": {
    "web": { "root": "web/" },
    "api": { "root": "api/", "entrypoint": "main:app" }
  },
  "rewrites": [
    { "source": "/api/(.*)", "destination": { "service": "api" } },
    { "source": "/(.*)", "destination": { "service": "web" } }
  ]
}
```

**Razón**: es el mecanismo que Vercel documenta para exactamente este caso —"deploy multiple backends
and frontends within a single Vercel project (...) with shared routing, environment variables, and a
unique domain, replacing the need to split monorepos into separate Vercel projects"— y está disponible
**en todos los planes**, incluido el gratuito. Un solo dominio significa un solo origen, que es lo que
la cookie de sesión del administrador necesita para viajar. Cada servicio declara su propio framework
y sus propias dependencias, así que no hay ambigüedad entre el build de Astro y el de Python.

**Alternativas consideradas**:

| Alternativa                                              | Por qué no es la primera opción                                                                                                                                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Funciones Python en una carpeta `/api` en la raíz        | Sigue soportado, pero la documentación lo encuadra como soporte a proyectos existentes, y deja a Astro y a Python compartiendo raíz, donde la detección de framework es ambigua. Queda como **plan B**. |
| Dos proyectos de Vercel y una reescritura de uno al otro | Dos despliegues, dos configuraciones de variables, y la reescritura como único punto de fallo. Es lo que el estudio de viabilidad previó, y queda como **plan C**.                                      |

---

### Resultado, 2026-11-06: **el plan A funciona**

Comprobado sobre el despliegue de vista previa de la rama, no deducido:

| Comprobación         | Resultado                                                                 |
| -------------------- | ------------------------------------------------------------------------- |
| `/`                  | `200`, página del sitio                                                   |
| `/api/estado`        | `200`, **cero redirecciones**, mismo dominio, cuerpo según contrato       |
| `/api/cookie-prueba` | `204` con `datafolio_prueba=1; HttpOnly; Path=/; SameSite=strict; Secure` |
| Petición siguiente   | el cliente envía `Cookie: datafolio_prueba=1`                             |
| `X-Robots-Tag`       | `noindex`, presente en las respuestas del sitio                           |

El cuarto es el que importá. Una cookie `SameSite=Strict` puesta por la API vuelve en la
petición siguiente al sitio, así que **el navegador ve un solo origen** y la sesión del
administrador de la feature 03 es posible tal como está especificada. Ni el plan B ni el C
hacen falta.

**Dato adicional**: la reescritura **conserva** el prefijo, o sea que el servicio recibe
`/api/estado` tal cual. Se dedujo pidiendo `/api/api/estado`, que devolvió `404`: si la
plataforma quitara el prefijo, esa dirección habría llegado al servicio como `/api/estado` y
habría devuelto `200`. Con eso se eliminaron las rutas duplicadas que existían mientras la
duda estaba abierta.

**Lo que todavía no está probado**: producción. Lo anterior vale para la vista previa. La
misma comprobación se repite sobre el dominio de producción al integrar la rama, y por eso el
endpoint de la cookie no se borra hasta entonces.

---

**Riesgo**: Services está en **beta**: "Behavior, APIs, and limits may change before general
availability". La historia P1 existe para comprobarlo en una hora de trabajo, antes de construir
encima. Si falla, se baja al plan B sin tocar nada del sitio.

---

## D-02. La API corre FastAPI directamente

**Decisión**: la API es una aplicación **FastAPI** en `api/main.py` con la variable `app` al nivel
superior del módulo, declarada como `"entrypoint": "main:app"`. Python **3.12**, fijado en
`pyproject.toml`.

**Razón**: el runtime de Python de Vercel ejecuta aplicaciones ASGI y WSGI tal cual, detecta FastAPI
por su dependencia y espera un nombre `app` al nivel superior en uno de sus ficheros de entrada
reconocidos (`app.py`, `index.py`, `server.py`, `main.py`, `wsgi.py`, `asgi.py`). No hace falta
adaptador ni envoltorio. 3.12 es la versión por defecto de la plataforma, es decir la más rodada;
3.13 y 3.14 están disponibles y no aportan nada que esta feature necesite.

**Consecuencia para el despliegue de prueba**: la prueba de la historia P1 se hace con la pila real,
FastAPI incluido, no con un manejador desnudo. Probar algo distinto de lo que se va a ejecutar no
prueba nada.

---

## D-03. La comprobación programada usa Schedules, no Cron Jobs

**Decisión**: **Vercel Schedules**, estática, declarada en `vercel.json`, con destino **ruta**
—`POST /api/salud`— ejecutándose **cada seis horas**.

**Corrección del 2026-11-06**: esta decisión decía "función privada, sin URL pública", y al ir a
implementarla resultó impracticable con nuestra pila. El destino de función exige tres cosas: el
SDK `@vercel/schedules`, que es de Node; un disparador `schedule/v1beta` que **hace privada la
función entera**, y nuestra API es una sola aplicación ASGI que tiene que seguir sirviendo
`/api/estado`; y un identificador que es la ruta en la salida del build, que hay que averiguar
con `vercel build` y que, si no coincide, **tumba el despliegue**.

El destino de ruta funciona con FastAPI tal cual, y no queda desprotegido: la plataforma envía
`Authorization: Bearer <CRON_SECRET>` en cada petición suya, y el manejador lo comprueba antes de
hacer nada. Eso añade una octava variable de entorno.

**Razón**: tres cosas que Cron Jobs no da en el plan gratuito.

1. **Frecuencia.** Cron Jobs en Hobby está limitado a una ejecución al día; Schedules permite hasta
   cada quince minutos. Esto importa más de lo que parece: ver D-04.
2. **Visibilidad.** Schedules guarda historial de ejecución por tarea, en el panel y en la CLI. Cron
   Jobs solo deja registros de función. Eso alimenta directamente el requisito de que el titular pueda
   consultar si falló.
3. **Entornos.** Schedules corre en producción, en ramas de vista previa y en entornos propios;
   Cron Jobs, solo en producción. Como la verificación de esta feature se hace sobre la vista
   previa, eso deja de ser un detalle.

Además, Cron Jobs es explícitamente **legado**: "Cron Jobs are a legacy feature and will be migrated
to Schedules". Empezar en lo legado es firmar una migración futura por nada.

**Riesgo**: Schedules también está en beta. La mitigación es que es configuración, no código: cambiar
a Cron Jobs son cinco líneas y una ruta protegida, y el aviso por correo no depende de cuál de los dos
se use.

---

### Segunda corrección, 2026-11-06: el disparador sale de Vercel

La tarea nunca apareció en el panel de Vercel. Se verificó que Schedules está en beta pública
**en todos los planes**, así que no es la cuenta; y se descartó que el servicio no recibiera
variables, porque las seis llegan. Quedan dos explicaciones, y ninguna se puede comprobar desde
fuera: que el bloque `schedules` no se aplique dentro de un proyecto con `services` —dos betas
conviviendo— o que el panel lo muestre en un sitio que no encontramos.

**Decisión**: el disparador pasa a una tarea programada de **GitHub Actions** contra el mismo
endpoint, cada seis horas. El bloque de `vercel.json` se conserva: si funciona, escribe de más y
no estorba; si no, no se pierde nada. Son dos mecanismos con fallos distintos, y esa redundancia
sí se justifica.

**Lo que gana**: no depende de ninguna beta, es gratis, el repositorio ya está en GitHub, y el
endpoint y el secreto ya están probados, así que no se toca una línea de código.

**Lo que cuesta, y hay que saberlo**: en un repositorio público, GitHub **desactiva las tareas
programadas tras 60 días sin actividad en el repositorio**, y la ejecución de la propia tarea no
cuenta como actividad. O sea que el mecanismo que protege contra la inactividad caduca por
inactividad. La red de abajo es el aviso por correo que el proveedor de datos manda una semana
antes de suspender, y que restaurar es un clic. Además, las tareas programadas de GitHub se
retrasan bajo carga y algunas se descartan: por eso corre en el minuto 17 y cada seis horas, no
en punto y no una vez al día.

---

## D-04. Una comprobación al día **no** garantiza mantener despierta la base

**Hallazgo que corrige una suposición de la spec.** La documentación de Supabase dice que un proyecto
gratuito se pausa por "too little user database activity over a rolling 7-day period", que las llamadas
a la API y las consultas a la base cuentan, y que "a few user requests to the database each day over the
previous week is typically enough" — pero añade, literalmente, que "it's possible that usage is not
enough to exclude it from automatic pausing even if you use the project yourself". O sea: una sola
petición diaria no es una garantía, es una apuesta.

**Decisión**: la comprobación corre **cada seis horas** —cuatro veces al día— y hace una **escritura
real** en la base, no una consulta de cortesía al endpoint raíz. Cuatro ejecuciones diarias siguen
siendo un consumo irrelevante y caben de sobra en el plan gratuito, pero mueven la señal de actividad
del terreno de "típicamente suficiente" al de holgado.

**Red de seguridad adicional**: Supabase avisa por correo al propietario aproximadamente una semana
antes de pausar un proyecto. Ese aviso es independiente de nuestro sistema y llega aunque todo lo
demás falle.

**Efecto en la spec**: la suposición que decía "se ejecuta una vez al día, que es lo que permite el
plan gratuito" era falsa en los dos extremos. Se corrige.

---

## D-05. La comprobación necesita una tabla, y eso cambia FR-029

**Problema**: la spec dice que el servicio de datos se crea "sin esquema ni contenido". Pero sin
ninguna tabla no hay forma de hacer una consulta que cuente como actividad de base de datos
—PostgREST sin tablas solo devuelve su propia descripción, que no toca la base— ni donde dejar
constancia del resultado, que es lo que el requisito de visibilidad pide.

**Decisión**: el servicio de datos se crea con **exactamente una tabla**, `salud`, de una sola fila,
que existe para la comprobación y para nada más. Cero esquema de aplicación: ni usuarios, ni
proyectos, ni artículos. Esos llegan en la feature 03.

**Razón**: es el mínimo que hace verificables dos requisitos a la vez. Una tabla de una fila es más
barata que la alternativa, que sería postergar la comprobación entera y dejar la base expuesta a la
pausa durante las semanas que tarden las features siguientes.

**Efecto en la spec**: FR-029 se corrige para decir "una única tabla, la de la propia comprobación".

---

## D-06. Enrutado bilingüe: los slugs traducidos se construyen a mano

**Hallazgo**: el enrutado nativo de i18n de Astro **no traduce slugs**. Su documentación exige que
"the file structure and URL structure must match for all languages", y la opción `path` de un locale
cambia el prefijo del idioma, no el nombre de cada página. Tampoco emite `hreflang` por su cuenta.

**Decisión**: enrutado explícito con **dos árboles de páginas reales** y nombres de archivo ya
traducidos, más **un único mapa de rutas** como fuente de verdad.

```text
web/src/pages/en/experience.astro
web/src/pages/es/experiencia.astro
```

El mapa de rutas (`web/src/i18n/rutas.ts`) relaciona cada sección con su slug en los dos idiomas. De
ese mapa salen, sin duplicar nada:

- el enlace del selector de idioma, que lleva a la página equivalente y no al inicio;
- las etiquetas `canonical`, `alternate` y `x-default` del encabezado;
- el índice de direcciones para buscadores.

**Razón**: es la única forma de cumplir el requisito de slugs traducidos, y el mapa único es lo que
evita que el slug de una sección viva en cuatro sitios a la vez, que es justo lo que el principio
"un valor, un solo lugar" prohíbe. Se configura `prefixDefaultLocale: true` para que los dos idiomas
tengan prefijo y ninguno quede en una posición privilegiada, como pide el requisito de direcciones
propias y distinguibles para cada idioma.

**Alternativa rechazada**: dejar las rutas en inglés y traducir solo las etiquetas. Es más barato y es
lo que recomiendan varias guías de la comunidad, pero incumple el requisito de frente.

---

## D-06 bis. La elección de idioma no se guarda

**Hallazgo del análisis cruzado**, no de la investigación inicial: el contrato prometía que la raíz
respetaría la elección de idioma guardada en el navegador. Es imposible. La raíz la resuelve el
servidor, y el servidor no puede leer el almacenamiento del navegador.

**Decisión**: no se guarda el idioma en ninguna parte. La dirección lo lleva, así que navegar y
recargar lo conservan. La raíz resuelve por detección en cada visita.

**Razón**: la alternativa era una cookie de preferencia. No viola el Principio IV —no identifica a
nadie— pero obliga a tocar la política de datos en el mismo cambio, y el Principio V manda construir
lo mínimo que cumple. Lo que la cookie añadiría es un solo caso: quien escribe la raíz a pelo en una
visita posterior. A cambio, cero datos del visitante y cero párrafos legales nuevos.

**Lo que se pierde, dicho de frente**: con el navegador en alemán y el español elegido a mano, volver
a escribir la raíz lleva al inglés. El tema sí se recuerda, porque lo aplica el propio navegador.

---

## D-07. La raíz es la única página que se renderiza en servidor

**Decisión**: `/` se renderiza en servidor —`prerender = false` solo en esa ruta— lee el idioma
preferido del navegador y redirige a `/en/` o a `/es/`. Todo lo demás del sitio se mantiene estático.

**Razón**: la detección de idioma necesita leer la cabecera de la petición, y `Astro.preferredLocale`
solo existe cuando hay una petición que leer. Hacer el sitio entero dinámico por una redirección
sería pagar latencia y presupuesto de rendimiento en todas las páginas para resolver una sola.

---

## D-07 bis. La página de error también se renderiza en servidor

**Hallazgo del análisis cruzado**: las tareas pedían una página de error "en el idioma del
visitante" con un único archivo estático, que solo puede estar en un idioma.

**Decisión**: el 404 se renderiza en servidor y toma el idioma del **prefijo de la dirección
pedida**; inglés cuando no hay prefijo.

**Razón**: es el idioma correcto por definición —quien pidió `/es/algo-que-no-existe` está leyendo en
español— y no cuesta presupuesto, porque un 404 es una respuesta rara. La alternativa, dos páginas
estáticas más una regla de enrutado por prefijo, es más piezas para el mismo resultado.

Así que el sitio tiene **dos** rutas en servidor, no una: la raíz y el error. Todo lo demás que no
depende de datos administrables sigue siendo estático.

---

## D-08. Los valores visuales viven en un archivo CSS

**Decisión**: Tailwind se integra con **`@tailwindcss/vite`** registrado en `vite.plugins` de
`astro.config.mjs`, y todos los tokens viven en **`web/src/styles/tokens.css`**: la paleta clara en
`@theme`, la oscura redefinida bajo el selector del tema oscuro, y tipografías, espaciados, radios y
sombras junto a ellas.

**Razón**: la integración `@astrojs/tailwind` está **deprecada** y su propio paquete remite al plugin
de Vite. Un único archivo CSS cumple el requisito de que cambiar un valor cambie el sitio entero sin
tocar un componente: los componentes solo usan clases de utilidad, que leen los tokens.

**Alternativa rechazada**: `tailwind.config.js` con la configuración en JavaScript. Parte los valores
entre un archivo de configuración y el CSS, que es medio token en cada sitio.

---

## D-09. El tema se aplica antes del primer pintado

**Decisión**: un script **en línea y bloqueante** en el `<head>`, antes de cualquier CSS, que lee la
preferencia guardada —o la del sistema si no hay ninguna— y escribe `data-theme` en `<html>`. El botón
flotante solo cambia ese atributo y guarda la elección.

**Razón**: es la única forma de que no haya destello. Un script diferido o un componente hidratado
corren después del primer pintado, que es exactamente cuando el destello ya ocurrió. En línea cuesta
menos de un kilobyte y no añade ninguna petición.

**Degradación**: todo el acceso al almacenamiento va envuelto en `try`/`catch`. Si el navegador lo
bloquea, se usa la preferencia del sistema y el sitio funciona igual, como pide el requisito de
degradación.

---

## D-10. El sitio se publica bloqueado a buscadores con una cabecera

**Decisión**: una cabecera **`X-Robots-Tag: noindex`** aplicada a todas las rutas desde la
configuración de nivel superior de `vercel.json`, más un `robots.txt` que excluye la zona de
administración.

**Razón**: una cabecera en un solo sitio cubre todas las rutas, incluidas las estáticas y los archivos,
y levantar el bloqueo en la feature 02 es borrar un bloque. Una etiqueta `<meta robots>` en la
plantilla obligaría a lógica por página y se olvidaría en la que no usa esa plantilla. Un
`robots.txt` con `Disallow` por sí solo no sirve para esto: impide el rastreo, no la indexación.

---

## D-11. El correo sale con la biblioteca estándar

**Decisión**: `smtplib` y `email.message` de la biblioteca estándar de Python, al puerto **587** con
**STARTTLS**, con el envío **esperado** antes de devolver la respuesta HTTP.

**Razón**: no se añade una dependencia por veinte líneas. Vercel bloquea el puerto 25 pero no el 587.
Y el envío tiene que completarse antes de que la función devuelva: en un entorno sin servidor, lo que
quede pendiente cuando la respuesta sale puede no ejecutarse nunca.

---

## D-12. Consultar la base desde Python, sin dependencias

**Decisión**: `urllib.request` de la biblioteca estándar contra el endpoint REST del proyecto de datos,
con la clave secreta en la cabecera **`apikey`**, para escribir la fila de `salud`.

**Dos detalles que la documentación de Supabase fija y que es fácil equivocar:**

- La clave va en `apikey`, **no** en `Authorization: Bearer`. Las claves nuevas se envían así.
- La clave secreta devuelve **401 si la petición parece venir de un navegador**: el servidor mira el
  `User-Agent`. Es una defensa a nuestro favor, pero obliga a que la petición de Python no finja ser
  un navegador. Si alguna vez da 401 sin motivo aparente, mirar ahí primero.

**Qué clave**: la **secreta moderna** (`sb_secret_...`), que sustituye a la antigua `service_role` y
salta las políticas de acceso igual. Supabase deprecia las claves JWT heredadas a finales de 2026,
así que empezar con ellas sería firmar una migración por nada.

**Razón**: es una sola petición HTTP. El cliente oficial de Supabase traería una dependencia y su árbol
entero para eso. Si la feature 03 necesita consultas de verdad, se reconsidera entonces, con el
problema delante.

---

## D-13. Qué se prueba y con qué

**Decisión**:

| Qué                                                  | Con qué                                           | Por qué                                                                                                                          |
| ---------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Mapa de rutas y negociación de idioma                | **Vitest**                                        | Son funciones puras con casos límite reales: idioma no soportado, cabecera ausente, slug inexistente.                            |
| Lógica de la comprobación y del aviso                | **pytest**                                        | Igual: decide, formatea y maneja fallos.                                                                                         |
| Teclado, ausencia de destello, responsive, contraste | **Verificación manual sobre el sitio desplegado** | La constitución ya exige verificar en el sitio real, y automatizar un navegador para esta feature costaría más que lo que cubre. |

**Pospuesto a conciencia**: pruebas de navegador automatizadas. Se reconsideran cuando haya formularios
y sesión que romper, en la feature 03.

---

## D-14. Cómo se miden los números de rendimiento

**Decisión**: **PageSpeed Insights** sobre la dirección pública ya desplegada, perfil de móvil, mediana
de tres ejecuciones, como puerta antes de integrar código a `main`.

**Razón**: ejecuta Lighthouse con perfil de móvil y red simulada por defecto, no hay nada que instalar
y no cuesta nada. El criterio de la spec se fijó así en la clarificación del 2026-11-05.

---

## Resumen de riesgos abiertos

| Riesgo                                                  | Probabilidad | Qué lo contiene                                                                                   |
| ------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| Vercel Services, en beta, no sirve o cambia             | Media        | La historia P1 lo prueba antes de construir. Plan B: carpeta `/api`. Plan C: dos proyectos.       |
| Vercel Schedules, en beta, cambia                       | Baja         | Es configuración. Volver a Cron Jobs son cinco líneas.                                            |
| La base se pausa igual pese a la comprobación           | Baja         | Cuatro escrituras diarias, más el aviso por correo que Supabase manda una semana antes de pausar. |
| El bloqueo a buscadores se olvida al publicar contenido | Media        | Queda como requisito explícito de la feature 02, no como nota.                                    |

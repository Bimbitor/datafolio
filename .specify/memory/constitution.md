# Datafolio Constitution

Datafolio es el portafolio personal de Javi Giraldo: su carta de presentación profesional
y académica, y su punto de contacto con reclutadores. Esta constitución gobierna cómo se
construye. Las decisiones de producto viven en `docs/project-brief.md`; los valores
visuales, en `docs/design-tokens.md`. Esta constitución manda sobre cómo se trabaja; esos
documentos mandan sobre qué se construye.

## Core Principles

### I. Especificación antes que código (NO NEGOCIABLE)

Ninguna línea de código de la aplicación se escribe antes de que exista una especificación
aprobada para la feature que la contiene. El orden es constitución → `/speckit-specify` →
`/speckit-clarify` → `/speckit-plan` → `/speckit-tasks` → `/speckit-implement`, y una
feature no avanza al siguiente paso con preguntas abiertas en el actual.

Toda duda sin resolver se marca explícitamente en el documento donde aparece y se decide
antes de planificar. Está prohibido resolverla asumiendo en silencio durante la
implementación: una suposición no escrita es una decisión que nadie tomó.

Rationale: este proyecto nació de una idea dictada en desorden. El valor de SDD está en
que la discusión ocurra en documentos baratos de cambiar y no en código ya escrito.

### II. Un valor, un solo lugar

Todo valor que aparece más de una vez tiene exactamente un origen:

- Los colores, tipografías, espaciados, radios y sombras salen del archivo de tokens, que
  implementa `docs/design-tokens.md`. Ningún componente escribe un valor literal. Si hay
  que tocar un componente para que un cambio de paleta se vea, ese componente está mal
  escrito y es un defecto.
- El contenido estático (home, experiencia, contacto, política de datos) vive en el código
  y se despliega con commits. El contenido administrable (proyectos, artículos,
  comentarios) vive en la base de datos. Ningún dato vive en los dos sitios.
- Las direcciones de correo, el destino del formulario y cualquier parámetro de entorno son
  variables de entorno, nunca literales en el código.
- Los PDFs del CV son archivos versionados que el sitio sirve tal cual. El sitio no genera,
  renderiza ni transforma documentos en tiempo de ejecución.

Rationale: el portafolio va a cambiar de paleta, de correo y de contenido muchas veces.
Cada valor duplicado es un cambio futuro que se hará a medias.

### III. El servidor es la única autoridad

La seguridad de este sitio nunca depende de que algo esté oculto.

- Toda operación de escritura verifica la credencial en el servidor. Ocultar un botón o una
  ruta no protege nada: un visitante no autenticado no puede escribir ni llamando a la API
  directamente.
- El frontend nunca se comunica con la base de datos. Solo el backend tiene credenciales de
  datos.
- Ningún secreto aparece en el repositorio, en su historial, ni en el JavaScript que llega
  al navegador. El repositorio es público y eso es una decisión, no un descuido: obliga a
  que la protección sea real.
- Hay un único usuario administrador y no existe forma de crear otro desde la interfaz.
- Todo contenido que entra desde fuera del proyecto — el README de un repositorio, el
  cuerpo de un comentario — se trata como texto sin confianza y nunca como HTML ejecutable.

Rationale: el formulario de login será sondeado por robots a los pocos días de estar en
línea, y un portafolio comprometido daña justo lo que este sitio existe para proteger, que
es la reputación profesional de su dueño.

### IV. Del visitante no se guarda nada

No se almacena dirección IP, agente de usuario, cookie de identificación ni huella de
dispositivo de ninguna persona que visite el sitio. De un comentario se guarda el texto, la
fecha y el nombre solo si quien comenta decide escribirlo. Los mensajes del formulario de
contacto se envían por correo y no se persisten. La analítica es agregada por hora y
anónima.

La consecuencia se acepta de frente y se comunica: el panel cuenta eventos, no personas. No
habrá visitantes únicos ni sesiones, y las cifras son aproximadas. Donde el límite de abuso
necesite distinguir orígenes, se usa un hash con sal que se purga al expirar la ventana y
del que no se puede reconstruir la dirección.

La página de política de tratamiento de datos describe exactamente lo que el sistema hace.
Si el comportamiento cambia, la política cambia en el mismo cambio, nunca después.

Rationale: no guardar es la única forma de no filtrar, y una política que no corresponde
con el sistema es peor que no tenerla.

### V. Lo mínimo que cumple, terminado

Se construye la versión más pequeña que satisface el requisito, y se construye completa.

- Sin abstracciones, envoltorios, opciones ni configuración que nadie pidió. Sin código
  "para después".
- No se añade una dependencia por unas pocas líneas. Se prefiere lo que el proyecto o la
  plataforma ya ofrecen.
- Ser perezoso aplica a la solución, nunca al trabajo: un cambio incluye todo lo que rompe
  —llamadores, pruebas, datos de prueba, documentación— o no está hecho.
- Nunca se recorta: validación en los límites de confianza, manejo de errores que evita
  pérdida de datos, seguridad, accesibilidad, ni nada que el titular haya pedido.
- Un atajo con un límite conocido se documenta en el código, diciendo cuál es el límite y
  cuándo habría que reemplazarlo.

Rationale: este portafolio lo mantiene una sola persona en ratos libres. Cada pieza de más
es deuda que nadie va a pagar.

## Restricciones técnicas y de producto

Estas restricciones son vinculantes y solo se cambian enmendando esta constitución o
actualizando `docs/project-brief.md`, que es su fuente.

- **Stack fijo**: Astro con islas interactivas y Tailwind en el frontend; FastAPI en Python
  como única puerta de escritura; Supabase como base de datos; monorepo; despliegue en
  Vercel.
- **Costo cero**: todo debe funcionar dentro de los planes gratuitos de Vercel y Supabase, y
  con cuentas de Gmail. No hay dominio propio ni hosting de pago. Cualquier propuesta que
  introduzca un costo recurrente requiere aprobación explícita del titular antes de
  implementarse.
- **Sin estado en memoria**: el backend corre como función serverless. El límite de tasa, la
  caché de los README y cualquier otro estado persisten en la base de datos, nunca en
  variables de proceso.
- **Bilingüe o no se publica**: todo artículo y todo proyecto publicado existe en español y
  en inglés. El formulario de administración no permite publicar con un idioma vacío.
  Guardar como borrador con un solo idioma sí está permitido.
- **Presupuesto de rendimiento**: en las páginas públicas, LCP por debajo de 2.5 s y CLS por
  debajo de 0.1 en móvil, y menos de 100 KB de JavaScript. Un cambio que rompa el
  presupuesto se revisa antes de seguir.
- **Accesibilidad**: navegación completa por teclado con foco visible, y texto alternativo
  en los dos idiomas en toda imagen con contenido. Las reglas de contraste de
  `docs/design-tokens.md` se respetan sin excepción.
- **Sin animaciones** en esta versión. Los cambios de estado usan transiciones de 150 ms
  como máximo, o ninguna.
- **Datos de prueba fuera de producción**: los proyectos inventados que se usan para
  desarrollar no se publican en el sitio en producción. Un portafolio que muestra proyectos
  falsos a un reclutador es un problema peor que uno incompleto.

## Flujo de trabajo y puertas de calidad

- **Orden de las features**: 01 sitio base → 02 contenido estático → 03 admin y
  autenticación → 04 proyectos → 05 blog y comentarios → 06 analítica → 07 diseño visual.
  La feature 03 va obligatoriamente antes que la 04 y la 05, porque ambas dependen de la
  autenticación.
- **Pruebas exigidas**: toda operación CRUD (proyectos, artículos, borradores,
  comentarios), los dos formularios públicos, el flujo de autenticación, el renderizado y
  saneado de Markdown, y la lógica de filtros. Lógica nueva no trivial sin su prueba o
  verificación está incompleta.
- **Secretos**: `.env` y `.env.*` nunca se versionan; `.env.example` lleva solo nombres de
  variables. El escaneo automático de secretos corre antes de cada commit y en integración
  continua. Un secreto publicado por error se rota en el proveedor; borrar el commit no
  basta.
- **Skills del proyecto**: el diseño visual se trabaja con Impeccable; los textos del sitio,
  en los dos idiomas, pasan por `humanizer`; la implementación sigue el criterio de
  `ponytail`. Impeccable sustituye a `frontend-design`, que queda retirada.
- **Ramas y `main`**: se sigue la convención de Spec Kit. Cada feature tiene **una rama
  propia, nombrada como su carpeta de spec** (`001-sitio-base`), creada al especificarla, y
  esa rama acompaña a la feature de principio a fin: spec, plan, tareas y código viajan
  juntos y se integran juntos. `main` es producción —Vercel despliega desde ahí, así que
  integrar es publicar— y solo recibe trabajo que cumple la Definición de hecho: nunca
  código a medias, roto o sin probar. Antes de integrar, la rama se revisa en el despliegue
  de vista previa que la plataforma genera para ella. Los documentos de alcance del
  proyecto —constitución, brief, tokens, viabilidad, política— no pertenecen a ninguna
  feature y viven en `main`.
- **Un solo entorno de datos.** Hay un único proyecto de Supabase, el de producción. No hay
  base de pruebas ni pila local: las vistas previa comparten la base de producción y la
  verificación se hace sobre el sitio desplegado. Es una decisión tomada a conciencia, y
  deja tres reglas que la hacen sostenible:
  - **Las pruebas automáticas no son destructivas.** Crean sus propios registros y los
    borran al terminar. Nunca vacían tablas, nunca tocan el usuario administrador, nunca
    borran contenido que no hayan creado ellas.
  - **El contenido creado al probar nace como borrador** y se elimina al terminar. Un
    borrador no es visible para nadie, así que probar el panel no ensucia el sitio público.
  - Las migraciones de esquema se aplican **de forma deliberada, al integrar a `main`**,
    nunca desde una rama en curso: si no, la base queda por delante del código desplegado.
- **Commits**: formato `vX.Y.Z-AAAA-MM-DD-tipo: descripción`, en español, describiendo el
  cambio y no el proceso.
- **Definición de hecho**: una feature está terminada cuando cumple sus criterios de
  aceptación, sus pruebas pasan, no deja secretos expuestos, respeta el presupuesto de
  rendimiento y la accesibilidad, y está desplegada y verificada en el sitio real. "Funciona
  en mi máquina" no cuenta.

## Governance

Esta constitución está por encima de cualquier otra práctica del proyecto. Ante un
conflicto entre esta constitución y una spec, un plan o una costumbre, manda la
constitución.

**Enmiendas**: cualquier cambio a un principio o a una restricción requiere aprobación
explícita del titular, queda registrado en el Sync Impact Report del propio archivo y se
aplica en un commit propio. Una restricción no se "interpreta con flexibilidad" durante una
implementación: o se cumple, o se enmienda antes.

**Versionado**: MAJOR cuando se elimina o redefine un principio de forma incompatible;
MINOR cuando se añade un principio o se amplía materialmente una sección; PATCH para
precisiones, redacción y correcciones sin efecto semántico.

**Cumplimiento**: cada `/speckit-plan` verifica que el plan no contradiga esta
constitución, y lo deja por escrito. Cada revisión de código comprueba lo mismo. Toda
complejidad añadida debe justificarse contra el Principio V; si no hay justificación, se
quita.

**Guía de ejecución**: `docs/project-brief.md` para qué se construye y
`docs/design-tokens.md` para los valores visuales. Esos documentos se actualizan cuando una
decisión cambia, en el mismo cambio que la aplica.

**Version**: 1.2.0 | **Ratified**: 2026-11-05 | **Last Amended**: 2026-11-05

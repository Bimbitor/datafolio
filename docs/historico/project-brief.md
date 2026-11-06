# Datafolio — Brief de proyecto (entrada histórica para SDD)

> Estado: **histórico**. Aquí se ordenó la idea y se tomaron las decisiones de producto, en nueve rondas,
> antes de que existiera cualquier spec. Ya no es la autoridad de nada: manda la constitución sobre cómo se
> trabaja y manda la spec de cada feature sobre qué se construye. Se conserva por dos razones: es el registro
> de por qué el proyecto es como es, y es la entrada de la que saldrán las specs de las features 02 a 07,
> que todavía no están escritas. Donde una spec aprobada diga otra cosa, la spec gana sin discusión.
>
> Este documento es la _entrada_ al flujo Spec-Driven Development.
> Orden previsto: `/speckit.constitution` → `/speckit.specify` (por feature) → `/speckit.clarify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`.
> Nada de código hasta que las specs estén aprobadas.
>
> Todo lo marcado `[P-xx]` está **sin decidir** y debe resolverse antes del `/speckit.plan` de la feature que lo contiene.
> Si algo aquí contradice `docs/historico/research/`, manda este documento; si contradice una spec en `specs/`, manda la spec.
>
> **Rondas de decisiones** (todas el 2026-11-04):
>
> - Ronda 1: P-01 a P-07 (identidad, tomada de los CVs), P-09, P-10, P-12, P-13, P-14, P-16, P-17, P-18, P-19, P-24.
> - Ronda 2: P-15 (render del README).
> - Ronda 3: P-20, P-21, P-23, P-25, P-26, P-27, P-28, P-29, P-30, P-31, P-32, P-33, P-37 a P-42.
> - Ronda 4: P-08, P-22, P-43, P-48, P-51, y el dominio cambia a `javidatastudio.dev` (verificado disponible el 2026-11-04). P-49 decidido en su forma; falta elegir proveedor.
> - Ronda 5: P-51 revisado — el repositorio es **público**, con la exigencia de que ninguna clave aparezca en las fuentes ni en el historial (RS-16).
> - Ronda 6: **sin dominio propio por ahora** (P-37 aplazado como P-52). Correo público `javidatastudio@gmail.com`. P-44 y P-49 resueltos sobre Gmail.
> - Ronda 7: P-34 (tokens, en `design-tokens.md`), P-35 (dos fotos y carpetas) y P-36 (accesibilidad acotada). La skill de diseño pasa a Impeccable.
> - Ronda 8: P-11 (sin animaciones en esta versión), P-45 y P-46 (analítica propia, agregada por hora), P-50 (el teléfono se publica). P-52 retirado: no hay dominio propio y no está planeado.
> - Ronda 9: P-47 aprobado. **El brief no tiene pendientes abiertos.** Listo para la constitución y la primera spec.

---

## 1. Propósito

Portafolio personal que funciona como carta de presentación profesional y académica, y como punto de contacto.
No es un blog con currículum pegado ni una landing de una sola página: es un sitio con secciones navegables, cada una con su propia URL.

**Audiencia primaria:** reclutadores técnicos y hiring managers que llegan por LinkedIn o por un enlace en el CV.
**Audiencia secundaria:** colegas y lectores del blog que llegan por búsqueda.

**Objetivo:** que un reclutador entienda en ~60 segundos quién soy, qué he hecho y cómo contactarme, y que pueda llegar al mejor proyecto en dos clics.

**Métricas de éxito:**

- Un visitante nuevo llega desde el home a un proyecto en ≤2 clics, y a un canal de contacto en ≤1 clic desde cualquier página.
- CV descargable (ES/EN) desde la sección de experiencia sin pasos intermedios.
- La interacción se mide de forma agregada y se consulta desde el panel de administración (ver §5.9).

## 2. Identidad y contenido del titular

Fuente: `CV_Javi_Giraldo_EN.pdf` y `CV_Javi_Giraldo_ES.pdf` (ambos CVs del titular, revisados el 2026-11-04). Estos datos son el contenido real de las secciones estáticas.

**Identidad**

- Nombre legal completo: Javi Johan Rodríguez Giraldo. **Solo aparece en los PDFs del CV**, no en el sitio (ver §8.3).
- Nombre público / marca del sitio: **Javi Giraldo**.
- Titular EN: _Data Engineer | Database Developer_ · Titular ES: _Ingeniero de Datos | Desarrollador de Bases de Datos_.
- Ubicación: Bogotá, Colombia (GMT-5). Modalidad: presencial, híbrido o remoto.
- Idiomas: español nativo, inglés B2 (competencia profesional).
- El texto final del hero y de "sobre mí" se redacta en la feature 02 con la skill `humanizer`, partiendo del perfil profesional del CV.

**Contacto público**

| Canal    | Valor                                                                        |
| -------- | ---------------------------------------------------------------------------- |
| Correo   | **javidatastudio@gmail.com** (dirección pública del sitio, la vCard y el CV) |
| WhatsApp | +57 315 851 5323                                                             |
| LinkedIn | linkedin.com/in/javi-giraldo                                                 |
| GitHub   | github.com/Bimbitor                                                          |

**Dominio:** por ahora **ninguno propio**. El sitio vive en el subdominio gratuito que asigna Vercel (`…vercel.app`), para no introducir un costo anual mientras el portafolio se construye.

- `*.vercel.app` también está en la lista de precarga HSTS, así que RS-01 (solo HTTPS) se cumple igual, sin pagar nada.
- No hay dominio propio y no está planeado en esta versión. Si algún día se compra uno, habrá que redirigir el subdominio de Vercel con redirecciones permanentes y actualizar `canonical`, `hreflang` y el sitemap para no perder lo indexado. Nada se rompe, solo cuesta algo más de trabajo que hacerlo desde el principio.

**Experiencia laboral** (la más reciente primero)

| Rol                               | Organización     | Lugar            | Periodo            |
| --------------------------------- | ---------------- | ---------------- | ------------------ |
| Database Developer                | BCD Travel       | Bogotá, Colombia | 07/2024 – presente |
| Analista de Tecnología            | BCD Travel       | Bogotá, Colombia | 05/2023 – 07/2024  |
| Coordinador de Registro y Control | Educación Futuro | Bogotá, Colombia | 08/2022 – 12/2022  |

**Formación académica**

| Programa                                                                              | Institución                       | Periodo            |
| ------------------------------------------------------------------------------------- | --------------------------------- | ------------------ |
| Ciencia de Datos (en curso, 5.º semestre)                                             | Fundación Universitaria Compensar | 07/2024 – presente |
| Misión TIC 2022 — Programación                                                        | Universidad Sergio Arboleda       | 07/2021 – 12/2021  |
| Técnico Laboral en Mantenimiento y Soporte de Equipos y Tecnologías de la Información | Educación Futuro                  | 01/2020 – 08/2020  |

**Certificaciones y formación complementaria:** AWS Certified Cloud Practitioner (CLF-C02, en preparación), AWS Certified Data Engineer – Associate (DEA-C01, en preparación), Git y GitHub (Platzi), Python para Ciencia de Datos (Platzi), SQL Server 2019 Esencial (LinkedIn Learning), Databricks: Arquitectura Delta Lake, Herramientas de IA para Developers.

**Objetivo profesional:** roles de Data Engineer en entornos cloud, apoyado en 3+ años en BCD Travel (SQL Server, SSIS, T-SQL, Python, Azure DevOps) y en formación activa en AWS (S3, Glue, PySpark, Athena) más la carrera de Ciencia de Datos.

**Proyectos**

- Real: **Data Lakehouse sobre AWS** — proyecto personal, en construcción, 2026. S3 con arquitectura medallion (Bronze/Silver/Gold), Glue + PySpark, Glue Data Catalog, Athena sobre Parquet, reglas de calidad con cuarentena de rechazados, control de accesos con IAM. Repositorio y documentación en preparación.
- Durante el desarrollo, el catálogo se puebla con **proyectos de prueba inventados** para ejercitar tarjetas, buscador, filtros y CRUD. El titular reemplazará esos registros por los reales antes de publicar.
- Regla asociada: los proyectos de prueba **no se publican** en el dominio de producción. Un portafolio que muestra proyectos inventados a un reclutador es un problema distinto y peor que una página incompleta. Viven como datos de semilla en desarrollo, o en estado borrador si ya están en la base de datos de producción.

Los demás contenidos del CV (competencias técnicas agrupadas, logros por rol) se transcriben en la feature 02 desde los dos PDFs; no se reescriben aquí.

## 3. Alcance

### Dentro del alcance

Sitio multisección con URLs propias, bilingüe ES/EN, modo claro/oscuro, responsive; blog en Markdown y catálogo de proyectos administrables por el titular, ambos obligatoriamente en los dos idiomas y con borradores; comentarios abiertos y anónimos con aprobación previa; panel de analítica agregada; página de política de tratamiento de datos; descarga de CV en PDF desde archivos versionados en el repo.

### Fuera del alcance (explícito)

- Registro de usuarios. Hay **un solo** usuario (el titular) y no existe botón de registro: no habrá usuarios nuevos.
- Generación o renderizado de PDF en tiempo de ejecución. Los PDFs del CV son archivos estáticos que el titular sube por commit; el sitio solo los sirve.
- Pagos, newsletter, buscador global del sitio.
- Edición colaborativa, roles múltiples, borradores compartidos.
- **Hosting de pago.** Todo debe funcionar en el plan gratuito de Vercel (ver §7).
- **Dominio propio.** El sitio vive en el subdominio de Vercel. No está planeado comprar uno en esta versión.
- **Animaciones.** Esta versión no las lleva (ver RF-05).
- Almacenamiento de datos personales de los visitantes (ver §5.6, §5.9 y §8.2).

## 4. Mapa del sitio (cada sección con URL propia)

Rutas con prefijo de idioma y **slugs traducidos** en cada idioma (decisión de SEO):

| Ruta ES                 | Ruta EN               | Contenido                                                                         | Fuente                   |
| ----------------------- | --------------------- | --------------------------------------------------------------------------------- | ------------------------ |
| `/es/`                  | `/en/`                | Home: presentación, resumen de cada sección sin detalle, CTAs                     | Estático (código)        |
| `/es/experiencia`       | `/en/experience`      | Formación + experiencia en línea de tiempo filtrable; descarga de CV              | Estático + PDFs del repo |
| `/es/proyectos`         | `/en/projects`        | Catálogo de tarjetas con buscador y filtros                                       | Base de datos            |
| `/es/proyectos/[slug]`  | `/en/projects/[slug]` | Ficha: título, enlace al repo, enlace a producción, README renderizado            | Base de datos + GitHub   |
| `/es/blog`              | `/en/blog`            | Índice de artículos                                                               | Base de datos            |
| `/es/blog/[slug]`       | `/en/blog/[slug]`     | Artículo en Markdown renderizado + comentarios aprobados                          | Base de datos            |
| `/es/contacto`          | `/en/contact`         | GitHub, LinkedIn, WhatsApp, correo, formulario, botón de Claude, guardar contacto | Estático + formulario    |
| `/es/politica-de-datos` | `/en/data-policy`     | Política de tratamiento de datos                                                  | Estático (código)        |
| `/admin/...`            | `/admin/...`          | Panel: CRUD, borradores, moderación, analítica                                    | Base de datos            |

El home muestra un resumen de todo sin detalle; el detalle vive en cada sección. No se usan anclas como sustituto de rutas.

**Idioma en la URL:** cada idioma tiene su propia URL con prefijo, ambas indexables, con slugs traducidos (`/es/experiencia` ≠ `/en/experience`). Cada página declara `hreflang` hacia su equivalente y `x-default` hacia la versión en inglés, más una `canonical` propia. La raíz `/` redirige al idioma detectado del navegador, con inglés como destino por defecto. El panel de administración es monolingüe (español) y no se indexa.

## 5. Requisitos funcionales

### 5.1 Global

- **RF-01** Modo oscuro y claro, con botón flotante permanente en la esquina inferior derecha, disponible en todas las páginas.
- **RF-02** El tema inicial respeta la preferencia del sistema del visitante; la elección manual persiste entre visitas y no provoca destello de tema incorrecto al cargar.
- **RF-03** Sitio bilingüe inglés/español con selector de idioma visible. El idioma inicial se detecta del navegador; si no se puede determinar o no es español, se sirve **inglés por defecto**. La elección manual persiste y gana sobre la detección.
- **RF-04** Todos los colores se consumen desde un único archivo de variables/tokens; ningún valor de color se escribe suelto en un componente. Cambiar la paleta allí debe repintar el sitio completo.
- **RF-05** **Sin animaciones en esta versión.** No hay animaciones de entrada, transiciones entre páginas ni microinteracciones decorativas. Lo único que se mueve es lo que tiene que moverse para que un control se entienda: un menú que se abre, un estado `hover` o `focus` que cambia de color.
  - Se gana en rendimiento y en tiempo de construcción, y se evita lo que más abarata un portafolio, que son animaciones mal calibradas.
  - Los cambios de estado usan transiciones de 150 ms como mucho, o ninguna. Eso no es "animación" y no necesita catálogo.
  - Nada de esto cierra la puerta: los tokens y la estructura permiten añadirlas más adelante sin rehacer nada.
- **RF-06** Responsive con los breakpoints estándar de Tailwind: `sm` 640, `md` 768, `lg` 1024, `xl` 1280, `2xl` 1536. Diseño móvil primero.
- **RF-07** Navegación persistente con acceso a todas las secciones y a contacto.

### 5.2 Home

- **RF-08** Presenta quién soy (profesional y académicamente), trayectoria resumida, objetivos, y un adelanto de proyectos y blog; cada bloque enlaza a su sección.
- **RF-09** Integra fotografía propia como parte del diseño, no como foto pegada: la imagen se compone con la paleta y el layout.

### 5.3 Experiencia

- **RF-10** Línea de tiempo única que combina formación académica y experiencia laboral, ordenada cronológicamente.
- **RF-11** La línea de tiempo filtra en cliente, sin recarga, por cuatro facetas combinables: **tipo** (académico/laboral), **rango de años**, **tecnología** y **empresa o institución**.
- **RF-12** Botón de descarga del CV en PDF, en español o en inglés. El sitio sirve un archivo ya existente en `public/cv/cv-es.pdf` y `public/cv/cv-en.pdf`; no construye ni renderiza nada.
  - El archivo llega al visitante con **la fecha de la descarga en el nombre**: `CV_Javi_Giraldo_ES_2026-11-04.pdf`. Se consigue con el atributo `download` del enlace, calculando el nombre en el momento del clic.
  - En la página **no se muestra ninguna fecha de actualización**: así no hay nada que mantener ni que pueda quedar desactualizado.

### 5.4 Proyectos

- **RF-13** Catálogo de tarjetas, una por proyecto.
- **RF-14** Buscador que filtra por nombre, por etiquetas y por fecha, combinables.
- **RF-15** Cada proyecto requiere: título, enlace al repositorio, enlace a la web o entorno de producción, y descripción. Título y resumen existen en los dos idiomas (ver RF-23).
- **RF-16** La descripción del proyecto es el README del repositorio de GitHub, renderizado como **GitHub Flavored Markdown** (tablas, listas de tareas, enlaces automáticos, bloques de código con resaltado de sintaxis), con estas reglas:
  - **Todo el HTML embebido se elimina**, no se filtra por lista blanca. Consecuencia aceptada: los badges de shields.io, las secciones plegables y los encabezados centrados desaparecen del render en el sitio. A cambio, ningún contenido del repositorio puede ejecutar código en el dominio del portafolio.
  - **Mermaid no se renderiza.** Un bloque ` ```mermaid ` se muestra como bloque de código con su texto.
  - **Las rutas relativas no se reescriben.** Una imagen o enlace relativo del README queda roto en el sitio y es un resultado aceptado. Si el titular quiere que una imagen se vea, usa una URL absoluta en el README.
  - Los encabezados del README se degradan un nivel (`#` → `<h2>`) para no competir con el `<h1>` de la página, y el resultado se envuelve en una capa tipográfica.
- **RF-17** El README se trae **en cada visita, con caché**: si la copia está vigente se sirve esa; si está vencida se consulta GitHub y se actualiza. Si GitHub falla o se agota el límite de tasa, se sirve la última copia guardada antes que mostrar error o vacío. TTL por defecto **1 hora**, configurable por variable de entorno.
- **RF-18** El panel incluye un botón por proyecto para **forzar la actualización del README**, que invalida la caché de ese proyecto y la vuelve a traer de inmediato.
- **RF-19** Crear, editar y eliminar proyectos es exclusivo del titular autenticado.

### 5.5 Blog

- **RF-20** Artículos escritos en Markdown y renderizados al visitante.
- **RF-21** Plantilla por defecto estilo Notion: al crear un artículo, el editor ofrece imagen de portada y título.
- **RF-22** Si no se agrega imagen de portada, se usa un fondo de color genérico acorde a la paleta, derivado de los mismos tokens.
- **RF-23** **Contenido bilingüe obligatorio para publicar.** Todo artículo y todo proyecto publicado existe en español y en inglés. El formulario del panel presenta los campos de texto duplicados (una vez en español, una vez en inglés) y **no permite publicar** si falta uno de los dos idiomas. No hay contenido publicado monolingüe, así que no existe el caso de "no disponible en tu idioma".
- **RF-24** **Borradores.** Se puede guardar en estado borrador con un solo idioma lleno, o a medias, sin límite de cantidad. El panel muestra la **lista de borradores y pendientes por publicar** para retomarlos cuando el titular quiera. Los borradores no son visibles para nadie más y no se indexan.
- **RF-25** El editor del panel es un campo de texto Markdown con previsualización en vivo del resultado renderizado. No es un editor enriquecido.
- **RF-26** Crear, editar y eliminar artículos es exclusivo del titular autenticado.

### 5.6 Comentarios

- **RF-27** Comentarios abiertos sin registro, **tanto en artículos del blog como en fichas de proyecto**. El nombre es opcional; sin nombre se publica como anónimo. El panel de moderación muestra los de ambos tipos en una sola cola, indicando a qué contenido pertenece cada uno.
- **RF-28** El contenido del comentario se trata como texto, nunca como HTML ni Markdown ejecutable: se escapa al renderizar.
- **RF-29** **Moderación previa.** Un comentario enviado queda pendiente y no es visible para nadie salvo el titular en el panel. Solo aparece cuando el titular lo aprueba. Al enviarlo, el visitante ve confirmación de que quedó en revisión.
- **RF-30** El titular aprueba, rechaza o elimina cualquier comentario desde el panel.
- **RF-31** **No se almacenan datos personales de quien comenta.** Se guarda únicamente el texto del comentario, el nombre si decidió escribirlo, y la fecha. No se guarda IP, ni user agent, ni identificador alguno del visitante.
- **RF-32** Bajo el formulario de comentarios aparece un subtexto breve que lo aclara: no se guardan datos personales y el comentario pasa por revisión antes de publicarse.
- **RF-33** Aun sin guardar datos, el formulario necesita límite de tasa y longitud máxima; sin ellos la cola de moderación se llena de spam aunque el sitio público quede limpio. El límite se implementa **sin persistir la IP**: se guarda un hash con sal del origen junto a un contador de ventana corta, que se borra al expirar la ventana (ver RS-07).

### 5.7 Contacto

- **RF-34** Enlaces a GitHub, LinkedIn, WhatsApp con mensaje directo, y correo.
- **RF-35** Formulario alternativo: el visitante escribe y el mensaje **llega al correo del titular**, hoy `javidatastudio@gmail.com`. El mensaje **no se guarda en la base de datos**. La dirección de destino vive en una variable de entorno, para poder cambiarla sin tocar código ni volver a desplegar.
- **RF-36** El formulario incluye una **casilla de aceptación obligatoria** de la política de tratamiento de datos, con el enlace puesto sobre la palabra "política de tratamiento de datos", que lleva a `/es/politica-de-datos` o `/en/data-policy`. Sin aceptar, el formulario no se envía.
- **RF-37** Existe la página de **política de tratamiento de datos** en los dos idiomas, con su propia URL. Borrador inicial en `docs/politica-de-datos-borrador.md`; debe reflejar exactamente lo que el sistema hace y no más.
- **RF-38** En móvil se ofrece "guardar contacto" (descarga de un archivo vCard `.vcf`, la tarjeta de contacto que el teléfono ofrece agregar a la agenda). La detección es **por ancho de pantalla**, reutilizando los breakpoints de RF-06: visible por debajo de `md` (768px), oculto de ahí en adelante. Se resuelve con CSS, sin JavaScript ni detección de dispositivo.
  - Efecto aceptado: alguien con una ventana de escritorio muy angosta verá el botón. Descargar un `.vcf` en un computador no causa ningún daño; a lo sumo no le sirve.
  - Campos de la vCard: nombre público, titular profesional, correo, teléfono, sitio web, LinkedIn y GitHub.
- **RF-39** **Botón de Claude (opción a).** Un botón abre una conversación nueva en Claude con un mensaje ya escrito que apunta al portafolio y pide un resumen del perfil. No consume ninguna API de pago ni requiere backend: es un enlace. El texto del mensaje se redacta en la feature 02 con `humanizer`.
  - Riesgo aceptado: depende del formato de URL de un tercero. Si Claude cambia ese contrato, el botón deja de prellenar el mensaje y abre una conversación vacía. No rompe el sitio.

### 5.8 Autenticación y administración

- **RF-40** Zona de administración bajo `/admin` desde la que el titular gestiona proyectos, artículos, borradores, comentarios y analítica. No se indexa.
- **RF-41** **Inicio de sesión con usuario y contraseña.** Un único usuario, el titular. **No hay botón de registro** ni forma de crear usuarios desde la interfaz: el usuario inicial se provisiona una sola vez fuera de la aplicación.
- **RF-42** La contraseña viaja cifrada: HTTPS obligatorio, y nunca se registra en logs ni se envía por URL.
- **RF-43** La contraseña se almacena solo como hash con Argon2id (o bcrypt), salado. En la base de datos no hay contraseña recuperable. **El valor de la contraseña no se escribe en ningún archivo de este repositorio** (ver §8.2).
- **RF-44** El titular puede **cambiar** su contraseña estando autenticado, indicando la actual.
- **RF-45** El titular puede **restablecer** la contraseña por correo: la solicita, recibe un enlace con token de un solo uso y con vencimiento, y define una nueva. El token se invalida al usarse, al vencer o al emitirse uno nuevo. La respuesta es idéntica exista o no la cuenta, para no revelar el correo del administrador.
- **RF-46** Login y restablecimiento tienen límite de intentos por origen y por cuenta, con espera creciente.
- **RF-47** Toda operación de escritura verifica la credencial **en el servidor**. Un visitante no autenticado no puede escribir ni llamando a la API directamente.
- **RF-48** Parámetros de la cuenta y la sesión:
  - Contraseña de **mínimo 16 caracteres**, sin vencimiento: no expira ni obliga a cambiarla cada cierto tiempo.
  - Sesión de **10 horas exactas** desde el inicio de sesión. **No se renueva por actividad**: a las 10 horas se cierra, se esté usando el panel o no, y hay que volver a entrar.
  - Bloqueo temporal tras **5 intentos fallidos** desde el mismo origen, con espera creciente. Valor por defecto propuesto; dilo si lo quieres distinto.
  - Token de restablecimiento válido **30 minutos**, de un solo uso. Valor por defecto propuesto.
- **RF-49** **Envío de correo: SMTP de Gmail con contraseña de aplicación.** El sistema envía por `smtp.gmail.com` autenticándose con una contraseña de aplicación generada en la cuenta de Google del titular, que vive solo como variable de entorno. Cubre los dos únicos correos que el sitio manda: el enlace de restablecimiento y los mensajes del formulario de contacto.
  - Por qué basta: el restablecimiento solo se envía **a una dirección, la del propio titular**, y el formulario también. No hay envío masivo, así que el límite de Gmail (unos 500 correos al día) sobra. No hace falta dominio propio, ni proveedor de pago, ni configurar SPF o DKIM: Gmail firma sus propios correos.
  - **Quién envía:** la cuenta pública (`javidatastudio@gmail.com`). La contraseña de aplicación se genera ahí, no en la cuenta de administrador. Si esa clave se filtrara, permitiría enviar correo en nombre del titular, pero no leer su correo ni tocar la cuenta que controla el panel. El enlace de restablecimiento sale de la pública y **llega** a la de administrador.
  - **Verificado:** Vercel bloquea únicamente el puerto 25; el 587 con STARTTLS está abierto. Dos condiciones de implementación: el envío **se espera antes de devolver la respuesta HTTP** — una función serverless pausa el trabajo pendiente al responder, así que un envío no esperado se pierde en silencio — y la función **nunca se mueve al runtime Edge**, que no tiene sockets TCP. Ver `viabilidad-tecnica.md`, punto 3.
  - Requisito previo: verificación en dos pasos activada en la cuenta de Google que envía, sin la cual Google no permite crear contraseñas de aplicación.
  - Variables de entorno: `SMTP_HOST` (`smtp.gmail.com`), `SMTP_PORT` (`587` con STARTTLS), `SMTP_USER`, `SMTP_PASSWORD` (la contraseña de aplicación), `MAIL_TO_CONTACT` y `MAIL_TO_ADMIN`.
  - La contraseña de aplicación es revocable por separado y no da acceso a la cuenta de Google desde el navegador. Si se filtra, se revoca sin cambiar la contraseña de Google.
  - Límite conocido: si algún día el sitio necesitara enviar correo a terceros (notificaciones, boletines), esto no sirve y habría que pasar a un proveedor transaccional. No está en el alcance.

### 5.9 Panel de analítica

- **RF-50** El panel incluye una vista de **interacción histórica** del portafolio: la serie en el tiempo, no una foto del momento.
- **RF-51** Filtra por rango de fechas, con presets (últimos 7 días, 30 días, 6 meses, 12 meses, todo) y rango personalizado.
- **RF-52** La analítica es solo para el titular autenticado; no se expone públicamente.
- **RF-53** **La analítica es agregada y anónima.** No se guarda IP, ni user agent, ni cookie de identificación, ni huella del dispositivo. Como consecuencia, el panel cuenta **eventos, no personas**: no habrá "visitantes únicos" ni sesiones, y las cifras son aproximadas. Es el costo de no guardar datos de los visitantes, y es un intercambio aceptado.
- **RF-54** **Registro propio, en una tabla de la base de datos del proyecto.** No se usa una herramienta externa: el requisito es histórico completo dentro del propio panel, y los planes gratuitos de las herramientas de analítica recortan justo eso, la retención. Además evita una dependencia y un tercero más en la política de datos.
- **RF-55** **Granularidad: por hora.** Cada evento se agrega a su hora; el contador de esa combinación sube en uno. No se guarda el minuto ni el segundo, que no aportan nada y acercarían el registro a poder seguir a una persona. Para los rangos del panel (hasta 12 meses) la hora da detalle de sobra y el volumen se mantiene mínimo.
- **RF-56** **Catálogo de eventos.** Cada uno registra tipo, objetivo, ruta, idioma y tema. Propuesta inicial, ordenada por lo que de verdad dice algo en un portafolio que busca entrevistas:

  | Evento               | Objetivo que acompaña                           | Qué te dice                                                              |
  | -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
  | `cv_download`        | `es` \| `en`                                    | **La señal más fuerte de todas.** Quien descarga tu CV está evaluándote. |
  | `contact_click`      | `email` \| `whatsapp` \| `linkedin` \| `github` | Intención de contacto y por qué canal prefieren escribirte.              |
  | `contact_submit`     | —                                               | El objetivo final del sitio.                                             |
  | `project_link_click` | `<slug>:repo` \| `<slug>:demo`                  | Que alguien salga a tu repositorio vale más que que mire la tarjeta.     |
  | `project_view`       | `<slug>`                                        | Qué proyecto atrae. Te dice cuál poner primero.                          |
  | `post_view`          | `<slug>`                                        | Qué artículo funciona, y si el blog trae gente.                          |
  | `page_view`          | ruta                                            | Base de todo: qué secciones se visitan y cuáles nadie abre.              |
  | `vcard_download`     | —                                               | Te guardaron el contacto desde el móvil.                                 |
  | `claude_click`       | —                                               | Si el botón se usa o es adorno.                                          |
  | `filter_use`         | `projects` \| `timeline`                        | Si el buscador y los filtros sirven o sobran.                            |
  | `theme_toggle`       | `light` \| `dark`                               | Si el modo oscuro se usa.                                                |
  | `language_switch`    | `es` \| `en`                                    | Si el español se pide tanto como para justificar traducir todo.          |

  Cuatro de estos — `cv_download`, `contact_click`, `contact_submit` y `project_link_click` — son eventos de intención: el panel los muestra destacados, por encima del resto del tráfico. El catálogo es revisable: quitar o añadir uno es una fila en esta tabla y una llamada más en el código.

## 6. Modelo de datos (preliminar)

El contenido estático (home, experiencia, contacto, política) vive en el código. Solo lo que necesita CRUD o historial va a base de datos:

- **admin_user**: id, usuario, correo, hash de contraseña, último acceso, intentos fallidos, timestamps. Una sola fila.
- **password_reset_token**: id, admin_user_id, hash del token, vencimiento, usado_en.
- **project**: id, slug_es, slug_en, título ES/EN, resumen ES/EN, url_repo, url_produccion, etiquetas[], fecha, readme_cache, readme_fetched_at, destacado, orden, estado (borrador/publicado), timestamps.
- **post**: id, slug_es, slug_en, título ES/EN, cuerpo Markdown ES/EN, imagen_portada (opcional), estado (borrador/publicado), fecha de publicación, timestamps.
- **comment**: id, tipo_destino (`post` | `project`), id_destino, nombre (opcional), cuerpo, estado (pendiente/aprobado/rechazado), fecha. Sin IP ni user agent. Una sola tabla para los dos tipos de contenido: el destino lo definen las dos columnas, no dos tablas paralelas.
- **rate_limit**: clave (hash con sal del origen + acción), contador, inicio de ventana. Se purga al expirar.
- **event**: `hora` (marca de tiempo truncada a la hora), `tipo`, `objetivo`, `ruta`, `idioma`, `tema`, `conteo`. Clave única sobre las seis primeras columnas: cada combinación es una fila y las repeticiones suman al contador, no crean filas nuevas. Sin identificadores de visitante.
- Los mensajes del formulario de contacto **no se persisten**: van por correo (RF-35).

## 7. Arquitectura y stack

**Decidido:**

- **Frontend: Astro** con islas interactivas, Tailwind para estilos y tokens de color centralizados.
- **Backend: FastAPI** (Python) como **única puerta de escritura**. El frontend nunca habla con Supabase.
- **Base de datos: Supabase** (usuario admin, proyectos, artículos, comentarios, límites de tasa, eventos).
- **Despliegue: Vercel, plan gratuito**, un solo proyecto, monorepo.
- **Repositorio: monorepo** con el sitio y la API juntos (`web/` y `api/`).
- RLS en Supabase con denegación por defecto: lectura pública solo de proyectos publicados, artículos publicados y comentarios aprobados; todo lo demás, solo con credencial de servidor.
- SEO: sitemap con las dos variantes de idioma, `hreflang`, `x-default`, imágenes Open Graph.
- Pruebas: todas las funciones CRUD (proyectos, artículos, borradores, comentarios), los dos formularios públicos, el flujo de autenticación, el renderizado y saneado de Markdown, y la lógica de filtros.

**Por qué Astro** (simple de operar, con margen para lo dinámico, y el mejor rendimiento):

- Envía **cero JavaScript por defecto**. El home, la experiencia, la política y los artículos son HTML y CSS; un sitio así carga rápido sin tener que optimizar nada después.
- Las **islas** permiten meter JavaScript solo donde hace falta: los filtros de la línea de tiempo, el buscador de proyectos, el editor con previsualización, las gráficas de analítica. Cada isla carga su JS de forma independiente, así que el panel pesado no afecta al home.
- **i18n con prefijo de ruta y slugs traducidos** es una característica nativa, no un añadido. Es exactamente lo que decidimos en §4.
- **Markdown y GFM de primera clase**, con resaltado de sintaxis incluido, que es justo lo que pide RF-16.
- **Transiciones entre páginas** nativas si algún día se quieren, sin librerías. Esta versión no las usa.
- Tiene **adaptador oficial de Vercel**: las páginas públicas se pueden servir estáticas o renderizadas en servidor, y el panel autenticado se sirve en servidor en la misma aplicación.
- La alternativa realista era Next.js: más potencia dinámica, pero más JavaScript de base, más conceptos para operar y peor rendimiento por defecto en un sitio que es 80% contenido. Para lo que definimos, Astro gana.

**Cómo encaja todo en Vercel gratis** (respuesta a P-28):

- **Un solo proyecto de Vercel** sobre el monorepo, y esto no es una preferencia sino un requisito de seguridad: la cookie de sesión es `SameSite=Strict`, así que frontend y API tienen que compartir origen. Dos proyectos en dominios distintos convertirían esa cookie en una de terceros y el panel no podría autenticarse. Si la combinación de Astro y funciones Python en un mismo proyecto no funcionara, el plan B es dos proyectos con una reescritura que haga de proxy de `/api/*`, de modo que el navegador siga viendo un solo origen. Ver `viabilidad-tecnica.md`, punto 1.
- **Prueba de despliegue antes que nada.** La primera tarea de la feature 01 es desplegar un Astro vacío más un `api/index.py` que responda, y confirmar que ambos contestan en el mismo dominio. Si falla, se aplica el plan B antes de escribir una línea de autenticación.
- **Tarea programada diaria para mantener despierta la base de datos.** Supabase pausa los proyectos gratuitos tras una semana sin actividad, y un portafolio nuevo pasa semanas sin visitas. Una tarea de Vercel una vez al día que haga una consulta trivial lo evita. Entra en la feature 01 o, a más tardar, en la 03.
- FastAPI corre como **función serverless de Python** en `api/`, con el app ASGI expuesto en un único punto de entrada y las rutas enrutadas por configuración. No hace falta un servidor aparte ni hosting pagado.
- Consecuencias de serverless que hay que respetar en el diseño:
  - **Sin estado en memoria.** El límite de tasa y la caché del README no pueden vivir en variables de proceso: van a Supabase (tablas `rate_limit`, `readme_cache`).
  - **Arranque en frío.** La primera petición al panel tras un rato de inactividad tarda más. Aceptable en un panel de uso personal; el sitio público no lo sufre porque es estático.
  - **Hash lento a propósito.** Argon2id consume tiempo y memoria por diseño; hay que calibrar sus parámetros para que entre en los límites de la función y no agote el tiempo de ejecución.
  - El plan gratuito de Vercel es para uso **no comercial**; un portafolio personal lo es.

**Qué se renderiza dónde.** Decidido ahora, no sobre la marcha, porque cambiar una ruta de estática a servidor más adelante altera su caché, sus cabeceras y sus números de rendimiento.

| Rutas                                                                            | Modo                                                                     | Por qué                                                                                                                      |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Home, experiencia, contacto, política de datos, 404, `sitemap.xml`, `robots.txt` | **Estáticas**, generadas en el build                                     | Su contenido vive en el código y solo cambia con un commit. Son las que tienen que volar y las que ve primero un reclutador. |
| Catálogo y ficha de proyectos, índice y artículo del blog                        | **Servidor, con caché de CDN** (60 s, más revalidación en segundo plano) | Su contenido vive en la base de datos y tiene que reflejar lo que publicas desde el panel sin volver a desplegar.            |
| Panel `/admin/*` y todos los endpoints de la API                                 | **Servidor, sin caché** (`no-store`)                                     | Son privados o tienen efectos. Nada de esto puede quedar guardado en un intermediario.                                       |

Notas que evitan confusiones más adelante:

- **Por qué el blog no es estático:** publicar desde el panel exigiría volver a desplegar el sitio, y el panel existe justamente para no tener que hacerlo. La alternativa elegante sería regenerar solo esa página al publicar, pero es más maquinaria de la que justifica esperar 60 segundos.
- **La caché del CDN funciona porque todas las páginas públicas son idénticas para todo el mundo:** el idioma va en la URL y el tema se resuelve en el navegador. Un solo renderizado sirve a todos los visitantes, así que las invocaciones y las lecturas de base de datos se mantienen bajas incluso con un pico de tráfico.
- **Costo asumido:** un comentario recién aprobado o un artículo recién publicado pueden tardar hasta un minuto en aparecer. Es el único precio.
- **Son dos cachés distintas y no hay que mezclarlas:** la del README (RF-17, en la base de datos, 1 hora) y la de la página (CDN, 60 s). El botón de forzar actualización del README debe invalidar también la de la página; si no, el titular refresca y sigue viendo lo mismo durante un minuto, y pensará que el botón no sirve.
- Las páginas estáticas aplican el tema con un script en línea que corre antes del primer pintado, que es lo que evita el destello de RF-02.

**Rendimiento (lo que hay que optimizar para que fluya bien):**

El sitio nace rápido por ser mayormente estático, pero eso se pierde con descuidos típicos. Lo que sí hay que hacer:

- **Imágenes.** Son el peso real de un portafolio con fotos. Formatos modernos (AVIF/WebP) con respaldo, varios tamaños servidos según el ancho de pantalla, dimensiones declaradas para que la página no salte al cargar, y carga diferida en todo lo que no se ve al entrar. Las fotos del hero sí se cargan con prioridad.
- **Tipografías.** Como mucho dos familias, con subconjunto de caracteres, servidas desde el propio dominio y con `font-display: swap`. Una fuente mal servida bloquea el texto y arruina la primera impresión.
- **JavaScript.** Islas solo donde hay interacción real. El panel y sus gráficas no deben cargar nada en las páginas públicas.
- **Navegación.** Precarga de los enlaces visibles para que moverse entre secciones sea instantáneo, y transiciones de página nativas.
- **Caché.** Cabeceras largas para los archivos con huella en el nombre; los PDFs del CV con caché corta, porque se reemplazan.
- **Presupuesto de rendimiento** como criterio de aceptación de la feature 01: LCP por debajo de 2.5s y CLS por debajo de 0.1 en móvil, y menos de 100 KB de JavaScript en las páginas públicas. Si un cambio rompe el presupuesto, se revisa antes de seguir.

**Pendientes de arquitectura:** ninguno.

## 8. Seguridad

Apartado propio por decisión del titular. Un sitio con un único administrador, formularios públicos y una base de datos es un objetivo pequeño pero real: el login será sondeado por bots a los pocos días de estar en línea.

### 8.1 Requisitos de seguridad

- **RS-01** HTTPS en todo el sitio, con redirección desde HTTP y HSTS. El TLD `.dev` ya lo exige a nivel de navegador.
- **RS-02** El frontend **nunca** se comunica con Supabase. Solo el backend tiene credenciales de base de datos. Así, ninguna clave de datos viaja al navegador.
- **RS-03** Las claves de servicio (`service_role` de Supabase, clave de firma de sesión, credenciales de correo) viven **solo** en variables de entorno del servidor. Nunca en el código, nunca en el bundle del cliente, nunca en un archivo versionado.
- **RS-04** Ninguna variable con prefijo público (`PUBLIC_*` en Astro) contiene un secreto. Ese prefijo hace que el valor se incruste en el JavaScript que llega al navegador: es la forma más común de filtrar una clave.
- **RS-05** Sesión en cookie `HttpOnly`, `Secure`, `SameSite=Strict`, con vencimiento. Sin token en `localStorage`, que es legible por cualquier script.
- **RS-06** Validación de toda entrada en el servidor, incluso si el formulario ya validó en el cliente. Longitudes máximas en cada campo.
- **RS-07** Límite de tasa en login, restablecimiento, comentarios y formulario de contacto. Como no se guarda la IP (RF-31), la clave del límite es un **hash con sal** del origen, con la sal en variable de entorno, y el registro se purga al expirar la ventana. El hash no permite reconstruir la IP.
- **RS-08** Mensajes de error genéricos en login y restablecimiento: nunca "ese usuario no existe" ni "contraseña incorrecta" por separado, para no permitir enumeración de cuentas.
- **RS-09** Cabeceras de seguridad: `Content-Security-Policy` restrictiva, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, y `frame-ancestors 'none'`.
- **RS-10** CORS limitado al dominio propio. La API no responde a orígenes arbitrarios.
- **RS-11** Markdown y comentarios: el HTML del README se elimina (RF-16) y el cuerpo de los comentarios se escapa (RF-28). Son los dos únicos puntos donde entra contenido ajeno al sitio.
- **RS-12** Los logs no contienen contraseñas, tokens, cookies ni cuerpos de petición de autenticación. Los errores que ve el visitante no incluyen traza ni detalle interno.
- **RS-13** Dependencias con lockfile y actualizaciones de seguridad automáticas.
- **RS-14** Respaldos de la base de datos y verificación de que se pueden restaurar. Un portafolio con blog y comentarios tiene contenido que no está en el repositorio.
- **RS-15** El provisionamiento del usuario administrador no deja la contraseña en ningún archivo: se pasa por variable de entorno al ejecutarse una vez, o se escribe el hash directamente.
- **RS-16** **El repositorio es público, así que ninguna clave puede vivir en las fuentes ni en el historial.** Medidas concretas:
  - `.env` y `.env.*` nunca se versionan (el `.gitignore` ya lo cubre); `.env.example` lleva solo nombres de variables, sin valores.
  - Ningún secreto en código, ni en comentarios, ni en datos de semilla, ni en archivos de prueba.
  - Escaneo automático de secretos antes de cada commit y en CI, para que un descuido no llegue a GitHub. GitHub añade su propio escaneo y bloqueo de envío en repositorios públicos, que conviene dejar activo.
  - Si alguna vez se publica un secreto por error: **rotarlo en el proveedor**, no basta con borrar el commit. Lo que estuvo un minuto en un repositorio público se considera comprometido.
  - La ruta del panel y la estructura de la API son públicas por diseño. La protección es la credencial verificada en el servidor (RF-47), nunca el desconocimiento.

### 8.2 Manejo de secretos (respuesta a P-33)

No hace falta pagar nada ni montar infraestructura. Lo seguro y estándar para este proyecto son tres capas:

1. **Variables de entorno de Vercel**, separadas por entorno (Production, Preview, Development). Se cifran en reposo, solo se inyectan en el proceso del servidor, y Vercel no las vuelve a mostrar completas una vez guardadas. Ahí van: URL y `service_role` de Supabase, clave de firma de sesión, sal del límite de tasa, credenciales del proveedor de correo, correo de destino del formulario.
2. **En tu máquina, un archivo `.env` local** que nunca se versiona. El `.gitignore` del repo ya ignora `.env` y `.env.*`, y permite `.env.example`. En `.env.example` van los **nombres** de las variables con valores de ejemplo vacíos, nunca los reales: sirve de documentación y de lista de verificación al desplegar.
3. **Un gestor de contraseñas** para los secretos que manejas tú como persona: la contraseña del administrador y las credenciales de Supabase y Vercel. Ya usas uno (generaste la contraseña con Kaspersky); ese es el lugar correcto, no un archivo del proyecto.

**Sobre la contraseña que escribiste en el chat:** no la voy a guardar en el repositorio, y te recomiendo **no usarla**. Una contraseña deja de ser secreta en cuanto viaja por un canal que no es el gestor de contraseñas: quedó en el historial de esta conversación. Genera otra en Kaspersky cuando llegue el momento de provisionar el usuario, úsala solo desde el gestor, y que nunca pase por un chat, un commit ni un archivo de notas. El procedimiento de RF-43 y RS-15 ya está escrito para que el valor nunca toque el repositorio.

Rotación: si alguna clave se filtra, se regenera en el proveedor (Supabase, el servicio de correo) y se actualiza en Vercel. Ninguna clave debe ser irremplazable.

**Token de GitHub.** Tanto el repositorio del portafolio como los de los proyectos son públicos (`[P-51]` resuelto), así que leer sus README no exige credencial. Aun así conviene un **token de solo lectura, de alcance mínimo**, guardado como variable de entorno: sin token, GitHub permite 60 peticiones por hora por dirección IP, un límite que una función serverless compartida agota fácil; con token sube a 5.000. Si algún día un proyecto vive en un repositorio privado, el token pasa a ser obligatorio.

**Correos del proyecto (§8.3, `[P-49]` resuelto).** Sin dominio propio, la separación se hace con **dos cuentas de Gmail distintas**:

- **`javidatastudio@gmail.com`** — pública. Va en el sitio, en la vCard y en el CV. Es el destino del formulario de contacto.
- **Una segunda cuenta de Gmail, nunca publicada en ninguna parte** — es el correo del usuario administrador y el destino del enlace de restablecimiento. No debe ser derivable de la pública: nada de `javidatastudio+admin@gmail.com` ni variantes con puntos, porque se adivinan en un segundo y llegan al mismo buzón.

Las dos con verificación en dos pasos. Con esto, quien recoge direcciones de la web se lleva la pública y no la que controla el portafolio. La cuenta de Google del administrador pasa a ser parte del perímetro de seguridad del sitio: si cae esa cuenta, cae el panel.

### 8.3 Datos sensibles: qué conviene quitar o cambiar

Evaluación de lo que el proyecto expondría tal como está definido:

| Dato                                              | Riesgo                                                                                                                                                                                                                                                     | Recomendación                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Correo del administrador = correo público**     | **El más importante.** Publicar una dirección y usarla además como destino del restablecimiento de contraseña le entrega al atacante la mitad del problema: ya sabe a qué cuenta atacar. Si ese buzón cae, cae el portafolio.                              | **Decidido:** `javidatastudio@gmail.com` como pública, y una **segunda cuenta de Gmail nunca publicada** para el administrador y el restablecimiento. Verificación en dos pasos en ambas. No usar alias derivables (`+admin`, puntos): van al mismo buzón y se adivinan.                                                                                                                                                                              |
| **Teléfono +57 315 851 5323 publicado**           | Una vez en la web, lo recogen los robots de scraping: spam, llamadas automáticas, estafas por WhatsApp, y es un dato útil para suplantación o cambio de SIM. En el CV se lo das a quien tú eliges; en la web se lo das a todos.                            | **Decidido: el número se publica**, con el riesgo asumido a conciencia, porque hoy no hay otro número que poner. Mitigación posible más adelante, sin rehacer nada: conseguir una línea aparte para lo profesional y cambiar la variable. Si empieza a llegar spam, esa es la salida.                                                                                                                                                                 |
| **Nombre legal completo**                         | "Javi Johan Rodríguez Giraldo" en la web amplía la superficie para suplantación. El reclutador no lo necesita en la página.                                                                                                                                | Ya aplicado: el sitio usa "Javi Giraldo"; el nombre completo queda solo dentro del PDF del CV.                                                                                                                                                                                                                                                                                                                                                        |
| **Metadatos de los PDFs del CV**                  | Un PDF arrastra autor, software, y a veces rutas de archivos de tu equipo. Son archivos públicos y descargables.                                                                                                                                           | Limpiar metadatos de los dos PDFs antes de versionarlos en `public/cv/`.                                                                                                                                                                                                                                                                                                                                                                              |
| **Detalles internos de BCD Travel**               | El CV describe sistemas de tu empleador. Es normal y aceptable a ese nivel. Lo que no debe aparecer nunca, sobre todo en el blog, son nombres de servidores, cadenas de conexión, nombres de clientes, esquemas reales o fragmentos de código del trabajo. | Regla de contenido para el blog: nada que identifique infraestructura, clientes o código de un empleador. Los ejemplos técnicos se reescriben con datos ficticios.                                                                                                                                                                                                                                                                                    |
| **Datos de visitantes (IP, user agent, cookies)** | Guardarlos obliga a política de datos más amplia, aumenta lo que se puede filtrar y no aporta a tu objetivo.                                                                                                                                               | Ya aplicado: no se guardan (RF-31, RF-54). El límite de tasa usa hash con sal (RS-07).                                                                                                                                                                                                                                                                                                                                                                |
| **Mensajes del formulario**                       | Si se guardaran en la base de datos, serías responsable de custodiarlos.                                                                                                                                                                                   | Ya aplicado: van por correo y no se persisten (RF-35).                                                                                                                                                                                                                                                                                                                                                                                                |
| **Repositorio público**                           | Si el repo es público, se ve la estructura, la ruta del panel y la lógica. No es un problema si la seguridad no depende de ocultarla, pero un `.env` filtrado ahí sí es grave.                                                                             | **Decidido: el repositorio es público** (revisado, antes se había decidido privado). El código es parte del portafolio y un reclutador puede leerlo. La condición es que la seguridad no dependa de ocultar nada: ningún secreto en las fuentes ni en el historial (RS-03, RS-04, RS-16), y la ruta del panel protegida por credencial, no por ser desconocida. Como el repo nace público desde el primer commit, no hay historial viejo que auditar. |

## 9. Diseño visual y activos

### 9.1 Tokens visuales

Paleta, tipografía, espaciado, radios y sombras están **decididos** y documentados en [`design-tokens.md`](design-tokens.md), que es la fuente única de esos valores: paleta de azul petróleo y verdes en tema claro y oscuro, Inter Display para titulares e Inter para texto, escala de espaciado de 4px.

La composición, el ritmo y el tratamiento de las fotografías se trabajan en la feature 07; los valores de arriba ya no se discuten allí, solo se aplican.

### 9.2 Fotografías

Hay cuatro fotografías de estudio del titular, todas de medio cuerpo o cuerpo entero, traje azul oscuro sobre fondo blanco. Se usan **dos**:

| Sección      | Foto                       | Por qué                                                                                                                                                                              |
| ------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Home**     | Brazos cruzados, de frente | Es la más sobria y la que mejor envejece. Mirada directa, postura estable, y la figura queda a la derecha del encuadre, así que el titular cabe a la izquierda sin recortar a nadie. |
| **Contacto** | Señalando a la cámara      | El gesto apunta a quien mira y empuja a escribir, que es justo lo que esa sección pide. Encuadre cuadrado, cómodo junto al formulario.                                               |

Las otras dos quedan de reserva: la del gesto de palma abierta sirve como alternativa del home si la de brazos cruzados resulta demasiado cerrada, y la del guiño en formato muy vertical se descarta — proporción 1:2, difícil de encajar, y el tono es más informal de lo que conviene ante un reclutador.

**Tratamiento obligatorio:**

- **Recorte de fondo.** Las cuatro vienen sobre blanco. En tema oscuro, un rectángulo blanco brilla y rompe la página. Se recortan con transparencia y la silueta se apoya sobre el color de fondo del sitio.
- **Cuidado con el traje sobre el azul petróleo.** El traje azul muy oscuro queda cerca de `brand-deep`. Si la silueta se coloca sobre ese fondo, desaparece. Va sobre `surface` o `surface-raised`, o con una separación explícita: halo, borde, o un bloque de color detrás.
- Varios tamaños para servir según el ancho de pantalla, con dimensiones declaradas para que la página no salte al cargar. La del home carga con prioridad; la de contacto, diferida.
- Texto alternativo descriptivo en las dos, en los dos idiomas.

**Dónde viven los archivos:**

- `src/assets/images/profile/` — las fotografías ya procesadas. Van ahí, y no en `public/`, porque Astro solo optimiza y genera los tamaños responsive de lo que pasa por su canal de imágenes.
- `public/` — solo lo que debe servirse tal cual y con URL estable: `public/cv/` para los PDFs, favicon, `robots.txt`, imágenes de Open Graph.
- Los originales sin procesar **no se versionan**: `images_results/` se queda fuera del repositorio. Son archivos pesados que no aportan al despliegue, y el repositorio es público.

### 9.3 Accesibilidad

Alcance acordado, deliberadamente acotado:

- **Navegación completa por teclado.** Todo lo que se hace con el ratón se hace con el teclado: menú, selector de idioma, botón de tema, filtros, formularios, panel.
- **Foco visible.** Va incluido en lo anterior y no es negociable: navegar por teclado sin ver dónde estás no es navegar, es adivinar. Es el anillo de foco del navegador bien tratado, no una ayuda visual añadida.
- **Textos alternativos** en toda imagen con contenido, en los dos idiomas. Las decorativas se marcan como tales para que un lector de pantalla las salte.
- El contraste viene resuelto por los tokens: respetando las reglas de `design-tokens.md` — qué color nunca es texto, cuál no delimita un control, qué estados necesitan ícono además de color — deja de ser un tema aparte.
- **Fuera de alcance por ahora:** barra de accesibilidad, alternativa de alto contraste, enlaces de salto visibles y cualquier otra ayuda visual añadida.

## 10. Restricciones de proceso

- Especificación primero: nada de código hasta que constitución y specs estén aprobadas.
- Textos del sitio (copy en ES y EN) pasan por la skill `humanizer`.
- Diseño visual con la skill **Impeccable** (`pbakaus/impeccable`, Apache-2.0), ya instalada. Sustituye a `frontend-design`, que queda retirada del proyecto: Impeccable nació de esa misma skill y la amplía, así que usar las dos a la vez significa dos conjuntos de criterios estéticos compitiendo sobre el mismo código.
- Implementación con la skill `ponytail`: código modular, funcional, simple y fácil de mantener.
- Commits con el formato ya usado en el repo (`vX.Y.Z-YYYY-MM-DD-tipo: descripción`).
- **Ramas: convención de Spec Kit.** `main` es producción —Vercel despliega desde ahí, así que integrar es publicar— y solo recibe lo que cumple la Definición de hecho de la constitución.
  - Una rama por feature, con el nombre de su carpeta de spec (`001-sitio-base`), creada al especificarla. Spec, plan, tareas y código viajan en ella y se integran juntos.
  - Los documentos de alcance del proyecto —constitución, brief, tokens, viabilidad, política— no pertenecen a ninguna feature y viven en `main`.
  - Antes de integrar, la rama se revisa en su despliegue de vista previa.
  - **Un solo entorno de datos**: un proyecto de Supabase, el de producción. Sin base de pruebas ni pila local; las vistas previa comparten esa base y la verificación se hace sobre el sitio desplegado. A cambio, tres reglas: las pruebas automáticas no son destructivas y limpian lo que crean; el contenido creado al probar nace como borrador y se elimina al terminar; y las migraciones se aplican al integrar a `main`, nunca desde una rama en curso.

## 11. Criterios de aceptación de la primera versión

1. Las ocho secciones públicas existen en los dos idiomas con slugs traducidos, cargan con contenido real y son enlazables de forma independiente.
2. El cambio de tema y de idioma funciona en todas las páginas y persiste; un visitante con navegador en español llega al español, cualquier otro al inglés.
3. La línea de tiempo filtra sin recargar por tipo, años, tecnología y empresa, y los dos PDFs del CV se descargan con la fecha del día en el nombre del archivo.
4. El catálogo filtra por nombre, etiqueta y fecha; cada ficha muestra el README renderizado sin HTML; si GitHub no responde, se muestra la última copia en caché; el botón de forzar actualización la refresca.
5. El titular inicia sesión con usuario y contraseña sobre HTTPS, cambia su contraseña, y recibe el enlace de restablecimiento en su cuenta de administrador, enviado por SMTP de Gmail.
6. No existe ninguna forma de crear un segundo usuario desde la interfaz.
7. Un visitante no autenticado no puede crear, editar ni borrar nada, ni por interfaz ni llamando a la API directamente.
8. Publicar un artículo exige los dos idiomas; guardarlo como borrador no, y la lista de borradores está disponible en el panel.
9. Un comentario enviado desde un artículo y otro desde una ficha de proyecto llegan a la misma cola de moderación, no aparecen hasta que el titular los aprueba, y en la base de datos no hay IP ni user agent asociado.
10. El formulario de contacto no se envía sin aceptar la política, el enlace lleva a la página de política, y el mensaje llega al correo del titular sin quedar en la base de datos.
11. El panel de analítica muestra la serie histórica y filtra por los presets, incluido "últimos 6 meses".
12. El botón de Claude abre una conversación con el mensaje prellenado.
13. La opción de guardar contacto aparece en móvil y no en escritorio.
14. Cambiar los valores del archivo de tokens cambia los colores de todo el sitio sin tocar componentes, y el sitio completo se puede recorrer y usar solo con el teclado, con el foco siempre visible.
15. No hay ningún secreto en el repositorio público, en su historial, ni en el JavaScript que llega al navegador, y el escaneo automático de secretos está activo.
16. El sitio está desplegado en el subdominio de Vercel, funciona en móvil, tablet y escritorio, y todo corre sin costo: plan gratuito de Vercel, Supabase gratuito, Gmail, y sin dominio propio.
17. La tarea programada diaria corre y deja constancia de haber consultado la base de datos, de modo que Supabase nunca llega a los siete días de inactividad.
18. Las páginas estáticas se sirven desde el build y las dinámicas desde la caché del CDN; `/admin` y la API responden con `no-store`.

## 12. División propuesta en features para SDD

1. **`01-sitio-base`** — **prueba de despliegue de Astro + función Python en un mismo proyecto, primero que todo**; luego monorepo, Astro + Tailwind, enrutado bilingüe con slugs traducidos, archivo de tokens de `design-tokens.md`, modo oscuro, navegación por teclado, responsive, tabla de rutas estáticas contra renderizadas en servidor, creación del proyecto de base de datos vacío, tarea programada que lo mantiene despierto y avisa por correo si falla —lo que trae aquí la configuración del envío de correo—, SEO con el sitio bloqueado a buscadores hasta la feature 02, y despliegue en Vercel.
2. **`02-contenido-estatico`** — home, experiencia con línea de tiempo filtrable, contacto, política de datos, descarga de CV, vCard, botón de Claude. Al tener contenido real, se levanta el bloqueo de indexación.
3. **`03-admin-y-autenticacion`** — FastAPI en Vercel, login, hash, cambio de contraseña, sesión de 10 horas, restablecimiento por correo —el envío ya quedó configurado en la feature 01—, primer esquema de la base de datos, límites de tasa, secretos, estructura del panel. **Antes que cualquier CRUD.**
4. **`04-proyectos`** — tablas de proyectos, catálogo, buscador, ficha, README con caché y botón de refresco, CRUD bilingüe con borradores.
5. **`05-blog-y-comentarios`** — artículos bilingües, plantilla, editor con previsualización, borradores, comentarios con moderación previa en artículos y en fichas de proyecto.
6. **`06-analitica`** — registro agregado de eventos por hora y panel histórico con filtros.
7. **`07-diseno-visual`** — composición, ritmo y tratamiento de las fotografías, sobre los tokens ya fijados.

**División y orden aprobados por el titular el 2026-11-05.** Lo único que no se puede reordenar es que la feature 03 vaya antes que la 04 y la 05: proyectos y blog dependen de la autenticación.

## 13. Notas de contexto

- `docs/historico/research/README.md` referencia rutas `specs/02-architecture/` y `specs/04-content/` que todavía no existen. Si se adopta la división de la sección 12, esas referencias deben actualizarse.
- La constitución anterior se eliminó a propósito; se reescribe desde cero antes de la primera spec.
- La investigación recomienda evitar Vercel en plan gratuito si en el futuro se monetiza el sitio, y propone S3 + CloudFront como proyecto de AWS. Queda registrado; la decisión del titular es Vercel gratuito, y el sitio no es comercial.
- Los CVs viven hoy en `G:\My Drive\Documentos\CV\`. Para que RF-12 funcione tienen que estar versionados en `public/cv/`, con metadatos limpios.
- El `.gitignore` del repo ya ignora `.env` y `.env.*` y permite `.env.example`, que es lo que RS-03 necesita.
- `docs/historico/viabilidad-tecnica.md` recoge la revisión del stack hecha antes de la primera spec: qué se verificó contra documentación oficial, qué queda por comprobar con una prueba de despliegue y qué sería caro de cambiar más adelante.
- `package.json` fija `"node": "26.x"`, la LTS activa desde el 28 de octubre de 2026 y la versión por defecto de Vercel. Node 24 pasó a mantenimiento ese mismo mes.

# Política de tratamiento de datos — borrador

> **Aprobado como base por el titular el 2026-11-04.** Se publica con estos contenidos; quedan por sustituir los `‹pendiente›`.
>
> **Borrador para revisión del titular.** No es asesoría legal. Está redactado para reflejar exactamente lo que el sistema definido en las specs de `specs/` hace con los datos, ni más ni menos. Si el comportamiento del sitio cambia, esta política cambia con él.
>
> Destino: `/es/politica-de-datos` y, traducida, `/en/data-policy` (RF-37).
> Marco de referencia: Ley 1581 de 2012 y Decreto 1377 de 2013 de Colombia (habeas data).
>
> **Decisiones que faltan para cerrarlo:** si el teléfono se publica (`[P-50]`) y la fecha de vigencia. Están marcadas abajo como `‹pendiente›`.
> El correo y el envío ya están resueltos: `javidatastudio@gmail.com`, enviado por SMTP de Gmail.

---

## Responsable

Este sitio web es un portafolio personal de **Javi Giraldo**, persona natural, con domicilio en Bogotá, Colombia.
Correo de contacto para asuntos de datos personales: **javidatastudio@gmail.com**.

## Qué datos se recogen y qué se hace con ellos

### Formulario de contacto

Si decides escribirme por el formulario, recojo lo que escribas en él: tu nombre, tu correo electrónico y tu mensaje.

- **Para qué:** únicamente para leerte y responderte.
- **Dónde quedan:** el mensaje se envía a mi correo personal. **No se almacena en la base de datos de este sitio.** Queda en mi bandeja de entrada, como cualquier correo que me escribas directamente.
- **Cuánto tiempo:** el que permanezca en mi correo. Puedes pedirme que lo elimine.
- **Base del tratamiento:** tu autorización expresa, que das al marcar la casilla de aceptación antes de enviar el formulario.

### Comentarios en artículos y proyectos

Los comentarios son abiertos y no requieren registro, tanto en los artículos del blog como en las fichas de proyecto.

- **Qué se guarda:** el texto de tu comentario, la fecha, y tu nombre **solo si decides escribirlo**. El nombre es opcional; si lo dejas vacío, el comentario se publica como anónimo.
- **Qué NO se guarda:** no se guarda tu dirección IP, ni el tipo de navegador o dispositivo, ni ninguna cookie o identificador que permita reconocerte.
- **Para qué:** publicar el comentario en el artículo correspondiente.
- **Moderación:** todo comentario pasa por mi revisión antes de hacerse visible. Puedo no aprobarlo o eliminarlo después.
- **Cuánto tiempo:** mientras el artículo esté publicado, o hasta que lo elimine.
- **Ten en cuenta:** lo que escribas en un comentario aprobado es público. No incluyas ahí datos personales tuyos o de terceros.

### Medición de uso del sitio

Mido cómo se usa el sitio de forma **agregada y anónima**: cuántas veces se vio una página, cuántas descargas tuvo el CV, en qué idioma, ese tipo de conteo.

- **No se usan cookies de seguimiento**, ni perfiles publicitarios, ni huella digital del dispositivo.
- No se guarda tu IP ni ningún dato que permita identificarte o seguirte entre visitas.
- Como consecuencia, estas cifras cuentan eventos, no personas: no sé quién eres ni si ya habías entrado antes.

### Preferencias de idioma y tema

Tu elección de idioma y de modo claro u oscuro se guarda **en tu propio navegador**, para que el sitio te recuerde cómo lo dejaste. Esa información no se envía a ningún servidor, no viaja a mí y no se comparte con nadie. Si borras los datos de navegación de tu navegador, desaparece.

### Protección contra abuso

Para evitar que robots inunden los formularios de comentarios y contacto, el sistema cuenta cuántos envíos llegan desde un mismo origen en un intervalo corto. Para hacerlo **no guarda tu dirección IP**: guarda un valor derivado de ella mediante una función criptográfica con clave secreta, del que no se puede reconstruir la IP original, y lo borra cuando el intervalo termina.

## Qué no hago con tus datos

- No vendo, alquilo ni cedo datos personales a terceros.
- No envío correos comerciales ni boletines.
- No hago perfilamiento ni decisiones automatizadas sobre ti.
- No pido datos sensibles, y te pido que no los escribas en los formularios.

## Proveedores que intervienen

El sitio funciona sobre servicios de terceros que, en lo que les corresponde, actúan como encargados del tratamiento:

| Proveedor      | Función                                          | Datos que puede procesar                                            |
| -------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| Vercel         | Alojamiento del sitio                            | Datos técnicos de la conexión, en sus propios registros de servidor |
| Supabase       | Base de datos del blog, proyectos y comentarios  | Comentarios y nombre opcional                                       |
| Google (Gmail) | Envío del correo y buzón donde recibo tu mensaje | Tu nombre, correo y mensaje                                         |

Estos proveedores operan servidores fuera de Colombia, por lo que el uso del sitio implica una **transferencia internacional de datos** a los países donde están alojados. Al aceptar esta política autorizas esa transferencia.

## Tus derechos

Como titular de tus datos personales puedes, en cualquier momento y sin costo:

- Conocer qué datos tuyos tengo y cómo los uso.
- Pedir que los actualice o corrija si están desactualizados o son inexactos.
- Pedir que los elimine, incluido un comentario que hayas publicado.
- Revocar la autorización que diste.
- Presentar quejas ante la Superintendencia de Industria y Comercio de Colombia.

Para ejercerlos, escríbeme a **javidatastudio@gmail.com** indicando qué necesitas. Responderé en los plazos que fija la ley colombiana: quince días hábiles para consultas y quince días hábiles para reclamos, prorrogables según el caso.

Dado que casi no guardo información, en la mayoría de los casos lo único que tengo tuyo es un correo en mi bandeja de entrada o un comentario que publicaste.

## Seguridad

El sitio se sirve siempre por conexión cifrada (HTTPS). El acceso de administración está protegido con contraseña almacenada como hash, y toda escritura se verifica en el servidor. Ningún dato se guarda en el navegador de otros visitantes ni se expone públicamente, salvo los comentarios aprobados, que por naturaleza son públicos.

## Menores de edad

Este sitio no está dirigido a menores de edad y no recoge datos de ellos de forma consciente. Si eres menor, no uses los formularios.

## Cambios en esta política

Si cambia lo que el sitio hace con los datos, actualizo esta página y su fecha de vigencia. La versión publicada en esta URL es siempre la vigente.

**Vigente desde:** ‹fecha de publicación›
**Última actualización:** ‹fecha›

---

## Notas de implementación (no van en la página publicada)

- Si el formulario termina enviándose con un proveedor distinto a Gmail, hay que corregir la tabla de proveedores: declarar un encargado que no es el real es justamente lo que una política no debe hacer.
- Cuando se compre un dominio propio (`[P-52]`), hay que actualizar la dirección de contacto en esta página y en el sitio.
- Si en algún momento se decide guardar los mensajes del formulario en la base de datos (`[P-25]`, hoy resuelto como "no persistir"), esta política deja de ser exacta y hay que reescribir la sección del formulario.
- Si se añade analítica con cookies o con IP (`[P-45]`, `[P-46]`), hace falta además un aviso de cookies con consentimiento previo, que hoy no es necesario.
- La versión en inglés no es una traducción literal: debe decir lo mismo con la misma precisión. Se redacta en la feature 02.
- Revisar el teléfono: si se decide no publicarlo (`[P-50]`), no mencionarlo aquí tampoco.

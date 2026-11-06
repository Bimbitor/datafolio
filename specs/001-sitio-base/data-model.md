# Fase 1 — Modelo de datos: Sitio base

**Feature**: `001-sitio-base` | **Fecha**: 2026-11-05

Esta feature apenas tiene datos, y eso es intencional. El esquema de la aplicación nace en la feature 03. Aquí hay una tabla, que existe para la comprobación programada, y dos estructuras en el código que
funcionan como fuente única de verdad.

---

## 1. Tabla `salud`

Única tabla de la base de datos en esta feature. Tiene **una sola fila**, siempre la misma, que la
comprobación programada sobrescribe en cada ejecución. No crece.

| Campo           | Tipo          | Reglas                                                                                             |
| --------------- | ------------- | -------------------------------------------------------------------------------------------------- |
| `id`            | `smallint`    | Clave primaria. Fijo en `1`. Una restricción `CHECK (id = 1)` impide que aparezca una segunda fila |
| `comprobado_en` | `timestamptz` | Momento de la ejecución. Nunca nulo                                                                |
| `resultado`     | `text`        | `correcto` o `fallido`. Nunca nulo                                                                 |
| `detalle`       | `text`        | Causa del fallo cuando `resultado` es `fallido`; nulo cuando es `correcto`                         |

**Por qué una fila y no un historial**: el historial de ejecuciones lo guarda ya la plataforma, por
tarea programada, y duplicarlo aquí sería una tabla que crece sin que nadie la lea. Esta fila existe
para dos cosas: que la escritura cuente como actividad de base de datos, y que el último resultado sea
consultable sin entrar al panel de la plataforma.

**Ciclo de vida**: la fila se crea al aplicar la migración, con `resultado` en `correcto` y la fecha de
creación. A partir de ahí solo se actualiza. No se borra nunca.

**Acceso**: solo el servicio de la API, con la clave de servicio. El sitio no habla con la base de
datos, así que no hay ninguna política de acceso público que escribir. La tabla **no** se expone a
lectura anónima: no contiene nada secreto, pero publicarla sería dar a un robot un indicador gratuito
de la salud del sistema.

---

## 2. Mapa de rutas — `web/src/i18n/rutas.ts`

No es una tabla, es una estructura en el código, y es la fuente de verdad de las dieciocho direcciones
públicas del sitio. Se declara una vez y de ella salen los enlaces, el selector de idioma, las
etiquetas de buscador y el índice del sitio.

| Campo          | Qué es                                           | Reglas                                                                                                                       |
| -------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `clave`        | Identificador interno de la sección              | Único. Nueve en total: `inicio`, `experiencia`, `proyectos`, `proyecto`, `blog`, `articulo`, `contacto`, `politica`, `error` |
| `slug.en`      | Segmento de la dirección en inglés               | Obligatorio. Minúsculas, sin acentos, guiones en lugar de espacios                                                           |
| `slug.es`      | Segmento de la dirección en español              | Obligatorio. Mismas reglas. Puede coincidir con el inglés si la palabra es la misma                                          |
| `enNavegacion` | Si la sección aparece en el menú                 | Las nueve existen; `proyecto`, `articulo` y `error` no se enlazan desde el menú                                              |
| `enIndice`     | Si la sección entra en el índice para buscadores | `error` no entra                                                                                                             |

**Reglas que el código debe hacer cumplir**, porque son los casos en que esta estructura se rompe en
silencio:

1. Toda sección tiene slug en los **dos** idiomas. Un slug vacío es un error de construcción, no una
   página sin traducir.
2. Dos secciones no comparten slug dentro del mismo idioma.
3. Toda sección con `enNavegacion` tiene su etiqueta en los dos idiomas en `textos.ts`.

Estas tres son exactamente lo que cubren las pruebas de Vitest asignadas en la investigación.

---

## 3. Idioma y tema del visitante

No son datos del sistema: viven en el navegador de quien visita y **nunca** se envían ni se almacenan
en el servidor. Se documentan aquí porque tienen reglas de precedencia que hay que respetar igual.

| Dato           | Dónde vive                         | Precedencia                            |
| -------------- | ---------------------------------- | -------------------------------------- |
| Idioma elegido | Almacenamiento local del navegador | Manda sobre la cabecera del navegador  |
| Tema elegido   | Almacenamiento local del navegador | Manda sobre la preferencia del sistema |

**Orden de resolución del idioma** al entrar por la raíz:

1. Elección manual guardada, si existe.
2. Cabecera de idioma del navegador, si pide español.
3. Inglés.

**Orden de resolución del tema**:

1. Elección manual guardada, si existe.
2. Preferencia del sistema.
3. Claro.

**Si el almacenamiento está bloqueado** —navegación privada restringida, permisos denegados— ambas
lecturas fallan sin romper nada y se cae al siguiente nivel de la lista. Ese es el requisito de
degradación, y es la razón por la que todo acceso al almacenamiento va envuelto en `try`/`catch`.

---

## Lo que esta feature NO modela

Se deja constancia para que nadie lo añada "de paso":

- Usuario administrador, sesión, contraseña. → feature 03
- Proyectos, artículos, comentarios, borradores. → features 04 y 05
- Eventos de analítica y su agregación por hora. → feature 06
- Caché de los README de los repositorios. → feature 04
- Límite de tasa y su hash con sal. → feature 03

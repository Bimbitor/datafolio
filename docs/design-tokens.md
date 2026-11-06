# Tokens de diseño

> Fuente única de los valores visuales del portafolio. Resuelve `[P-34]` del brief.
> Estos valores se implementan **una sola vez** en el archivo de tokens del proyecto (RF-04). Ningún componente escribe un color, un tamaño o un radio suelto.
> La dirección visual completa (composición, ritmo, uso de las fotografías) se trabaja en la feature 07 con la skill de diseño.

## Color

Dos temas: claro y oscuro. Todo token existe en los dos. El tema claro es el primario.

| Token            | Claro     | Oscuro    | Para qué                                                                                  |
| ---------------- | --------- | --------- | ----------------------------------------------------------------------------------------- |
| `surface`        | `#ffffff` | `#121e22` | Fondo base de la página. Todo lo demás se mide contra este.                               |
| `surface-raised` | `#f2f3f8` | `#21333a` | Tarjeta de proyecto, tarjeta de artículo, bloque citado, fila alterna de tabla.           |
| `border-subtle`  | `#d9dce6` | `#354a52` | Separador decorativo y borde de tabla. **No sirve para delimitar un control.**            |
| `border-strong`  | `#8e94a4` | `#58707a` | Borde de campo, casilla e interruptor. Cumple 3:1 en los dos temas.                       |
| `text`           | `#0b0e1a` | `#ebf3f4` | Texto principal.                                                                          |
| `text-secondary` | `#3a4055` | `#b8c5cb` | Texto secundario, etiquetas de formulario, metadatos de artículo.                         |
| `text-muted`     | `#696f84` | `#85989f` | Texto terciario, fechas, estado deshabilitado. Pasa 4.5:1 también sobre `surface-raised`. |
| `brand-deep`     | `#06303d` | `#2f6f80` | Azul petróleo. Color maestro: titulares, barra de navegación, fondos de portada.          |
| `brand`          | `#0b5263` | `#268ba0` | Enlaces, estado activo de navegación, primera serie de gráfico.                           |
| `accent`         | `#1d7a64` | `#31ae91` | Verde esmeralda. Etiquetas de tecnología, hitos de la línea de tiempo, acentos.           |
| `highlight`      | `#2a9d5c` | `#50d188` | Verde claro. **Una sola llamada de atención por página.**                                 |
| `success`        | `#1d7a64` | `#31ae91` | Comentario aprobado, artículo publicado, formulario enviado.                              |
| `warning`        | `#9a6212` | `#d9a745` | Borrador, comentario pendiente de moderación, campo incompleto.                           |
| `danger`         | `#a32433` | `#ef7a86` | Error de validación, fallo de envío, acción destructiva en el panel.                      |
| `info`           | `#1f5fa8` | `#75b5ee` | Aviso neutro, nota informativa.                                                           |

### Reglas de color que no se negocian

- **`highlight` nunca es texto en tema claro.** Da 3.46:1 sobre blanco: alcanza para una forma, un punto o una barra, no para una letra.
- **`border-subtle` no delimita controles.** No llega a 3:1 contra `surface`. Para el borde de un input, de una casilla o de cualquier control, va `border-strong`.
- **`warning` y `accent` tienen la misma luminosidad.** Se distinguen por matiz, así que en escala de grises o para alguien con daltonismo se funden. Donde esos dos estados convivan — por ejemplo la cola de moderación, con comentarios aprobados y pendientes — **el ícono o el texto son obligatorios**: el color nunca es la única señal.
- `success` es deliberadamente el mismo verde que `accent`. Con una paleta verde, un verde de éxito distinto contrastaría tan poco con el acento que serían indistinguibles.

### Portada genérica de artículo (RF-22)

Un artículo sin imagen de portada muestra un bloque de color sólido con el título encima en `surface`. El color se elige de forma determinista a partir del slug, entre `brand-deep`, `brand` y `accent`, para que artículos distintos no se vean iguales y el mismo artículo se vea siempre igual. Los tres superan 5:1 con texto blanco. Sin degradados.

## Tipografía

Dos familias:

```
display: "Inter Display", "Inter", system-ui, sans-serif
text:    "Inter", system-ui, sans-serif
```

> Nota de implementación: **Inter Display no está en Google Fonts**, solo en la distribución oficial de Inter (licencia SIL OFL). Como el proyecto autoaloja las fuentes con subconjunto de caracteres por el presupuesto de rendimiento, se descarga de ahí. Si se quiere evitar el segundo archivo, la alternativa es usar `Inter` también para los display, o `Inter Tight`, que sí está en Google Fonts.

### Escala

| Estilo          | Familia | Tamaño | Interlínea | Peso | Letra    | Para qué                                                   |
| --------------- | ------- | ------ | ---------- | ---- | -------- | ---------------------------------------------------------- |
| `display-xl`    | display | 56px   | 58px       | 600  | -0.02em  | Titular del home. Uno por página.                          |
| `display-l`     | display | 40px   | 44px       | 600  | -0.015em | Titular de sección y de artículo.                          |
| `title`         | display | 28px   | 34px       | 600  | -0.01em  | Título dentro de un documento largo.                       |
| `section`       | display | 20px   | 26px       | 600  | —        | Encabezado de bloque, título de tarjeta.                   |
| `body-l`        | text    | 18px   | 29px       | 400  | —        | Entradilla, resumen, primer párrafo.                       |
| `body`          | text    | 16px   | 26px       | 400  | —        | Texto corrido. El valor por defecto de todo.               |
| `body-emphasis` | text    | 16px   | 26px       | 500  | —        | Dato que no puede pasarse por alto dentro de un párrafo.   |
| `ui`            | text    | 14px   | 22px       | 400  | —        | Texto de interfaz, controles, ayuda de campo.              |
| `numeric`       | text    | 15px   | 22px       | 500  | —        | Fechas y cifras. Con `font-variant-numeric: tabular-nums`. |
| `footnote`      | text    | 13px   | 20px       | 400  | —        | Nota al pie, fuente de un dato, letra menuda.              |
| `label`         | text    | 12px   | 16px       | 500  | 0.1em    | Rótulo en caja alta. Una o dos palabras, nunca frases.     |

En móvil, `display-xl` y `display-l` bajan de escala; los valores concretos se fijan en la feature 01 con el resto del responsive.

## Espaciado

Escala de 4px. Todo margen, relleno y separación sale de aquí.

| Token     | Valor | Para qué                                              |
| --------- | ----- | ----------------------------------------------------- |
| `space-1` | 4px   | Separación entre un ícono y su texto.                 |
| `space-2` | 8px   | Hueco entre etiquetas, relleno vertical de celda.     |
| `space-3` | 12px  | Relleno de campo, hueco entre botones.                |
| `space-4` | 16px  | Relleno de tarjeta. El paso más usado.                |
| `space-5` | 24px  | Separación entre bloques relacionados.                |
| `space-6` | 32px  | Separación entre secciones de una página.             |
| `space-7` | 48px  | Margen interior de página, aire sobre un titular.     |
| `space-8` | 64px  | Separación entre grandes bloques, respiro de portada. |
| `space-9` | 96px  | Aire alrededor de la fotografía del home.             |

## Radios

| Token         | Valor | Para qué                                         |
| ------------- | ----- | ------------------------------------------------ |
| `radius-sm`   | 4px   | Distintivo, etiqueta de tecnología, casilla.     |
| `radius-md`   | 8px   | Botón, campo de formulario.                      |
| `radius-lg`   | 14px  | Tarjeta de proyecto, tarjeta de artículo, panel. |
| `radius-full` | 999px | Píldora, avatar, punto de estado.                |

## Sombras

Dos niveles y nada más.

| Token      | Claro                              | Oscuro                          | Para qué                                                  |
| ---------- | ---------------------------------- | ------------------------------- | --------------------------------------------------------- |
| `shadow-1` | `0 1px 2px rgba(6, 48, 61, 0.10)`  | `0 1px 2px rgba(0, 0, 0, 0.5)`  | Tarjeta en reposo.                                        |
| `shadow-2` | `0 8px 24px rgba(6, 48, 61, 0.14)` | `0 8px 24px rgba(0, 0, 0, 0.6)` | Menú desplegable, panel flotante, botón flotante de tema. |

## Cómo se implementa

- Un único archivo de variables CSS en `:root`, con el bloque del tema oscuro sobrescribiendo los mismos nombres. Tailwind consume esas variables; no se duplican valores en la configuración. El archivo es `web/src/styles/tokens.css`, y el mecanismo concreto —`@theme` con el plugin de Vite de Tailwind— está decidido en `specs/001-sitio-base/research.md`, D-08.
- El cambio de tema alterna un atributo en `<html>`, no una clase por componente.
- Cambiar un valor de esta tabla y el archivo de tokens debe repintar el sitio completo. Si hay que tocar un componente para que el cambio se vea, ese componente está mal escrito.

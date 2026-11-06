# Tokens de diseño

> Fuente única de los valores visuales del portafolio. Resuelve `[P-34]` del brief.
> Estos valores se implementan **una sola vez** en el archivo de tokens del proyecto (RF-04). Ningún componente escribe un color, un tamaño o un radio suelto.
> La dirección visual completa (composición, ritmo, uso de las fotografías) se trabaja en la feature 07 con la skill de diseño.

## Color

Dos temas: claro y oscuro. Todo token existe en los dos. El tema claro es el primario.

| Token            | Claro     | Oscuro    | Para qué                                                                       |
| ---------------- | --------- | --------- | ------------------------------------------------------------------------------ |
| `surface`        | `#ffffff` | `#181b2e` | Fondo base de la página. Todo lo demás se mide contra este.                    |
| `surface-raised` | `#f8f4ed` | `#2b2e4b` | Tarjeta, bloque citado, fila alterna de tabla. En claro es una crema cálida.   |
| `border-subtle`  | `#d9dce6` | `#404564` | Separador decorativo y borde de tabla. **No sirve para delimitar un control.** |
| `border-strong`  | `#878d9e` | `#73779a` | Borde de campo, casilla e interruptor. Pasa 3:1 sobre los dos fondos.          |
| `text`           | `#0b0e1a` | `#f1f1f7` | Texto principal.                                                               |
| `text-secondary` | `#3a4055` | `#c0c2d1` | Texto secundario, etiquetas de formulario, metadatos.                          |
| `text-muted`     | `#696f84` | `#9396aa` | Texto terciario, fechas, estado deshabilitado.                                 |
| `brand-deep`     | `#141b4d` | `#6772c7` | Índigo profundo. Color maestro: titulares, navegación, fondos de portada.      |
| `brand`          | `#2f40b1` | `#8792e2` | Enlaces, estado activo, llamada a la acción, primera serie de gráfico.         |
| `accent`         | `#5466bd` | `#aab2e7` | Etiquetas de tecnología, hitos de la línea de tiempo, segunda serie.           |
| `success`        | `#1d7a64` | `#31ae91` | Comentario aprobado, artículo publicado, formulario enviado.                   |
| `warning`        | `#9a6212` | `#d9a745` | Borrador, comentario pendiente de moderación, campo incompleto.                |
| `danger`         | `#a32433` | `#ef7a86` | Error de validación, fallo de envío, acción destructiva en el panel.           |
| `info`           | `#1f5fa8` | `#75b5ee` | Aviso neutro, nota informativa.                                                |

Los tres índigos son valores exactos del sistema de origen. La crema, los fondos oscuros, los
bordes y los textos del tema oscuro están derivados y medidos: cada uno se movió solo en
claridad, conservando matiz y saturación, hasta alcanzar su objetivo de contraste.

### Reglas de color que no se negocian

- **Todo se mide contra los dos fondos, no solo contra `surface`.** Un campo de formulario
  dentro de una tarjeta se apoya en `surface-raised`, que es el fondo exigente. Es el error que
  tenía la versión anterior de este documento: `border-strong` daba 3.03 sobre el fondo base y
  2.77 sobre la tarjeta, así que el borde de cualquier campo dentro de una tarjeta estaba por
  debajo del mínimo. Los valores de la tabla cumplen contra los dos.
- **`border-subtle` no delimita controles.** Queda por debajo de 3:1 a propósito: es una línea
  decorativa. Para el borde de un input, una casilla o cualquier control, va `border-strong`.
- **Un estado nunca se comunica solo con color.** Siempre lleva además un ícono o una palabra.
  No es una recomendación: medidas en escala de grises, `accent`, `success` y `warning` se
  separan entre 1.00 y 1.35, y `brand` e `info` entre 1.31 y 1.33. Por debajo de 1.40 son
  indistinguibles para quien tiene deficiencia de visión cromática, y en una impresión en
  blanco y negro lo son para todo el mundo.
- **`brand` y `accent` sí se separan**, 1.41 en oscuro y 1.61 en claro, para que un enlace no
  se confunda con una etiqueta.
- **`success` tiene verde propio.** Con la paleta anterior hubo que hacerlo igual que `accent`
  porque dos verdes contrastaban 1.02 entre sí. Con marca índigo esa restricción desaparece.

### Portada genérica de artículo (RF-22)

Un artículo sin imagen de portada muestra un bloque de color sólido con el título encima en blanco. El color se elige de forma determinista a partir del slug, entre `brand-deep`, `brand` y `accent`, para que artículos distintos no se vean iguales y el mismo artículo se vea siempre igual.

**El bloque conserva los valores del tema claro en los dos temas**, como haría una fotografía. Así el texto blanco encima mide siempre lo mismo: 16.23, 8.44 y 5.23. Si el bloque cambiara con el tema, en oscuro el blanco caería a 3.99 sobre `brand` y a 2.76 sobre `accent`. Sin degradados.

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

| Token      | Claro                               | Oscuro                          | Para qué                                                  |
| ---------- | ----------------------------------- | ------------------------------- | --------------------------------------------------------- |
| `shadow-1` | `0 1px 2px rgba(20, 27, 77, 0.10)`  | `0 1px 2px rgba(0, 0, 0, 0.5)`  | Tarjeta en reposo.                                        |
| `shadow-2` | `0 8px 24px rgba(20, 27, 77, 0.14)` | `0 8px 24px rgba(0, 0, 0, 0.6)` | Menú desplegable, panel flotante, botón flotante de tema. |

## Cómo se implementa

- Un único archivo de variables CSS en `:root`, con el bloque del tema oscuro sobrescribiendo los mismos nombres. Tailwind consume esas variables; no se duplican valores en la configuración. El archivo es `web/src/styles/tokens.css`, y el mecanismo concreto —`@theme` con el plugin de Vite de Tailwind— está decidido en `specs/001-sitio-base/research.md`, D-08.
- El cambio de tema alterna un atributo en `<html>`, no una clase por componente.
- Cambiar un valor de esta tabla y el archivo de tokens debe repintar el sitio completo. Si hay que tocar un componente para que el cambio se vea, ese componente está mal escrito.

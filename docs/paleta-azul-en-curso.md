# Cambio de paleta a índigo — trabajo en curso

> **No es la fuente de verdad.** Los tokens vigentes siguen en `design-tokens.md`, con la
> paleta verde. Esto recoge lo decidido y lo medido para el cambio a índigo, para que no se
> pierda y se pueda retomar sin repetir el trabajo.

## Decidido

Paleta **Monocromo Índigo**, con el cuarto color convertido en **fondo alterno**, no en un
cuarto cromático. El cuarto índigo original (`#8492cd`) no servía para texto ni para formas:
daba 3,01 sobre blanco y 2,72 sobre el fondo alterno, por debajo del mínimo de 3,0.

Consecuencia: el token `highlight` desaparece. Una paleta monocroma con tres valores y un
papel cálido no necesita un cuarto cromático que además no podría llevar texto. La llamada
de atención pasa a `brand`, que sirve para texto y para botón relleno.

## Tema claro — verificado

Los tres índigos son valores exactos del sistema de origen. La crema está elegida midiendo.

| Token            | Valor     | Comprobación                                                    |
| ---------------- | --------- | --------------------------------------------------------------- |
| `surface`        | `#ffffff` | —                                                               |
| `surface-raised` | `#f8f4ed` | 1,096 contra blanco: misma separación visual que el gris actual |
| `brand-deep`     | `#141b4d` | exacto del origen                                               |
| `brand`          | `#2f40b1` | exacto del origen, 8,44 sobre blanco                            |
| `accent`         | `#5466bd` | exacto del origen, 5,23 sobre blanco y 4,77 sobre la crema      |
| `text-muted`     | `#696f84` | 4,55 sobre la crema: sigue pasando                              |

Creminas descartadas: `#f6f1e8` baja `text-muted` a 4,44 y `accent` a 4,65, las dos por
debajo de 4,5.

## Tema oscuro — derivado, pero NO válido todavía

El origen solo documenta los cuatro colores claros de esta paleta, así que el tema oscuro hay
que derivarlo. Se derivó imitando los contrastes que la paleta verde ya tenía probados:

| Token            | Derivado  | Contraste sobre el fondo | El verde daba |
| ---------------- | --------- | ------------------------ | ------------- |
| `surface`        | `#111843` | —                        | —             |
| `surface-raised` | `#1e2872` | 1,30                     | 1,30          |
| `border-subtle`  | `#2b3aa5` | 1,82                     | 1,82          |
| `border-strong`  | `#5262d2` | 3,27                     | 3,25          |
| `brand-deep`     | `#4b5bd0` | 3,00                     | 3,00          |
| `brand`          | `#6a78d7` | 4,27                     | 4,28          |
| `accent`         | `#8d99d3` | 6,18                     | 6,15          |
| `text`           | `#f0f1f9` | 15,10                    | 15,11         |
| `text-secondary` | `#bcc1e4` | 9,62                     | 9,63          |
| `text-muted`     | `#8891ce` | 5,66                     | 5,66          |

**El defecto**: la derivación igualó los contrastes pero mantuvo la saturación de la marca, y
los contrastes solos no bastan. El fondo de tarjeta `#1e2872` y el separador `#2b3aa5` salen
azules intensos, mientras que sus equivalentes verdes (`#21333a`, `#354a52`) son grises
teñidos, casi neutros. Una tarjeta sobre fondo azul vivo no es un plano elevado, es un bloque
de color.

**Qué falta**: desaturar las superficies y los bordes del tema oscuro conservando el matiz
índigo, y volver a medir. Los contrastes de la tabla son el objetivo a mantener mientras se
hace.

## Lo que el cambio de paleta arrastra

- Las **reglas de color que no se negocian** de `design-tokens.md` hay que rehacerlas. La
  primera —`highlight` nunca es texto— desaparece con el token. La tercera —`warning` y
  `accent` comparten luminosidad, así que el ícono es obligatorio— se escribió para el verde
  y hay que volver a medirla contra el índigo.
- `success` **recupera un verde propio**: `#1d7a64` claro y `#31ae91` oscuro. Con la paleta
  verde hubo que hacer `success` igual a `accent` porque dos verdes contrastaban 1,02 entre
  sí; con marca índigo esa restricción desaparece.
- La portada genérica de artículo elige entre `brand-deep`, `brand` y `accent`. Los tres
  siguen superando 5:1 con texto blanco, así que esa regla aguanta.
- Las sombras usan `rgba(6, 48, 61, …)`, que es el azul petróleo de la paleta verde. Pasan a
  derivarse de `#141b4d`.

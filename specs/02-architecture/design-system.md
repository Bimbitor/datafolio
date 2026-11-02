# Sistema de diseño

> Tokens y reglas visuales. Estado: **Propuesto**. Objetivo: sobrio, legible, técnico, con personalidad propia (PR-12).

## Dirección visual

[[POR DEFINIR: 2 o 3 adjetivos. Propuesta: "técnico, cálido, preciso".]]

Ideas para que no sea genérico (elegir una o dos):

- Estética de "terminal / consola" sutil: tipografía mono en metadatos, `>` en títulos de sección.
- Estética de "diagrama de arquitectura": líneas finas, cuadrícula de fondo tenue, acentos como conectores.
- Estética de "tablero de vuelos" (guiño al sector turismo): tipografía tabular en métricas.

## Tokens

| Token | Claro | Oscuro | Uso |
|---|---|---|---|
| `--color-bg` | [[#ffffff]] | [[#0b0f14]] | Fondo |
| `--color-surface` | [[#f5f7fa]] | [[#121820]] | Tarjetas |
| `--color-text` | [[#0f172a]] | [[#e6edf3]] | Texto principal |
| `--color-muted` | [[#475569]] | [[#9aa7b4]] | Texto secundario |
| `--color-accent` | [[POR DEFINIR]] | [[POR DEFINIR]] | Enlaces, CTA |
| `--color-border` | [[#e2e8f0]] | [[#243041]] | Bordes |
| `--font-sans` | [[POR DEFINIR]] | | Texto |
| `--font-mono` | [[POR DEFINIR]] | | Código, métricas |
| `--radius` | [[8px]] | | |
| `--space-*` | escala 4/8/12/16/24/32/48/64 | | |
| `--content-width` | [[72ch]] | | Ancho de lectura |

Reglas: máximo 1 o 2 colores de acento; contraste AA verificado en ambos temas.

## Modo oscuro

- Por defecto sigue `prefers-color-scheme`.
- Toggle de 3 estados [[POR DEFINIR: claro / oscuro / sistema, o solo 2]] persistido en `localStorage` (con try/catch).
- Script inline en `<head>` para evitar parpadeo (FOUC).
- Diagramas Mermaid y SVG con variante por tema (o colores vía `currentColor` / variables CSS).
- Bloques de código con tema dual de Shiki.

## Componentes base (a especificar por feature)

| Componente | Feature | Notas |
|---|---|---|
| `Header`, `Footer`, `ThemeToggle`, `LangSwitch` | F-001, F-002 | |
| `Hero` | F-003 | |
| `ProjectCard` | F-005 | Título, resumen, métrica, etiquetas, cover |
| `TagFilter` | F-005 | Sin JS si es posible (enlaces / `:target`) |
| `Mermaid`, `Callout`, `MetricTile`, `DecisionTable` | F-006 | Para MDX |
| `LiveMetrics` | F-007 | Isla |

## Imágenes y foto

- Foto real, reciente, fondo neutro, luz natural. **Nunca generada por IA** (investigación §10).
- [[POR DEFINIR: ¿foto en hero o solo en Sobre mí?]]
- Formatos AVIF/WebP vía `astro:assets`, siempre con `alt`.

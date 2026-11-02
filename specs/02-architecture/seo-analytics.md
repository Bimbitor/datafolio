# SEO y analítica

> Estado: **Propuesto**

## SEO por página

| Elemento | Regla |
|---|---|
| `<title>` | `{Página} · {Nombre}`; home: `{Nombre} · Data Engineer` |
| `meta description` | ≤ 160 caracteres, viene del frontmatter (`summary` / `description`) |
| Open Graph / Twitter | `og:title`, `og:description`, `og:image` (1200×630) por proyecto y post, `og:locale` |
| Canonical | URL absoluta de la página; posts republicados en dev.to/Medium apuntan aquí |
| `hreflang` | Recíproco ES/EN + `x-default` |
| Sitemap | `@astrojs/sitemap` con i18n |
| robots.txt | Permitir todo, enlazar sitemap |
| JSON-LD | `Person` (home y sobre mí: `name`, `jobTitle`, `url`, `sameAs` → GitHub, LinkedIn), `BlogPosting` en posts, `CreativeWork` o `SoftwareSourceCode` en proyectos |

[[POR DEFINIR: ¿imágenes OG generadas automáticamente en build (Satori) o diseñadas a mano?]]

## Analítica

| Opción | Costo | Cookies | Notas |
|---|---|---|---|
| Cloudflare Web Analytics | Gratis | No | Requiere cuenta Cloudflare; funciona sin proxy |
| GoatCounter | Gratis (uso personal) | No | Muy simple |
| Umami Cloud | Gratis con límites | No | Eventos personalizados |
| Plausible | Pago | No | |

Propuesta: [[POR DEFINIR]] (sugerido: GoatCounter o Cloudflare Web Analytics).

## Eventos a medir

| Evento | Dónde |
|---|---|
| `cv_download` (con idioma) | Botón CV |
| `outbound_github` / `outbound_linkedin` | Enlaces salientes |
| `project_view` (slug) | Caso de estudio |
| `lang_switch` | Selector |

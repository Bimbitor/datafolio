# Stack técnico

> Estado: **Propuesto** salvo lo marcado como Aceptado. Cada fila Aceptada debería tener un ADR.

| Capa | Elección | Estado | Alternativas descartadas | Motivo |
|---|---|---|---|---|
| Generador | **Astro** (versión estable actual) | Aceptado (base desplegada) | Quarto, Hugo, Next.js, Jekyll, Gatsby | Cero JS por defecto, MDX, i18n nativo, islas para widgets. Ver investigación §4. |
| Lenguaje | TypeScript (strict) | Propuesto | JS plano | Esquemas de contenido tipados, errores en build. |
| Estilos | Tailwind CSS v4 | Propuesto | CSS propio, UnoCSS | Velocidad, tokens en un solo lugar. [[POR DEFINIR: ¿CSS propio con variables es suficiente?]] |
| Contenido | Markdown + MDX con Content Collections (Zod) | Propuesto | CMS headless | PR-11: un archivo por proyecto. |
| Diagramas | Mermaid (texto) + Excalidraw exportado a SVG | Propuesto | Imágenes PNG | Versionables, nítidos, tema claro/oscuro. |
| Render de Mermaid | [[POR DEFINIR: `rehype-mermaid` en build (SVG estático) vs. Mermaid en cliente]] | Por definir | | Build = 0 JS; cliente = más simple. |
| Resaltado de código | Shiki (incluido en Astro) | Propuesto | Prism | Temas claro/oscuro duales. |
| Gráficos interactivos | Observable Plot o ECharts como isla | Propuesto | Chart.js, D3 directo | Ligeros; solo donde aporten. |
| Íconos | [[POR DEFINIR: astro-icon + Iconify / SVG inline]] | Por definir | | |
| Tipografía | [[POR DEFINIR: una para texto + una mono]] autoalojadas | Por definir | Google Fonts en CDN | Rendimiento y privacidad. |
| Imágenes | `astro:assets` (`<Image />`, AVIF/WebP) | Propuesto | | NFR-001. |
| SEO | `@astrojs/sitemap`, JSON-LD manual | Propuesto | | NFR-005. |
| RSS | `@astrojs/rss` | Propuesto | | FR-031. |
| Calidad | Prettier, ESLint (o Biome), `astro check`, Lighthouse CI, lychee (links) | Propuesto | | NFR-007, NFR-008. |
| Gestor de paquetes | npm | Aceptado (base desplegada) | pnpm, bun | Sin fricción en Actions y Windows. |
| Node | 22 LTS | Aceptado | | |
| CV | [[POR DEFINIR: JSON Resume / YAML propio → HTML + PDF (Playwright)]] | Por definir | Word/Canva | FR-041: una sola fuente. |
| Plantilla de partida | [[POR DEFINIR: Starfolio / Astro Nano / desde cero]] | Por definir | | PR-12: personalizar hasta no ser reconocible. |

## Dependencias permitidas

- Toda dependencia nueva se justifica en el `plan.md` de la feature (qué aporta, peso, mantenimiento).
- Preferir integraciones oficiales de Astro.
- Ninguna dependencia que meta JS global en todas las páginas sin ADR.

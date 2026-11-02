# Features: backlog e índice

> Una carpeta por feature: `NNN-nombre-corto/` con `spec.md`, `plan.md`, `tasks.md`. Copia `_template/` para empezar.

## Backlog propuesto

| ID | Feature | Requisitos | Fase | Estado | Carpeta |
|---|---|---|---|---|---|
| F-000 | Base desplegada en GitHub Pages | NFR-011 | 0 | Hecha | (sin spec, bootstrap) |
| F-001 | Layout base, header, footer, tema claro/oscuro, 404 | FR-001, FR-002, FR-004, FR-042, NFR-003, NFR-004 | 1 | Borrador | |
| F-002 | i18n ES/EN y selector de idioma | FR-003, NFR-005, NFR-007 | 1 | Borrador | |
| F-003 | Página de inicio | FR-010, FR-011, FR-012 | 1 | Borrador | |
| F-004 | Sobre mí y CV (HTML + PDF) | FR-040, FR-041 | 1 | Borrador | |
| F-005 | Colección y listado de proyectos con filtros | FR-020, FR-024, NFR-006 | 1 | Borrador | |
| F-006 | Página de caso de estudio + componentes MDX | FR-021, FR-022, FR-023 | 2 | Borrador | |
| F-007 | Widget de métricas en vivo | FR-013, FR-050, FR-052 | 3 | Borrador | |
| F-008 | Página de estado del sistema | FR-051 | 3 | Borrador | |
| F-009 | Página `/lab` y "cómo construyo con IA" | FR-034 | 4 | Borrador | |
| F-010 | Blog + RSS | FR-030, FR-031, FR-032 | 2 | Borrador | |
| F-011 | Página `/now` | FR-033 | 4 | Borrador | |
| F-012 | CI de calidad (lint, links, Lighthouse, i18n) | NFR-001, NFR-007, NFR-008 | 1 | Borrador | |
| F-013 | SEO técnico (sitemap, OG, JSON-LD, hreflang) | NFR-005 | 1 | Borrador | |
| F-014 | Analítica sin cookies + eventos | NFR-012 | 2 | Borrador | |

Estados: `Borrador` → `Lista` → `En progreso` → `En revisión` → `Hecha` / `Descartada`.

## Cómo crear una feature

```bash
cp -r specs/03-features/_template specs/03-features/001-layout-base
```

Luego llena `spec.md`, pasa la DoR, y sigue con `plan.md` y `tasks.md`. Actualiza la tabla de arriba.

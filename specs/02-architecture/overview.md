# Arquitectura: visión general

> Estado: **Propuesto**. Las decisiones estructurales se registran en `../adr/`.

## Contexto (C4 nivel 1)

```mermaid
flowchart TB
    R([Reclutador / Hiring manager]) -->|HTTPS| SITE[Portafolio estático<br/>Astro]
    J([Javi]) -->|git push / PR| GH[GitHub repo<br/>Bimbitor/datafolio]
    GH -->|GitHub Actions| SITE
    SITE -->|enlaces| REPOS[Repos de proyectos<br/>GitHub]
    SITE -->|enlaces| LI[LinkedIn / Builder Center / dev.to]
    PIPE[Pipeline de datos<br/>Airflow o Action programada] -->|JSON| STORE[(S3 o rama data)]
    STORE -->|fetch en build o en cliente| SITE
    SRC[(Datos abiertos<br/>Aerocivil / datos.gov.co)] --> PIPE
```

## Contenedores (C4 nivel 2)

| Contenedor | Tecnología | Responsabilidad | Spec |
|---|---|---|---|
| Sitio | Astro + MDX + Tailwind | Renderizar páginas estáticas bilingües | `tech-stack.md` |
| Contenido | Content Collections (MD/MDX + Zod) | Proyectos, posts, CV, datos personales | `content-model.md` |
| CI/CD | GitHub Actions | Build, verificaciones, deploy | `deployment.md` |
| Hosting | GitHub Pages (fase 1), S3 + CloudFront (fase 3, propuesto) | Servir archivos | `deployment.md` |
| Pipeline del widget | Python + (Airflow / Action) + S3 | Producir `metrics.json` | `data-pipeline.md` |
| Analítica | [[POR DEFINIR]] sin cookies | Medir uso | `seo-analytics.md` |

## Flujo de una publicación

```mermaid
sequenceDiagram
    participant J as Javi
    participant G as GitHub
    participant A as Actions
    participant P as Pages
    J->>G: push a feat/NNN y abre PR
    G->>A: CI (build + checks)
    A-->>G: estado verde / rojo
    J->>G: merge a main
    G->>A: workflow deploy
    A->>A: npm ci, astro build
    A->>P: upload artifact + deploy
    P-->>J: https://bimbitor.github.io/datafolio/
```

## Estructura del repositorio

```
/
├── AGENTS.md / CLAUDE.md     instrucciones para agentes de IA
├── AI_USAGE.md               registro de uso de IA
├── README.md
├── docs/research/            investigación (no vinculante)
├── specs/                    fuente de verdad (este sistema)
├── src/
│   ├── pages/                rutas (es en raíz, en/ para inglés)
│   ├── layouts/              [futuro]
│   ├── components/           [futuro]
│   ├── content/              [futuro] colecciones
│   ├── i18n/                 [futuro] cadenas de UI
│   └── styles/               [futuro]
├── public/                   assets estáticos (favicon, cv.pdf, og)
├── astro.config.mjs
└── .github/workflows/        deploy.yml (+ ci.yml futuro)
```

## Decisiones abiertas

- [[POR DEFINIR]] ¿Plantilla de partida (Starfolio, Astro Nano) o construcción propia? Ver `tech-stack.md`.
- [[POR DEFINIR]] ¿Migrar hosting a AWS en fase 3? Ver `deployment.md`.
- [[POR DEFINIR]] ¿Dominio propio? ¿Cuál?

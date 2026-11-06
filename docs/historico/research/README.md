# Investigación

Material de referencia que alimentó las specs. No es vinculante: si algo aquí contradice una spec en `specs/`, manda la spec.

| Archivo                                                  | Fuente                     | Fecha      | Enfoque                                                                                          |
| -------------------------------------------------------- | -------------------------- | ---------- | ------------------------------------------------------------------------------------------------ |
| [01-investigacion-claude.md](01-investigacion-claude.md) | Claude (Advanced Research) | 2026-11-01 | Portafolio para Data Engineer híbrido, Astro, hosting, AWS, IA, i18n, foto, plan de 12 semanas   |
| [02-investigacion-gemini.md](02-investigacion-gemini.md) | Gemini (Deep Research)     | 2026-11    | Astro vs Quarto, UX por sección, estructura de repos de datos, proyectos Lakehouse/Streaming/RAG |

## Coincidencias entre ambas

- Generador estático (Astro como primera opción) con CI/CD en GitHub Actions y hosting gratuito.
- 3 proyectos insignia en formato de caso de estudio, con diagramas Mermaid, decisiones y métricas.
- Modo oscuro, bilingüe ES/EN y foto real en "Sobre mí".
- Repos con estructura de ingeniería: tests, CI, Docker, Makefile, README con problema, arquitectura, ejecución y trade-offs.
- Mostrar la IA como parte de la ingeniería (evals, MCP, datos sintéticos), no como chatbot genérico.

## Diferencias a resolver en las specs

- Gemini propone streaming (Kafka/Redpanda) como proyecto 2; Claude propone un proyecto financiero batch con migración SSIS. Ver `specs/04-content/project-catalog.md`.
- Claude propone migrar el hosting a S3 + CloudFront como proyecto AWS; Gemini se queda en GitHub Pages / Netlify / Vercel. Ver `specs/02-architecture/deployment.md`.

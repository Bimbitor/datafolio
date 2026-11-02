# datafolio

Portafolio de **Javi Rodríguez Giraldo**, Data Engineer con base en ciencia de datos.

🌐 **Sitio:** https://bimbitor.github.io/datafolio/

> Estado: **fundaciones**. El sitio publicado es una versión base; el diseño y contenido se construyen feature por feature siguiendo las specs.

## Cómo está organizado

| Carpeta | Qué hay |
|---|---|
| [`specs/`](specs/README.md) | Fuente de verdad: constitución, producto, arquitectura, features, contenido, ADRs y checklists (spec-driven development). |
| [`docs/research/`](docs/research/README.md) | Investigaciones que alimentaron las specs (Claude y Gemini). |
| `src/` | Código del sitio (Astro). |
| `public/` | Archivos estáticos. |
| `.github/workflows/` | Despliegue a GitHub Pages. |
| [`AGENTS.md`](AGENTS.md) | Reglas para agentes de IA que trabajen en el repo. |
| [`AI_USAGE.md`](AI_USAGE.md) | Registro de lo construido con IA. |

## Desarrollo local

Requiere Node 22+.

```bash
npm install
npm run dev       # http://localhost:4321/datafolio/
npm run build     # genera dist/
npm run preview   # sirve dist/
```

## Flujo de trabajo

1. Elegir o crear una feature en [`specs/03-features/`](specs/03-features/README.md).
2. Completar `spec.md` → `plan.md` → `tasks.md`.
3. Rama `feat/NNN-nombre`, PR a `main`.
4. Al hacer merge a `main`, GitHub Actions construye y publica en Pages.

## Stack

Astro · TypeScript · GitHub Actions · GitHub Pages. Ver [specs/02-architecture/tech-stack.md](specs/02-architecture/tech-stack.md).

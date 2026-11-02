# ADR-0002: Astro + GitHub Pages como base

| Campo | Valor |
|---|---|
| Estado | Aceptado |
| Fecha | 2026-11-01 |
| Decisor | Javi |
| Features / specs afectadas | `02-architecture/tech-stack.md`, `02-architecture/deployment.md`, F-000 |

## Contexto

Se necesita un sitio estático, gratuito, fácil de mantener, con i18n y MDX, y capaz de alojar islas interactivas para el widget de datos. Ambas investigaciones (Claude y Gemini) coinciden en Astro como primera opción.

## Opciones consideradas

| Opción | Pros | Contras |
|---|---|---|
| Astro | Cero JS por defecto, MDX, i18n nativo, islas | Curva ligera de TS |
| Quarto | Renderiza notebooks, ideal para DS | Menos flexible para marca personal, i18n artesanal |
| Hugo | Build muy rápido | Plantillas Go, sin componentes |
| Next.js | Ecosistema React | Pesado para contenido, más mantenimiento |

Hosting: GitHub Pages (integrado al repo, gratis) vs Cloudflare Pages (ilimitado, previews) vs Netlify/Vercel (límites o restricción comercial).

## Decisión

Astro como generador y GitHub Pages con despliegue por GitHub Actions desde `main`, en el repo `datafolio`, servido en `https://bimbitor.github.io/datafolio/` (Astro con `base: "/datafolio"`). Con un dominio propio en el futuro, la ruta base se elimina.

## Consecuencias

**Positivas:** costo 0, nombre de repo con marca propia, deploy automático, cero configuración extra.

**Negativas:** la URL lleva la subruta `/datafolio/` hasta tener dominio propio; sin headers HTTP propios (CSP solo por meta), sin previews de PR nativas.

**Qué haría revisar esta decisión:** fase 3 del roadmap (migración a S3 + CloudFront) o necesidad de previews.

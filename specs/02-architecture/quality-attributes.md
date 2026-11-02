# Atributos de calidad: rendimiento, accesibilidad, seguridad

> Cómo se cumplen y verifican los NFR. Estado: **Propuesto**

## Rendimiento (NFR-001, NFR-002)

- HTML estático; JS solo en islas con `client:visible` o `client:idle`.
- Fuentes autoalojadas, `font-display: swap`, subset latino.
- Imágenes con `astro:assets`, tamaños responsivos, lazy loading debajo del pliegue.
- Presupuestos: LCP < 2.0 s, CLS < 0.05, TBT < 100 ms (móvil, Lighthouse).
- Verificación: Lighthouse CI en cada PR sobre home y un caso de estudio.

## Accesibilidad (NFR-003, NFR-004)

- HTML semántico (`header`, `nav`, `main`, `article`, `footer`), un `h1` por página.
- Enlace "Saltar al contenido".
- Foco visible en todos los elementos interactivos.
- Diagramas: `alt` corto + resumen textual de la arquitectura debajo (o `<details>`).
- `prefers-reduced-motion`: sin animaciones.
- Verificación: Lighthouse + axe en CI; revisión manual con teclado antes de cada release.

## Seguridad (NFR-009)

- Sin secretos en el repo; GitHub secret scanning y Dependabot activos.
- Deploy a Pages con `GITHUB_TOKEN` y permisos mínimos (`pages: write`, `id-token: write`).
- Fase AWS: OIDC de GitHub a un rol IAM de mínimo privilegio, bucket privado con OAC.
- Enlaces externos con `rel="noopener noreferrer"`.
- [[POR DEFINIR: Content-Security-Policy vía `<meta>` (Pages no permite headers propios) o vía CloudFront en fase AWS]].

## Mantenibilidad (NFR-006, NFR-007)

- `astro check` y lint en CI.
- Esquemas Zod en colecciones.
- Verificación de claves i18n.
- Dependabot semanal; actualizar Astro en una feature dedicada.

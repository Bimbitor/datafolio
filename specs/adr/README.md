# Architecture Decision Records (ADR)

Registro de decisiones estructurales. Un ADR **aceptado no se edita**: si la decisión cambia, se crea un ADR nuevo que lo reemplaza (`Reemplazado por ADR-NNNN`).

## Cuándo crear un ADR

- Cambia el stack, el hosting, el modelo de contenido o un principio de la constitución.
- Hay dos o más alternativas razonables y elegir una tiene consecuencias a futuro.
- Una feature agrega JS global, una dependencia pesada o un servicio de pago.

## Cómo

1. Copia `_template.md` a `NNNN-titulo-en-kebab.md` (número siguiente).
2. Estado `Propuesto` mientras se discute; `Aceptado` cuando Javi decide.
3. Actualiza la tabla de abajo y las specs de `02-architecture/` afectadas.

## Índice

| ADR | Título | Estado | Fecha |
|---|---|---|---|
| [0001](0001-adoptar-spec-driven-development.md) | Adoptar spec-driven development | Aceptado | 2026-11-01 |
| [0002](0002-astro-github-pages-base.md) | Astro + GitHub Pages como base | Aceptado | 2026-11-01 |
| 0003 | [[POR DEFINIR: Idioma por defecto]] | | |
| 0004 | [[POR DEFINIR: Render de Mermaid]] | | |
| 0005 | [[POR DEFINIR: Migración de hosting a AWS]] | | |

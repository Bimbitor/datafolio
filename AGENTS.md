# Instrucciones para agentes de IA

Este repo usa **spec-driven development**. Antes de escribir código, lee en este orden:

1. `specs/00-constitution.md` (reglas no negociables)
2. `specs/README.md` (cómo funciona el sistema)
3. La spec de la feature en la que trabajas: `specs/03-features/NNN-*/spec.md`, `plan.md`, `tasks.md`
4. Las specs de `specs/02-architecture/` que la feature referencie

## Reglas

- **No implementes nada sin una feature en estado `Lista` o `En progreso`.** Si te piden algo que no tiene spec, propón primero la spec usando `specs/03-features/_template/`.
- Trabaja tarea por tarea según `tasks.md`; marca `[x]` y anota el commit.
- Si el plan no sirve, **actualiza `plan.md` y explica por qué** antes de desviarte.
- Decisiones estructurales → propone un ADR en `specs/adr/` con estado `Propuesto`. No lo marques `Aceptado`: solo Javi acepta.
- No agregues dependencias sin justificarlas en `plan.md`.
- Enlaces internos y assets siempre con `import.meta.env.BASE_URL` (el sitio vive en `/datafolio/`).
- Toda cadena visible en ES y EN (`src/i18n/`). Sin texto hardcodeado en componentes.
- Cero JS en el cliente salvo islas justificadas.
- Nunca escribas secretos ni datos confidenciales del empleador.
- Textos públicos: sin rayas (—) ni guiones dobles; frases separadas por comas o puntos.
- Al terminar, agrega una entrada en `AI_USAGE.md`.

## Comandos

```bash
npm install
npm run dev
npm run build
```

## Precedencia ante conflicto

Constitución > ADR aceptado > `specs/02-architecture` > `specs/01-product` > spec de feature > código existente.

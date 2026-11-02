# ADR-0001: Adoptar spec-driven development

| Campo | Valor |
|---|---|
| Estado | Aceptado |
| Fecha | 2026-11-01 |
| Decisor | Javi |
| Features / specs afectadas | Todas |

## Contexto

El portafolio lo mantiene una sola persona con poco tiempo, apoyándose en agentes de IA. Sin una fuente de verdad escrita, los agentes generan código inconsistente y las decisiones se pierden. Además, el propio proceso es evidencia de criterio de ingeniería para los reclutadores técnicos.

## Opciones consideradas

| Opción | Pros | Contras |
|---|---|---|
| A. Construir directo, documentar al final | Rápido al inicio | Deriva, decisiones perdidas, la IA improvisa |
| B. Solo issues de GitHub | Ligero | Sin visión global ni trazabilidad |
| C. SDD en `specs/` (constitución → producto → arquitectura → feature: spec, plan, tasks) + ADRs | Trazable, legible por IA, demuestra proceso | Costo inicial de escritura |

## Decisión

Elegimos **C**. Ninguna feature se implementa sin `spec.md` en estado Lista (PR-08).

## Consecuencias

**Positivas:** agentes de IA con contexto preciso, historial de decisiones, proceso mostrable en el portafolio.

**Negativas:** más archivos que mantener; riesgo de que las specs queden desactualizadas (mitigado por la DoD).

**Qué haría revisar esta decisión:** si mantener specs consume más del 30% del tiempo del proyecto.

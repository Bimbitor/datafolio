# Definition of Done (DoD)

Una feature pasa a **Hecha** cuando:

## Funcional
- [ ] Todos los criterios de aceptación verificados.
- [ ] Funciona en ES y EN; selector lleva a la página equivalente.
- [ ] Funciona en tema claro y oscuro.
- [ ] Funciona en móvil (360 px) y escritorio.

## Calidad
- [ ] `npm run build` sin errores ni warnings nuevos.
- [ ] `astro check` / lint en verde (cuando exista F-012).
- [ ] Lighthouse ≥ 95 en las 4 categorías en páginas afectadas.
- [ ] Navegable con teclado; foco visible.
- [ ] Sin enlaces rotos.
- [ ] Sin secretos ni datos confidenciales.

## Documentación
- [ ] `tasks.md` con todas las tareas marcadas y commits anotados.
- [ ] Specs afectadas actualizadas en el mismo PR (requirements: estado → Hecho).
- [ ] ADR creado si hubo una decisión estructural.
- [ ] `AI_USAGE.md` actualizado si se usó IA.
- [ ] Tabla de `03-features/README.md` actualizada.

## Entrega
- [ ] PR mergeado a `main` con referencia `F-NNN`.
- [ ] Deploy en verde y verificado en https://bimbitor.github.io/datafolio/.

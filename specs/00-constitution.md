# Constitución del proyecto

> Principios no negociables. Toda spec, plan, tarea o PR debe respetarlos. Cambiar uno requiere un ADR aceptado.
>
> Estado: **Propuesto**, pendiente de revisión por Javi.

## Misión

[[POR DEFINIR: una frase. Propuesta: "Demostrar en menos de 60 segundos que Javi es un Data Engineer con base en ciencia de datos que construye pipelines reales en AWS, y dar evidencia verificable de ello."]]

## Principios

| ID | Principio | Qué implica en la práctica |
|---|---|---|
| PR-01 | **Evidencia antes que adjetivos.** | Ninguna afirmación ("sé Spark") sin un enlace a algo que lo pruebe (repo, caso de estudio, métrica). Nada de barras de nivel de skills. |
| PR-02 | **Los proyectos son el producto; el sitio es la vitrina.** | El esfuerzo se reparte ~20% sitio / ~80% proyectos. Una mejora visual nunca bloquea publicar un caso de estudio. |
| PR-03 | **Dos clics al proyecto insignia.** | Desde cualquier punto de entrada (home, LinkedIn, GitHub, un post) se llega al proyecto insignia en máximo 2 clics. |
| PR-04 | **Estático primero, cero JS por defecto.** | Solo se envía JavaScript al cliente cuando una funcionalidad lo exige (isla). Se justifica en el plan de la feature. |
| PR-05 | **Bilingüe de verdad.** | Toda página pública existe en ES y EN, o declara explícitamente que no. No hay textos de UI sin traducir. |
| PR-06 | **Accesible y rápido.** | Lighthouse ≥ 95 en las 4 categorías (móvil). Contraste WCAG AA. Funciona con teclado. |
| PR-07 | **IA documentada, nunca escondida.** | Todo lo construido con asistencia de IA se registra en `AI_USAGE.md`. Javi debe poder explicar y defender cada línea. |
| PR-08 | **Spec primero.** | No se escribe código de una feature sin `spec.md` en estado Lista. Los hotfix son la única excepción y se documentan después. |
| PR-09 | **Cero secretos en el repo.** | Credenciales solo en GitHub Secrets / OIDC. `.env.example` sí, `.env` nunca. |
| PR-10 | **Costo cero o acotado.** | Hosting y servicios gratuitos por defecto. Todo recurso de pago tiene presupuesto y alerta (AWS Budgets) antes de crearse. |
| PR-11 | **Mantenible por una persona con poco tiempo.** | Agregar un proyecto o post = crear un archivo Markdown/MDX. Sin CMS, sin base de datos para el sitio. |
| PR-12 | **Nada genérico.** | Sin datasets de tutorial (Titanic, Iris, MNIST). Plantillas siempre personalizadas hasta no ser reconocibles. |

## Estilo de escritura

- Textos públicos en primera persona, directos, sin rayas (—) ni guiones dobles; las frases se separan con comas o puntos.
- Ver `04-content/voice-and-tone.md`.

## Gobierno

- **Dueño y aprobador único:** Javi.
- **Agentes de IA:** proponen y ejecutan; no aprueban. Ver `AGENTS.md`.
- **Precedencia ante conflicto:** Constitución > ADR aceptado > `02-architecture` > `01-product` > spec de feature > código.

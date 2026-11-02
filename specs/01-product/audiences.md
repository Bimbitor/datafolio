# Audiencias

> Diseñamos para estas personas, en este orden de prioridad. Estado: **Propuesto**

## A1. Reclutador / Talent Acquisition (no técnico)

- **Contexto:** revisa decenas de perfiles; dedica 30 s a 2 min por sitio.
- **Quiere saber:** rol, seniority, stack, idioma, ubicación / disponibilidad remota, cómo contactarlo.
- **Entra por:** enlace en CV, LinkedIn, plataforma de empleo.
- **Éxito:** en 60 s puede decir "Data Engineer, AWS, Bogotá, inglés, aquí está su CV".
- **Implica:** hero claro, CV descargable visible, contacto en el header/footer, nada de jerga en el primer pantallazo.

## A2. Hiring manager / Data Engineer Senior (técnico)

- **Contexto:** filtra antes o después de la entrevista técnica. Lee 1 o 2 proyectos a fondo.
- **Quiere saber:** ¿entiende idempotencia, particionamiento, calidad, costos? ¿Escribe código mantenible? ¿Sabe explicar trade-offs?
- **Entra por:** enlace del reclutador o del CV directo al proyecto.
- **Éxito:** encuentra arquitectura, decisiones, tests y CI en verde sin buscar.
- **Implica:** plantilla de caso de estudio rigurosa, enlaces directos a código relevante, ADRs.

## A3. Comunidad técnica / pares

- **Contexto:** llega por un post (Builder Center, dev.to, LinkedIn).
- **Quiere:** aprender algo concreto.
- **Implica:** blog con RSS, posts autocontenidos que enlazan al proyecto.

## A4. Javi (mantenedor)

- **Contexto:** poco tiempo, trabaja por las noches, a veces con agentes de IA.
- **Quiere:** agregar un proyecto o post en < 30 min sin romper nada.
- **Implica:** contenido en Markdown/MDX, esquemas validados, CI que falla temprano, `AGENTS.md` claro.

## Recorridos clave (user journeys)

| ID | Audiencia | Recorrido | Clics máximos |
|---|---|---|---|
| J-1 | A1 | Home → Descargar CV | 1 |
| J-2 | A1 | Home → Contacto (email / LinkedIn) | 1 |
| J-3 | A2 | Home → Proyecto insignia → Repo | 2 |
| J-4 | A2 | Proyecto → Decisiones (ADR) | 1 dentro de la página |
| J-5 | A3 | Post → Proyecto relacionado | 1 |
| J-6 | Todos | Cualquier página → cambiar idioma manteniendo la página equivalente | 1 |

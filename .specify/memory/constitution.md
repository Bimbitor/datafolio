# Datafolio Constitution

Portafolio profesional de Javi, Data Engineer híbrido entre ciencia de datos e ingeniería de
datos (AWS, Airflow, Spark). Su propósito es demostrar con evidencia verificable que construye
sistemas de datos reales, y llevar a quien lo visita hasta esos proyectos en el menor número de
clics. Las reglas de esta constitución son inmutables y el agente de IA MUST respetarlas
estrictamente.

## Core Principles

### I. Evidencia Verificable (NO NEGOCIABLE)

- Es la regla crítica del sistema: toda afirmación sobre una habilidad o un resultado MUST ir
  acompañada de un enlace que la demuestre, sea un repositorio, un caso de estudio o una métrica.
- MUST NOT publicarse barras de nivel de habilidad ni listas de tecnologías sin respaldo.
- MUST NOT usarse datasets de tutorial como Titanic, Iris o MNIST: no demuestran nada.
- Toda plantilla de terceros MUST personalizarse hasta no ser reconocible.
- Todo lo construido con asistencia de IA MUST registrarse en `AI_USAGE.md`, y Javi MUST poder
  explicar y defender cada línea del repositorio.

**Razón**: un portafolio que no se puede verificar es peor que no tener portafolio. El lector
técnico descuenta todo lo que no puede comprobar, y una sola afirmación inflada contamina las
que sí eran ciertas.

### II. Los Proyectos Viven Fuera (NO NEGOCIABLE)

- Los proyectos del portafolio viven en sus propios repositorios y URLs. Este repositorio
  MUST NOT alojar el código de ningún proyecto, solo una ficha con su enlace.
- Añadir un proyecto o una entrada MUST ser crear un único archivo Markdown.
- MUST NOT introducirse un gestor de contenidos ni una base de datos para el contenido del sitio.
- Una mejora visual del sitio MUST NOT bloquear la publicación de un caso de estudio.

**Razón**: contratan por los proyectos, no por el sitio. Y este portafolio se mantiene en ratos
libres, así que lo que exige ceremonia se abandona a la tercera semana.

### III. Estático por Defecto y Presupuestos Duros

- Las páginas MUST servirse como HTML estático. MUST NOT enviarse JavaScript al cliente salvo en
  una isla justificada en el plan de su feature.
- Toda dependencia MUST fijarse con versión exacta, sin rangos. Node y Python se cuentan por
  separado.
- El bundle de Python en Vercel MUST NOT superar los 500 MB, controlado con `excludeFiles` en
  `vercel.json`.
- Los servicios MUST ser gratuitos por defecto. Todo recurso de pago MUST tener presupuesto y
  alerta configurados antes de crearse.
- Cada dependencia nueva MUST justificarse en el `plan.md` de su feature indicando qué aporta,
  cuánto pesa y quién la mantiene.

**Razón**: cada kilobyte y cada dependencia es un costo que nadie va a revisar después. El límite
se pone ahora, cuando cuesta una línea de configuración.

### IV. Spec Primero y Cero Código Sombra

- Se construye estrictamente lo documentado en la spec de la feature. MUST NOT añadirse
  características "por si acaso", como pasarelas de pago, notificaciones o paneles de
  administración.
- Ninguna funcionalidad se implementa sin una spec en estado listo bajo `specs/`. Ante una
  petición sin spec, el agente MUST proponer la spec primero.
- Si una instrucción del usuario contradice esta constitución, o si se detecta una falla lógica,
  el agente MUST detenerse, advertir del problema y solicitar la actualización de la spec o de
  esta constitución antes de tocar el código fuente.
- Las decisiones estructurales MUST registrarse como ADR en `docs/adr/` con estado Propuesto. Un
  agente MUST NOT marcar un ADR como Aceptado.

**Razón**: Spec-Driven Development requiere que la especificación y el código no divergan. Un
agente que improvisa produce código que nadie pidió y que nadie podrá defender en una entrevista.

### V. Test Antes que Lógica

- Toda lógica nueva no trivial MUST tener una prueba que falle antes de escribirla.
- El alcance exacto de las pruebas MUST definirse en un ADR propio cuando exista el primer código
  que testear.
- Hasta que ese ADR exista, MUST NOT instalarse ninguna herramienta de pruebas.

**Razón**: elegir el marco de pruebas antes de saber qué se testea deja herramientas que nadie usa
y tests de adorno que no protegen nada.

### VI. Observable por Diseño

- Toda feature MUST declarar en su plan qué se mide y qué umbral la rompe. Una feature sin métrica
  declarada MUST NOT considerarse terminada.
- El backend MUST emitir logs estructurados con identificador de petición, latencia y resultado.
- Cada PR MUST verificar el peso de `dist/`, el puntaje de Lighthouse y que no haya enlaces roto.

**Razón**: sin una señal declarada de antemano no hay forma de saber si una feature sigue
funcionando un mes después, y un portafolio roto en silencio es peor que uno sin publicar.

### VII. Accesible y Rápido

- Lighthouse MUST marcar 95 o más en las cuatro categorías en móvil.
- El contraste MUST cumplir WCAG AA.
- Toda funcionalidad MUST poder usarse solo con teclado, con foco visible.
- Los diagramas MUST llevar texto alternativo y un resumen en texto.

**Razón**: un sitio inaccesible o lento contradice en la práctica todo lo que el portafolio afirma
saber de ingeniería.

## Stack Tecnológico

- **Arquitectura**: un solo proyecto de Vercel. Astro estático sirve el sitio y los archivos de
  `api/` son funciones Python independientes.
- **Frontend**: Astro con TypeScript en modo estricto. Estilos con Tailwind CSS v4 sobre tokens
  propios de color, tipografía y escala.
- **Backend**: FastAPI sobre el runtime de Python de Vercel. Atiende servicios del sitio y
  MUST NOT procesar datos.
- **Datos**: sin base de datos. El contenido vive en archivos Markdown versionados.
- **Idiomas**: español primero. La estructura de internacionalización (rutas, claves, hreflang)
  MUST existir desde el inicio para que añadir inglés no obligue a rehacer el ruteo.
- **Gestores**: npm para Node, uv para Python.
- **Versiones**: Node 24 o superior, igual en local y en CI. La versión de Python se fija a la que
  acepte el runtime de Vercel.

Cualquier dependencia o tecnología adicional MUST justificarse en el `plan.md` de su feature
frente al Principio III.

## Estilo de Código, Errores y Secretos

- **Estilo**: priorizar funciones puras y módulos pequeños. Evitar clases salvo que una librería
  lo haga obligatorio.
- **Nomenclatura**: camelCase para funciones y variables en TypeScript, PascalCase para tipos y
  componentes, snake_case en Python.
- **Errores en UI**: MUST NOT exponerse errores crudos ni *stack traces* al visitante. Todo error
  técnico MUST traducirse a un mensaje claro (ej.: "No pude enviar el mensaje, intenta de nuevo").
- **Errores en el backend**: MUST retornarse códigos HTTP semánticos: 400 petición inválida, 422
  validación fallida, 429 demasiadas peticiones, y 500 solo para fallas no previstas y sin detalle
  técnico en el cuerpo.
- **Secretos**: las credenciales MUST vivir solo en variables de entorno de Vercel. Se versiona
  `.env.example` sin valores y `.env` MUST NOT versionarse nunca. Ningún dato confidencial de un
  empleador entra al repositorio.

## Estilo de Escritura

- Los textos públicos se escriben en primera persona, directos, sin rayas ni guiones dobles. Las
  frases se separan con comas o puntos.
- MUST NOT quedar texto visible escrito directamente dentro de un componente: toda cadena vive en
  los archivos de idioma.
- Todo texto público MUST pasar por la skill `humanizer` antes de publicarse.

## Governance

- Esta constitución prevalece sobre cualquier otra práctica, instrucción o documento del proyecto.
  Las specs, los planes y las tareas MUST ser coherentes con ella.
- **Precedencia ante conflicto**: esta constitución, luego un ADR aceptado, luego
  `docs/architecture/`, luego la spec de la feature, y por último el código existente.
- **Dueño y aprobador único**: Javi. Los agentes de IA proponen y ejecutan, y MUST NOT aprobar.
- **Citación**: los principios se citan por su número, por ejemplo "cumple el Principio III".
- **Enmiendas**: se realizan mediante `/speckit-constitution`, documentando el cambio en el Sync
  Impact Report y revisando la coherencia de los artefactos existentes.
- **Versionado** (SemVer):
  - MAJOR: eliminación o redefinición incompatible de principios o reglas de dominio.
  - MINOR: nuevo principio o sección, o ampliación material de una guía.
  - PATCH: aclaraciones, redacción o erratas sin cambio semántico.
- **Bitácora**: un cambio por commit, siempre revertible por separado. Asunto con el formato
  `vX.Y.Z-AAAA-MM-DD-tipo: descripción`, cuerpo de dos renglones como máximo, y tag anotado por
  versión.
- **Cumplimiento**: cada plan (`/speckit-plan`) MUST superar el "Constitution Check", y toda
  revisión de código MUST verificar en especial los Principios I (evidencia) y IV (cero código
  sombra). Todo cambio de código MUST seguir la skill `ponytail` y todo diseño de interfaz la
  skill `frontend-design`. Toda complejidad adicional MUST justificarse por escrito.

**Version**: 1.0.0 | **Ratified**: 2026-11-02 | **Last Amended**: 2026-11-02

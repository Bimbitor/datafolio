# Constitución de datafolio

Portafolio profesional de Javi, Data Engineer híbrido entre ciencia de datos e ingeniería de
datos (AWS, Airflow, Spark). Este documento manda sobre cualquier otra práctica del
repositorio. Las specs, los planes, las tareas y el código lo respetan sin excepción.

## Principios fundamentales

### P-01 · Evidencia antes que adjetivos

Toda afirmación sobre una habilidad DEBE ir acompañada de un enlace que la demuestre: un
repositorio, un caso de estudio o una métrica. NUNCA se usan barras de nivel de habilidad ni
listas de tecnologías sin respaldo.

Razón: el lector técnico descuenta todo lo que no puede verificar, y una afirmación sin prueba
resta credibilidad a las que sí la tienen.

### P-02 · Los proyectos son el producto, el sitio es la vitrina

Los proyectos viven en sus propios repositorios y URLs. Este repositorio NUNCA aloja el código
de un proyecto del portafolio, solo una ficha con su enlace. Una mejora visual del sitio NUNCA
bloquea la publicación de un caso de estudio.

Razón: contratan por los proyectos. El sitio solo tiene que llevar hasta ellos sin estorbar.

### P-03 · Spec antes que código

Ninguna funcionalidad se implementa sin una especificación en estado listo bajo `specs/`. Ante
una petición sin spec, el agente DEBE proponer la spec primero. Un arreglo urgente es la única
excepción y se documenta el mismo día.

### P-04 · Test antes que lógica

Toda lógica nueva no trivial DEBE tener una prueba que falle antes de escribirla. El alcance
exacto de las pruebas se define en un ADR propio cuando exista el primer código que testear, y
hasta entonces NO se instala ninguna herramienta de pruebas.

Razón: elegir el marco de pruebas antes de saber qué se testea deja herramientas instaladas que
nadie usa, y tests de adorno que no protegen nada.

### P-05 · Observable por diseño

Toda feature DEBE declarar en su plan qué se mide y qué umbral la rompe. Una feature sin métrica
declarada no se considera lista. El backend DEBE emitir logs estructurados con identificador de
petición, latencia y resultado.

### P-06 · Presupuesto de dependencias

Node y Python se cuentan por separado. El bundle de Python en Vercel NUNCA supera los 500 MB.
Toda dependencia se fija con versión exacta, sin rangos. Cada dependencia nueva se justifica en
el plan de su feature indicando qué aporta, cuánto pesa y quién la mantiene. Ninguna dependencia
que envíe JavaScript global a todas las páginas entra sin ADR aceptado.

### P-07 · Estático por defecto

Las páginas se sirven como HTML estático. NUNCA se envía JavaScript al cliente salvo en una isla
justificada en el plan de su feature.

### P-08 · Accesible y rápido

Lighthouse DEBE marcar 95 o más en las cuatro categorías en móvil. El contraste cumple WCAG AA.
Toda funcionalidad DEBE poder usarse solo con teclado, con foco visible. Los diagramas llevan
texto alternativo y un resumen en texto.

### P-09 · Español primero, inglés sin rehacer rutas

El contenido se publica primero en español. La estructura de internacionalización (rutas, claves,
hreflang) DEBE existir desde el inicio para que añadir inglés no obligue a rehacer el ruteo. NUNCA
hay texto visible escrito directamente dentro de un componente.

### P-10 · Cero secretos en el repositorio

Las credenciales viven solo en variables de entorno de Vercel. Se versiona `.env.example` sin
valores. `.env` NUNCA se versiona. Ningún dato confidencial de un empleador entra al repositorio.

### P-11 · Costo cero o acotado

El hosting y los servicios son gratuitos por defecto. Todo recurso de pago DEBE tener presupuesto
y alerta configurados antes de crearse.

### P-12 · Mantenible por una persona con poco tiempo

Añadir un proyecto o una entrada DEBE ser crear un archivo Markdown. NUNCA se introduce un gestor
de contenidos ni una base de datos para el contenido del sitio.

Razón: el portafolio se mantiene en ratos libres. Lo que exige ceremonia se abandona.

### P-13 · Nada genérico

NUNCA se usan datasets de tutorial como Titanic, Iris o MNIST. Toda plantilla de terceros se
personaliza hasta no ser reconocible.

### P-14 · IA documentada, nunca escondida

Todo lo construido con asistencia de IA se registra en `AI_USAGE.md`. Javi DEBE poder explicar y
defender cada línea del repositorio.

Razón: el uso de IA es parte de la ingeniería que se demuestra. Esconderlo lo convierte en un
riesgo en la primera entrevista técnica.

### P-15 · Commits atómicos de bitácora

Un cambio por commit, siempre revertible por separado. Asunto con el formato
`vX.Y.Z-AAAA-MM-DD-tipo: descripción`. Cuerpo de dos renglones como máximo. Cada versión lleva su
tag anotado.

## Restricciones técnicas

| Aspecto | Regla |
|---|---|
| Arquitectura | Astro estático y backend FastAPI en un solo proyecto de Vercel. |
| Datos | Sin base de datos. El backend atiende servicios del sitio, no procesa datos. |
| Estilos | Tailwind v4 con tokens propios de color, tipografía y escala. |
| Node | 24 o superior, igual en local y en CI. |
| Python | Versión fijada a la que acepte el runtime de Vercel, confirmada en el primer deploy. |
| Peso del sitio | `dist/` bajo presupuesto declarado, verificado en cada PR. |
| Bundle de Python | 500 MB duro, con `excludeFiles` en `vercel.json`. |

Qué se observa y dónde:

| Capa | Señal | Dónde se lee |
|---|---|---|
| Backend | Tasa de error, latencia p95, logs con identificador de petición. | Runtime logs de Vercel. |
| Frontend | Visitas y Core Web Vitals reales. | Analítica sin cookies. |
| Cada PR | Peso de `dist/`, Lighthouse, enlaces roto. | CI. |

## Flujo de trabajo

El ciclo por feature usa spec-kit: `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement`.
Las tareas se marcan una por una y cada una queda trazable a un requisito.

Las decisiones estructurales se registran como ADR en `docs/adr/` con estado Propuesto. Un agente
NUNCA marca un ADR como Aceptado.

Skills obligatorias: **ponytail** en todo cambio de código, **frontend-design** al diseñar
interfaz, **humanizer** sobre todo texto público antes de publicarlo.

Los textos públicos del sitio se escriben en primera persona, directos, sin rayas ni guiones
dobles. Las frases se separan con comas o puntos.

Una feature está lista cuando cumple su spec, pasa lint, tipos y pruebas, respeta su presupuesto
de peso, declara su métrica y tiene su entrada en `AI_USAGE.md`.

## Gobierno

Dueño y aprobador único: Javi. Los agentes de IA proponen y ejecutan, nunca aprueban.

Precedencia ante conflicto: esta Constitución, luego un ADR aceptado, luego `docs/architecture/`,
luego la spec de la feature, y por último el código existente.

Los principios se citan por su identificador, por ejemplo "cumple P-06", en specs, planes y
revisiones.

Enmiendas: toda modificación requiere un ADR aceptado y un cambio de versión de este documento.
MAYOR al retirar o redefinir un principio de forma incompatible, MENOR al añadir un principio o
ampliar una guía de forma sustantiva, PARCHE para aclaraciones y correcciones sin efecto
semántico.

Cumplimiento: toda revisión verifica que el cambio respeta los principios aplicables. Lo que añade
complejidad se justifica por escrito o no entra.

**Version**: 1.0.0 | **Ratified**: 2026-11-02 | **Last Amended**: 2026-11-02

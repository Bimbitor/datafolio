---
description: "Lista de tareas para la implementación de la feature 001-sitio-base"
---

# Tasks: Sitio base

**Input**: Documentos de diseño en `/specs/001-sitio-base/`

**Prerequisites**: [plan.md](./plan.md), [spec.md](./spec.md), [research.md](./research.md),
[data-model.md](./data-model.md), [contracts/http.md](./contracts/http.md),
[quickstart.md](./quickstart.md)

**Tests**: incluidos. No es opcional en este proyecto: la constitución exige prueba o verificación para
toda lógica nueva no trivial, y la investigación asignó qué se prueba con qué en su decisión D-13.

**Organization**: las tareas se agrupan por historia de usuario para que cada una se implemente y se
verifique por separado.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: se puede hacer en paralelo con otras [P] del mismo bloque (archivos distintos, sin
  dependencias entre ellas)
- **[Story]**: a qué historia pertenece (US1 a US6)
- Toda tarea lleva su ruta de archivo exacta

## Path Conventions

Monorepo con dos servicios de Vercel, según la estructura de [plan.md](./plan.md):

- Sitio: `web/`
- API: `api/`
- Configuración del despliegue: `vercel.json` en la raíz

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: dejar el monorepo en pie, con los dos servicios declarados y el sitio bloqueado a
buscadores **antes** del primer despliegue público.

- [x] T001 Crear la estructura de carpetas `web/` y `api/` en la raíz del repositorio, según la
      estructura de `plan.md`
- [x] T002 Declarar el espacio de trabajo `web` y los guiones `dev`, `build`, `test`, `format` en
      `package.json`, conservando `"engines": { "node": "26.x" }`. **Solo `web`**: `api/` es Python y
      no tiene `package.json`, asi que no hay espacio de trabajo de npm que declarar
- [x] T003 [P] Fijar la versión de Python en `.python-version` con el valor `3.12`, que es la versión
      por defecto de la plataforma según `research.md` D-02
- [x] T004 Inicializar el sitio en `web/` con Astro y el adaptador de Vercel, y registrar
      `@tailwindcss/vite` en `vite.plugins` de `web/astro.config.mjs` — **no** la integración
      `@astrojs/tailwind`, que está deprecada (`research.md` D-08)
- [x] T005 Instalar y configurar **Vitest** en el espacio de trabajo `web`, con
      `web/vitest.config.ts` y el guión `test`. Sin esto, las pruebas de las fases 4 y 5 no tienen
      con qué ejecutarse
- [x] T006 Inicializar la API en `api/` con `api/pyproject.toml`: `requires-python = ">=3.12"`,
      dependencia de FastAPI, y `[tool.vercel] entrypoint = "main:app"`
- [x] T007 Añadir **pytest** como dependencia de desarrollo en `api/pyproject.toml` y crear la
      carpeta `api/tests/`
- [x] T008 Declarar los dos servicios y sus reescrituras en `vercel.json`: `web` con raíz `web/`,
      `api` con raíz `api/` y entrypoint `main:app`; reescritura de `/api/(.*)` al servicio `api` y de
      `/(.*)` al servicio `web` (`research.md` D-01)
- [x] T009 Añadir en `vercel.json` la cabecera `X-Robots-Tag: noindex` para **todas** las rutas, y las
      reglas de `Cache-Control` del contrato: `no-store` en `/`, `/admin/*` y `/api/*`
      (`contracts/http.md` §3). Esta tarea va antes del primer despliegue: el sitio no debe llegar
      indexable a internet ni un minuto
- [x] T010 [P] Crear `.env.example` con los siete nombres de variable del contrato —`SUPABASE_URL`,
      `SUPABASE_SERVICE_ROLE_KEY`, `SMTP_USER`, `SMTP_PASSWORD`, `ADMIN_EMAIL`, `SITE_URL`,
      `PUBLIC_CONTACT_EMAIL`— **sin
      ningún valor** (`contracts/http.md` §6)
- [x] T011 [P] Crear `web/src/pages/robots.txt.ts` con `Disallow: /admin` y la declaración del
      sitemap. **Se genera en lugar de vivir en `public/`** para que el dominio salga de `SITE_URL` y
      no quede escrito a mano; si la variable no está puesta, se omite la línea del sitemap

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: lo mínimo que tiene que existir para que haya algo que desplegar y algo que comprobar.

**⚠️ CRÍTICO**: ninguna historia empieza hasta que esta fase esté hecha, y **ninguna salvo la US1
empieza hasta que la US1 pase**.

- [x] T012 Crear la aplicación FastAPI en `api/main.py` con la variable `app` al nivel superior del
      módulo, que es lo que el runtime de Python busca (`research.md` D-02)
- [x] T013 Implementar `GET /api/estado` en `api/main.py`, que devuelve `200` con
      `{ "servicio": "api", "version": "0.1.0" }` y `Cache-Control: no-store`, sin autenticación y sin
      registrar nada (`contracts/http.md` §4)
- [x] T014 Implementar `GET /api/cookie-prueba` en `api/main.py`, que devuelve `204` y
      `Set-Cookie: datafolio_prueba=1; Path=/; HttpOnly; Secure; SameSite=Strict`. Añadir el comentario
      `# atajo: endpoint de verificacion, se borra al terminar la historia P1`
- [x] T015 Crear una página mínima en `web/src/pages/index.astro` que construya sin errores, solo para
      que el servicio del sitio tenga algo que servir en el despliegue de prueba
- [ ] T016 Conectar el repositorio al proyecto de Vercel en el plan gratuito, fijar `main` como su rama de
      producción, y configurar las siete variables de entorno **en la plataforma**, nunca en un archivo
      del repositorio

**Checkpoint**: hay dos servicios declarados y cada uno tiene algo que responder. Se puede desplegar.

---

## Phase 3: User Story 1 - El sitio y su API pueden convivir en un mismo despliegue (Priority: P1) 🎯 MVP

**Goal**: comprobar en producción que las páginas y las funciones de servidor responden bajo un mismo
dominio y que una cookie de origen propio viaja de ida y de vuelta. De esto depende que la
autenticación de la feature 03 sea posible.

**Independent Test**: sobre el despliegue de vista previa de la rama, abrir la página y el endpoint y
comprobar que comparten dominio, y que la cookie que devuelve el endpoint vuelve en la petición
siguiente.

**Esta historia es una puerta, no un incremento.** Si falla, no se sigue: se cambia de plan y se
repite.

- [ ] T017 [US1] Empujar la rama `001-sitio-base` y esperar el despliegue de vista previa que la
      plataforma genera para ella
- [ ] T018 [US1] Verificar que `/` responde la página del sitio bajo el dominio del despliegue
      (`quickstart.md`, historia P1, paso 1)
- [ ] T019 [US1] Verificar que `/api/estado` responde `200` **bajo el mismo dominio**, sin redirección
      a otro host (paso 2)
- [ ] T020 [US1] Verificar que `/api/cookie-prueba` entrega la cookie `datafolio_prueba` con
      `SameSite=Strict` (paso 3)
- [ ] T021 [US1] Verificar que el navegador **devuelve** esa cookie en la petición siguiente a
      `/api/estado`, con `curl -b` o con las herramientas de desarrollo (paso 4). **Este es el paso que
      decide la feature**
- [ ] T022 [US1] Si T021 falla: aplicar el plan B de `research.md` D-01 —funciones Python en una
      carpeta `/api` en la raíz, sin servicios— y repetir T017 a T021. Si vuelve a fallar, aplicar el
      plan C —dos proyectos con una reescritura que haga de proxy— y repetir
- [ ] T023 [US1] Registrar en `research.md` D-01 cuál de los tres planes quedó en pie y qué se observó.
      Un resultado que no se escribe se vuelve a investigar dentro de tres meses

**Checkpoint**: la incógnita está cerrada. A partir de aquí se puede construir sin riesgo de rehacer la
autenticación. **No continuar sin este checkpoint.**

---

## Phase 4: User Story 2 - Un visitante recorre el sitio publicado (Priority: P2)

**Goal**: el esqueleto navegable del portafolio, con sus nueve secciones en dos idiomas, cada una con
dirección propia, utilizable en cualquier pantalla.

**Independent Test**: abrir la dirección pública, visitar cada sección desde el menú en móvil y en
escritorio, y comprobar que cada una tiene dirección propia enlazable.

Esta fase crea los dos archivos que cargan con el principio "un valor, un solo lugar", así que las
historias US3, US4 y US5 se apoyan en ella.

### Tests for User Story 2

> Escribir estas pruebas antes de la implementación y comprobar que fallan.

- [ ] T024 [P] [US2] Prueba en `web/tests/rutas.test.ts`: toda sección del mapa tiene slug **en los dos
      idiomas**; un slug vacío es un error de construcción, no una página sin traducir
      (`data-model.md` §2, regla 1)
- [ ] T025 [P] [US2] Prueba en `web/tests/rutas.test.ts`: dos secciones no comparten slug dentro del
      mismo idioma (`data-model.md` §2, regla 2)
- [ ] T026 [P] [US2] Prueba en `web/tests/rutas.test.ts`: toda sección con `enNavegacion` tiene etiqueta
      en los dos idiomas (`data-model.md` §2, regla 3)

### Implementation for User Story 2

- [ ] T027 [US2] Crear `web/src/styles/tokens.css` como **único** origen de valores visuales: la paleta
      clara en `@theme`, la oscura redefinida bajo el selector del tema oscuro, y las tipografías,
      espaciados, radios y sombras de `docs/design-tokens.md`. Ningún componente escribirá nunca uno de
      estos valores
- [ ] T028 [US2] Crear `web/src/i18n/rutas.ts` con las nueve secciones y sus campos `clave`, `slug.en`,
      `slug.es`, `enNavegacion`, `enIndice`, usando los slugs de `contracts/http.md` §1. Las tres reglas
      de `data-model.md` §2 se validan en construcción
- [ ] T029 [P] [US2] Crear `web/src/i18n/textos.ts` con las cadenas de interfaz en los dos idiomas:
      etiquetas de navegación, del selector de idioma, del botón de tema y de la página de error
- [ ] T030 [US2] Crear `web/src/layouts/Base.astro` con el documento base, la navegación, el pie y los
      enlaces de encabezado, leyendo todo del mapa de rutas (depende de T028, T029)
- [ ] T031 [P] [US2] Crear `web/src/components/Navegacion.astro`, que genera sus enlaces desde el mapa
      de rutas y nunca desde una lista propia
- [ ] T032 [US2] Crear las nueve páginas en inglés bajo `web/src/pages/en/` con los slugs del contrato:
      `index`, `experience`, `projects`, `projects/[slug]`, `blog`, `blog/[slug]`, `contact`,
      `data-policy`
- [ ] T033 [US2] Crear las nueve páginas en español bajo `web/src/pages/es/` con los slugs traducidos
      del contrato: `index`, `experiencia`, `proyectos`, `proyectos/[slug]`, `blog`, `blog/[slug]`,
      `contacto`, `politica-de-datos`
- [ ] T034 [US2] Declarar el modo de entrega de cada ruta según `contracts/http.md` §1 y §3 (FR-028): estáticas el
      inicio, la experiencia, el contacto y la política; servidor con caché de CDN de 60 s el catálogo
      y las fichas de proyecto, el índice del blog y los artículos
- [ ] T035 [US2] Hacer que las cuatro rutas de detalle devuelvan **404** con cualquier identificador
      mientras no exista contenido, en lugar de una página válida y vacía (FR-036). Sirven **la misma
      página de error** que cualquier otra dirección inexistente, con `Cache-Control: no-store`: un 404
      cacheado seguiría sirviéndose cuando la feature 04 publique el primer proyecto. La plantilla de la
      ficha se construye, pero no se sirve hasta que haya algo dentro
- [ ] T036 [US2] Mostrar en cada sección sin contenido su armazón y una indicación visible de que el
      contenido está pendiente. **Sin texto de relleno que simule contenido real** (FR-009)
- [ ] T037 [P] [US2] Crear `web/src/pages/404.astro` **renderizada en servidor**
      (`prerender = false`), que responde estado **404** con `Cache-Control: no-store` y toma el idioma
      del **prefijo de la dirección pedida** —inglés si no hay prefijo—, con salida hacia el inicio.
      Una única página estática solo podría estar en un idioma (`contracts/http.md` §2 bis,
      `research.md` D-07 bis)
- [ ] T038 [US2] Añadir en el pie de `web/src/layouts/Base.astro` un enlace de correo hacia
      `PUBLIC_CONTACT_EMAIL`, presente en todas las páginas. La dirección se lee de la variable de
      entorno, nunca escrita en el código (FR-008)
- [ ] T039 [US2] Hacer el sitio utilizable y legible en móvil, tableta y escritorio sin desbordes
      horizontales, con los puntos de ruptura estándar y comprobado también con el texto ampliado al
      200 %

**Checkpoint**: las doce direcciones fijas responden, las de detalle muestran su armazón con cualquier
identificador, y el sitio se recorre. Ya se puede enseñar.

---

## Phase 5: User Story 3 - El visitante lee el sitio en su idioma (Priority: P3)

**Goal**: cada visitante entra en su idioma, puede cambiarlo cuando quiera, y los buscadores entienden
qué página equivale a qué.

**Independent Test**: abrir el sitio con el navegador en español y luego en otro idioma, comprobar el
destino, cambiar de idioma a mano y verificar que la elección sobrevive a la navegación y a la recarga.

### Tests for User Story 3

- [ ] T040 [P] [US3] Prueba en `web/tests/idioma.test.ts`: la negociación devuelve español con una
      cabecera que pide español, inglés con cualquier otro idioma, e inglés cuando la cabecera está
      **ausente o es ilegible** (`contracts/http.md` §2)
- [ ] T041 [P] [US3] Prueba en `web/tests/rutas.test.ts`: para toda sección, el mapa resuelve su
      página equivalente en el otro idioma, que es lo que sostiene el selector y SC-006

### Implementation for User Story 3

- [ ] T042 [US3] Crear `web/src/i18n/idioma.ts` con la negociación del idioma en el orden de
      `data-model.md` §3: elección guardada, cabecera del navegador si pide español, inglés
- [ ] T043 [US3] Configurar `i18n` en `web/astro.config.mjs` con `defaultLocale: "en"`, los dos locales
      y `prefixDefaultLocale: true`, para que ningún idioma quede en posición privilegiada
      (`research.md` D-06)
- [ ] T044 [US3] Convertir `web/src/pages/index.astro` en la **única** ruta del sitio renderizada en
      servidor (`prerender = false`), que lee el idioma preferido y responde `302` a `/en/` o a `/es/`
      con `Cache-Control: no-store`, sin registrar nada de la petición (`research.md` D-07)
- [ ] T045 [US3] Crear `web/src/components/SelectorIdioma.astro`, que lleva a la **página equivalente**
      en el otro idioma usando el mapa de rutas, nunca al inicio (FR-013)
- [ ] T046 [US3] Comprobar que la elección de idioma se conserva al navegar y al recargar **por la
      propia dirección**, sin guardar nada: no debe existir cookie ni entrada de almacenamiento para el
      idioma. La raíz resuelve por detección en cada visita (FR-014, `research.md` D-06 bis)
- [ ] T047 [US3] Emitir en `web/src/layouts/Base.astro` las cuatro etiquetas de encabezado del contrato:
      `canonical`, `alternate` para cada idioma y `alternate` `x-default` apuntando al inglés, todas
      generadas desde el mapa de rutas (`contracts/http.md` §3)
- [ ] T048 [US3] Crear `web/src/pages/sitemap.xml.ts`, que genera el índice desde el mapa de rutas
      incluyendo los dos idiomas y excluyendo las secciones con `enIndice` en falso

**Checkpoint**: el sitio es bilingüe de verdad, con direcciones traducidas y equivalencias declaradas.

---

## Phase 6: User Story 4 - El visitante elige cómo se ve el sitio (Priority: P4)

**Goal**: tema claro y oscuro, con la preferencia del dispositivo por defecto, un botón siempre a mano y
ningún destello al cargar.

**Independent Test**: abrir el sitio con el sistema en claro y luego en oscuro, alternar con el botón,
recargar con red lenta simulada y comprobar que no hay destello del tema contrario.

- [ ] T049 [US4] Añadir en el encabezado de `web/src/layouts/Base.astro` un script **en línea y
      bloqueante**, antes de cualquier CSS, que lee la preferencia guardada o la del sistema y escribe
      `data-theme` en `<html>`, con el acceso al almacenamiento en `try`/`catch`. En línea y bloqueante
      no es un detalle: cualquier otra forma corre después del primer pintado, que es cuando el destello
      ya ocurrió (`research.md` D-09)
- [ ] T050 [US4] Crear `web/src/components/BotonTema.astro`, flotante en la esquina inferior derecha,
      disponible en todas las páginas, que solo cambia el atributo `data-theme` y guarda la elección
- [ ] T051 [US4] Verificar que el cambio de tema es inmediato o con una transición de **150 ms como
      máximo**, y que no hay ninguna animación (FR-023)
- [ ] T052 [US4] Comprobar el contraste de texto y de bordes de control en los dos temas contra
      `docs/design-tokens.md`, revisando una por una sus tres reglas no negociables
- [ ] T053 [US4] Prueba del archivo único: cambiar un color en `web/src/styles/tokens.css`, desplegar,
      comprobar que el cambio se ve en todas las secciones **sin haber tocado ningún componente**, y
      revertir. Es el criterio de aceptación del principio "un valor, un solo lugar" (SC-008)

**Checkpoint**: el sitio respeta la preferencia de quien entra y la suya propia, sin fogonazos.

---

## Phase 7: User Story 5 - El sitio se puede usar solo con el teclado (Priority: P5)

**Goal**: todo el sitio recorrible y operable sin ratón, con el foco siempre visible.

**Independent Test**: recorrer el sitio entero con tabulador y entrada, comprobando que se alcanza todo
elemento interactivo y que siempre se ve dónde está el foco.

- [ ] T054 [US5] Asegurar que todo elemento interactivo es alcanzable y operable con el teclado en un
      orden que sigue el orden visual, usando elementos nativos en lugar de contenedores con
      comportamiento añadido (FR-024)
- [ ] T055 [US5] Definir en `web/src/styles/tokens.css` un indicador de foco visible y comprobarlo en
      los **dos** temas (FR-025)
- [ ] T056 [US5] Hacer que el menú de navegación en móvil se abra, se recorra y se cierre con teclado,
      y que el foco **no quede atrapado** dentro de él
- [ ] T057 [P] [US5] Dar texto alternativo en el idioma de la página a toda imagen con contenido, y
      marcar las decorativas para que un lector de pantalla las omita (FR-026)
- [ ] T058 [US5] Comprobar que con la preferencia de movimiento reducido activada no hay ninguna
      diferencia perceptible, porque no hay animaciones

**Checkpoint**: el compromiso de accesibilidad del proyecto se cumple en el esqueleto, que es donde
cuesta diez veces menos que después.

---

## Phase 8: User Story 6 - El sitio se mantiene en pie sin vigilancia (Priority: P6)

**Goal**: el servicio de datos no se suspende por inactividad, y si la comprobación falla, el titular se
entera por correo.

**Independent Test**: comprobar que la tarea queda registrada con su intervalo de seis horas y que su
última ejecución consta como correcta; después, provocar un fallo y comprobar que llega el aviso.

### Tests for User Story 6

- [ ] T059 [P] [US6] Prueba en `api/tests/test_salud.py`: una escritura correcta deja `resultado` en
      `correcto` y `detalle` nulo; un fallo deja `resultado` en `fallido` con la causa en `detalle`
- [ ] T060 [P] [US6] Prueba en `api/tests/test_salud.py`: cuando la escritura falla **y** el envío del
      correo también falla, la función no se rompe y el fallo original se propaga al registro

### Implementation for User Story 6

- [ ] T061 [US6] Crear el proyecto de Supabase en el plan gratuito y guardar `SUPABASE_URL` y
      `SUPABASE_SERVICE_ROLE_KEY` en las variables de entorno de Vercel. La clave **solo** la lee el
      servicio de la API
- [ ] T062 [US6] Crear la migración de la tabla `salud` con exactamente estos campos y restricciones
      (`data-model.md` §1): `id smallint` clave primaria fijo en `1` con `CHECK (id = 1)` para impedir
      una segunda fila; `comprobado_en timestamptz` **nunca nulo**; `resultado text` **nunca nulo**, con
      valores `correcto` o `fallido`; `detalle text` nulo cuando el resultado es `correcto`. La tabla
      **no** se expone a lectura anónima
- [ ] T063 [US6] Insertar la fila única inicial con `id = 1`, `resultado = 'correcto'` y la fecha de
      creación. A partir de ahí la fila solo se actualiza, nunca se borra
- [ ] T064 [P] [US6] Crear `api/correo.py` con el envío por SMTP usando `smtplib` y `email.message` de
      la biblioteca estándar, al puerto **587** con **STARTTLS**, **esperando** a que el envío termine
      antes de devolver. Sin dependencias nuevas (`research.md` D-11, y la restricción de la
      constitución)
- [ ] T065 [US6] Crear `api/salud.py`: escribe la fila de `salud` con `urllib.request` contra el
      endpoint REST del proyecto de datos; si falla, envía el correo de aviso a `ADMIN_EMAIL` con la
      causa; si el correo también falla, deja el fallo original en el registro de la plataforma
      (`contracts/http.md` §5)
- [ ] T066 [US6] Declarar en `vercel.json` una tarea programada de **Vercel Schedules** con destino
      **función privada** —sin URL pública— que ejecute `api/salud.py` **cada seis horas**
      (`research.md` D-03, D-04)
- [ ] T067 [US6] Verificar en el panel que la tarea está registrada con su intervalo y que su historial
      muestra al menos una ejecución correcta, y que la fila de `salud` tiene esa fecha
- [ ] T068 [US6] Provocar un fallo: invalidar temporalmente la clave de la base en las variables de
      entorno, disparar la tarea a mano, comprobar que llega el correo con la causa, y **restaurar la
      clave**

**Checkpoint**: el sitio sobrevive a semanas sin visitas, y sus fallos se avisan solos.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: cerrar la feature, quitar los andamios y pasar las puertas de calidad.

- [ ] T069 **Eliminar** `GET /api/cookie-prueba` de `api/main.py`. Era un andamio de la historia US1 y
      su borrado es un punto de la Definición de hecho, no un recordatorio
- [ ] T070 [P] Ejecutar la verificación completa de `quickstart.md`, historia por historia, marcando
      cada casilla
- [ ] T071 Pasar la puerta de rendimiento con PageSpeed Insights sobre la dirección pública, perfil de
      móvil, **mediana de tres ejecuciones**: contenido principal por debajo de 2,5 s, desplazamiento
      involuntario por debajo de 0,1, menos de 100 KB de JavaScript por página (`research.md` D-14). Un
      resultado fuera de presupuesto se revisa, no se promedia hasta que pase
- [ ] T072 [P] Comprobar que `npm test` y `pytest` pasan, y que el gancho de pre-commit no encuentra
      ningún secreto
- [ ] T073 [P] Verificar que la cabecera `X-Robots-Tag: noindex` sigue puesta en todas las rutas y
      anotar en la spec de la feature 02 que levantarla es tarea suya
- [ ] T074 Comprobar SC-010 **ocho días después de integrar**: abrir el sitio tras una semana sin
      visitas y verificar que responde con normalidad y que el historial de la tarea programada no tiene
      fallos. Es el único criterio de la feature que necesita que pase el tiempo
- [ ] T075 Integrar la rama a `main` y comprobar el sitio en producción. Según la constitución 1.5.0,
      el código solo entra cuando cumple la Definición de hecho y se ha revisado en la vista previa.
      Comprobar además en el panel de las dos plataformas que el consumo del mes es cero (SC-011)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (fase 1)**: sin dependencias.
- **Foundational (fase 2)**: depende de la fase 1. Bloquea todo lo demás.
- **US1 (fase 3)**: depende de la fase 2. **Bloquea todas las demás historias**, y esto es una
  excepción al patrón habitual: US1 no es un incremento sino una puerta. Si su resultado obliga al plan
  B o al C, cambia la estructura del despliegue, y construir antes de saberlo sería trabajo a rehacer.
- **US2 (fase 4)**: depende de US1. Crea el mapa de rutas, los tokens y la plantilla base, de los que
  dependen US3, US4 y US5.
- **US3 (fase 5)**, **US4 (fase 6)**, **US5 (fase 7)**: dependen de US2. Entre ellas son independientes.
- **US6 (fase 8)**: depende solo de la fase 2. No toca el sitio, así que puede ir en paralelo a US2 en
  adelante.
- **Polish (fase 9)**: depende de que estén todas.

### User Story Dependencies

```text
Setup → Foundational → US1 (puerta)
                        ├── US2 → US3
                        │      ├── US4
                        │      └── US5
                        └── US6
```

### Within Each User Story

- Las pruebas se escriben antes y se comprueba que fallan.
- El mapa de rutas y los textos antes de la plantilla; la plantilla antes de las páginas.
- La tabla antes de la función que escribe en ella; la función antes de la tarea programada.
- Una historia se termina antes de pasar a la siguiente prioridad.

### Parallel Opportunities

- Fase 1: T003, T010 y T011 en paralelo.
- Fase 4: las tres pruebas T024 a T026 en paralelo; después T029, T031 y T037 en paralelo.
- Fase 5: T040 y T041 en paralelo.
- Fase 8: T059 y T060 en paralelo; T064 en paralelo con la migración.
- **US6 completa en paralelo con US2, US3, US4 y US5**: no comparte ningún archivo con el sitio.
- Fase 9: T070, T072 y T073 en paralelo.

---

## Parallel Example: User Story 2

```bash
# Las tres pruebas del mapa de rutas, juntas:
Tarea: "Prueba de slugs en los dos idiomas en web/tests/rutas.test.ts"
Tarea: "Prueba de slugs no duplicados en web/tests/rutas.test.ts"
Tarea: "Prueba de etiquetas de navegación en web/tests/rutas.test.ts"

# Tras el mapa y la plantilla, tres archivos sin relación entre sí:
Tarea: "Crear web/src/i18n/textos.ts"
Tarea: "Crear web/src/components/Navegacion.astro"
Tarea: "Crear web/src/pages/404.astro"
```

---

## Implementation Strategy

### Primero la puerta, no el MVP

Lo habitual es entregar la historia P1 como producto mínimo. Aquí no: la US1 no entrega nada que se
pueda enseñar, entrega una **respuesta**. El orden es fases 1 y 2, luego US1, y solo entonces se decide
si lo que sigue se construye sobre servicios, sobre una carpeta `/api` o sobre dos proyectos.

El primer incremento enseñable es la **US2**: el sitio recorrible en dos idiomas.

### Entrega incremental

1. Fases 1 y 2 → hay algo que desplegar.
2. US1 → **puerta**. La incógnita queda cerrada y registrada.
3. US2 → el esqueleto navegable. Primer momento en que esto se puede mostrar a alguien.
4. US3 → bilingüe de verdad, con direcciones traducidas.
5. US4 → claro y oscuro.
6. US5 → operable sin ratón.
7. US6 → se mantiene solo. Puede ir en paralelo desde el punto 2.
8. Fase 9 → se quitan los andamios y se pasa la puerta de rendimiento.

### Una sola persona

Este proyecto lo mantiene una persona en ratos libres, así que el paralelismo real es poco. Lo que sí
conviene aprovechar: **US6 no toca ni un archivo del sitio**, así que es lo que se hace cuando apetezca
Python en vez de CSS.

---

## Notes

- Las tareas marcadas [P] tocan archivos distintos y no dependen entre sí.
- Commit por tarea o por grupo lógico, con el formato de la constitución:
  `vX.Y.Z-AAAA-MM-DD-tipo: descripción`.
- En cualquier checkpoint se puede parar y verificar la historia por separado.
- Los dos archivos a vigilar en revisión son `web/src/styles/tokens.css` y `web/src/i18n/rutas.ts`: si
  un color o un slug aparece fuera de ellos, es un defecto, no una excepción.
- Lo que esta feature **no** construye está listado en `data-model.md`. Si una tarea parece pedir un
  usuario, un proyecto, un artículo o un evento de analítica, está mal entendida.

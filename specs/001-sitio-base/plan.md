# Implementation Plan: Sitio base

**Branch**: `001-sitio-base` | **Date**: 2026-11-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-sitio-base/spec.md`

## Summary

Esta feature levanta el esqueleto del portafolio y, antes que nada, despeja la única incógnita capaz
de obligar a rehacer trabajo: que el sitio y su API respondan bajo un mismo dominio, porque de eso
depende que la sesión del administrador funcione. Se resuelve con **Vercel Services**, que es el
mecanismo documentado para desplegar un frontend y un backend de Python como un solo proyecto con un
solo dominio, y está disponible en el plan gratuito.

Sobre eso se construye lo estructural, que es lo que cuesta diez veces más si se deja para después:
el enrutado bilingüe con slugs traducidos salidos de un mapa único, el archivo único de tokens
visuales, el tema claro y oscuro aplicado antes del primer pintado, la navegación por teclado, y la
comprobación programada que impide que la base de datos del plan gratuito se suspenda por inactividad.
El sitio queda publicado y bloqueado a buscadores hasta que tenga contenido real.

El detalle de cada decisión técnica, con su fuente y sus alternativas descartadas, está en
[research.md](./research.md).

## Technical Context

**Language/Version**: TypeScript sobre Node **26.x** en el sitio; **Python 3.12** en la API

**Primary Dependencies**: Astro (islas, modo híbrido), Tailwind CSS vía `@tailwindcss/vite`, FastAPI.
Nada más. El envío de correo y la consulta a la base se hacen con la biblioteca estándar de Python
(`smtplib`, `urllib.request`)

**Storage**: Supabase (PostgreSQL), proyecto único de producción, creado en esta feature con **una sola
tabla**: `salud`, de la propia comprobación programada. Sin esquema de aplicación

**Testing**: **Vitest** para el mapa de rutas y la negociación de idioma; **pytest** para la lógica de
la comprobación y del aviso; verificación manual sobre el sitio desplegado para teclado, contraste,
ausencia de destello y comportamiento responsive

**Target Platform**: Vercel, plan gratuito, un único proyecto con dos servicios. Navegadores modernos
de móvil, tableta y escritorio

**Project Type**: Sitio web estático con islas interactivas, más una API de servidor en el mismo
despliegue. Monorepo

**Performance Goals**: LCP por debajo de 2,5 s y desplazamiento involuntario por debajo de 0,1 en móvil;
menos de 100 KB de JavaScript por página pública. Medido con PageSpeed Insights sobre el sitio
desplegado, perfil de móvil, mediana de tres ejecuciones

**Constraints**: Coste cero. Sin estado en memoria: la API corre sin servidor. Sin animaciones;
transiciones de 150 ms como máximo. Ningún secreto en el repositorio, que es público. Nada del
visitante se almacena

**Scale/Scope**: Doce direcciones fijas y cuatro de detalle —seis más dos secciones en dos idiomas—, un
único usuario
administrador que aún no existe, tráfico de portafolio personal. Una tarea programada

## Constitution Check

_GATE: debe pasar antes de la Fase 0. Reevaluado tras la Fase 1._

Verificado contra la constitución **1.4.0**.

| Principio                                  | Cómo lo cumple este plan                                                                                                                                                                                                                                                                                                  | Veredicto |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **I. Especificación antes que código**     | La spec está aprobada y clarificada, con cero marcadores abiertos. Las dos dudas que la investigación destapó —la frecuencia de la comprobación y la tabla que necesita— se corrigen **en la spec**, no se resuelven en silencio durante la implementación.                                                               | Pasa      |
| **II. Un valor, un solo lugar**            | Los tokens visuales en `web/src/styles/tokens.css` y en ningún otro sitio. Los slugs de las dos lenguas en `web/src/i18n/rutas.ts`, de donde salen los enlaces, el selector de idioma, las etiquetas `canonical`/`hreflang` y el índice para buscadores. Las direcciones de correo y las claves, en variables de entorno. | Pasa      |
| **III. El servidor es la única autoridad** | En esta feature no hay ninguna escritura pública. La comprobación programada es una **función privada sin URL pública**, y la clave de la base vive solo en el servicio de la API; el sitio nunca habla con la base de datos.                                                                                             | Pasa      |
| **IV. Del visitante no se guarda nada**    | No hay analítica en esta feature. El idioma y el tema se guardan en el navegador del visitante y nunca se envían. La raíz lee la cabecera de idioma para redirigir y no la almacena.                                                                                                                                      | Pasa      |
| **V. Lo mínimo que cumple, terminado**     | Cero dependencias añadidas para el correo y la consulta a la base. Sin navegador automatizado, sin abstracciones sobre Astro ni sobre FastAPI, sin componentes que nadie pidió. Las secciones sin contenido muestran su armazón, no relleno.                                                                              | Pasa      |

**Restricciones técnicas y de producto**

| Restricción                                                      | Estado                                                                                                                                                       |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pila fija: Astro + Tailwind, FastAPI, Supabase, monorepo, Vercel | Respetada tal cual                                                                                                                                           |
| Coste cero                                                       | Services está disponible en todos los planes; Schedules admite el intervalo elegido en el plan gratuito; Supabase gratuito; correo desde una cuenta de Gmail |
| Sin estado en memoria                                            | La comprobación escribe en la base. Esta feature no tiene límite de tasa ni caché que guardar                                                                |
| Bilingüe o no se publica                                         | No aplica todavía —no hay contenido administrable—, pero el enrutado nace exigiendo las dos lenguas                                                          |
| Presupuesto de rendimiento                                       | Páginas estáticas, sin framework en el cliente. Lo único que se envía es el script de tema en línea y el menú móvil. Muy por debajo de 100 KB                |
| Accesibilidad                                                    | Teclado y foco visible son la historia P5, no un añadido. Las reglas de contraste de los tokens son criterio de aceptación                                   |
| Sin animaciones                                                  | Ninguna. Los cambios de tema son inmediatos                                                                                                                  |
| Datos de prueba fuera de producción                              | No hay datos de aplicación que inventar en esta feature                                                                                                      |

**Puertas de calidad**

- Las pruebas exigidas por la constitución para esta feature son las de la lógica nueva no trivial:
  mapa de rutas, negociación de idioma, y la lógica de la comprobación y su aviso. Están asignadas en
  la tabla D-13 de la investigación.
- La rama integra sus **documentos** a `main` en cuanto están terminados, y su **código** solo cuando
  cumple la Definición de hecho y se ha revisado en el despliegue de vista previa.

**Sin violaciones que justificar.** La sección de Complejidad queda vacía a propósito.

**Reevaluación tras la Fase 1**: el diseño no introdujo ninguna violación. Los dos artefactos que
podían introducirla —la tabla de la comprobación y el endpoint temporal de verificación de la cookie—
se declararon con su límite por escrito: la tabla es de una fila y no guarda historial, y el endpoint
se elimina al cerrar la feature, lo que figura como punto de la Definición de hecho en
[quickstart.md](./quickstart.md). La investigación obligó además a corregir dos suposiciones de la
spec, y se corrigieron **en la spec** antes de escribir este plan, en lugar de absorberlas aquí.

## Project Structure

### Documentation (this feature)

```text
specs/001-sitio-base/
├── plan.md              # Este archivo
├── research.md          # Fase 0: catorce decisiones con su fuente
├── data-model.md        # Fase 1: la tabla de salud y el mapa de rutas
├── quickstart.md        # Fase 1: cómo se verifica cada historia
├── contracts/
│   └── http.md          # Fase 1: la superficie pública del despliegue
├── checklists/
│   └── requirements.md  # Calidad de la spec: 16/16
└── tasks.md             # Fase 2: lo genera /speckit-tasks, no este comando
```

### Source Code (repository root)

```text
vercel.json              # Los dos servicios, las reescrituras, las cabeceras y la tarea programada
package.json             # Node 26.x, formato y pruebas del sitio
.python-version          # 3.12

web/                     # Servicio del sitio
├── astro.config.mjs     # Plugin de Tailwind, i18n con prefijo en ambos idiomas, adaptador de Vercel
├── src/
│   ├── styles/
│   │   └── tokens.css   # ÚNICO origen de color, tipografía, espaciado, radios y sombras
│   ├── i18n/
│   │   ├── rutas.ts     # ÚNICO origen de los slugs de las nueve secciones en los dos idiomas
│   │   ├── idioma.ts    # Negociación del idioma del visitante
│   │   └── textos.ts    # Cadenas de la interfaz en los dos idiomas
│   ├── layouts/
│   │   └── Base.astro   # Script de tema en línea, canonical, hreflang, x-default, navegación, pie
│   ├── components/
│   │   ├── Navegacion.astro
│   │   ├── BotonTema.astro        # Flotante, abajo a la derecha
│   │   └── SelectorIdioma.astro   # Lleva a la página equivalente, no al inicio
│   └── pages/
│       ├── index.astro            # Ruta en servidor: redirige por idioma
│       ├── 404.astro              # Ruta en servidor: idioma del prefijo pedido, estado 404
│       ├── sitemap.xml.ts         # Generado desde rutas.ts
│       ├── en/                    # home, experience, projects, project, blog, post,
│       └── es/                    # contact, data-policy — con los slugs ya traducidos
└── public/
    └── robots.txt

api/                     # Servicio de la API
├── main.py              # FastAPI: `app` al nivel superior
├── salud.py             # Comprobación programada: escribe en la base y avisa si falla
├── correo.py            # Envío por SMTP con la biblioteca estándar
├── pyproject.toml       # Python 3.12, FastAPI, entrypoint main:app
└── tests/
    └── test_salud.py

web/tests/               # Vitest: rutas e idioma
```

**Structure Decision**: monorepo con dos servicios de Vercel, `web/` y `api/`, declarados en el
`vercel.json` de la raíz. Cada uno se construye por separado, con su propio framework y sus propias
dependencias, y los dos responden bajo el mismo dominio gracias a las reescrituras de nivel superior.
Es la estructura que la constitución ya fijaba —monorepo, carpetas separadas— y la que Vercel
documenta para un monorepo políglota.

Dos archivos cargan con el peso del principio "un valor, un solo lugar", y conviene nombrarlos aquí
porque son los que hay que vigilar en revisión: `web/src/styles/tokens.css` y `web/src/i18n/rutas.ts`.
Si un valor de color o un slug aparece fuera de ellos, es un defecto.

## Complexity Tracking

> Sin violaciones de la constitución. Nada que justificar.

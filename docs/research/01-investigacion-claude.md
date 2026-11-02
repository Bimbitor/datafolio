# Portafolio web de datos para Data Engineer híbrido: guía 2026 con Astro, AWS e IA

> Investigación realizada con Claude (Advanced Research) el 2026-11-01.
> Documento de referencia. Las decisiones vinculantes viven en `specs/`; si algo aquí contradice una spec, manda la spec.

# Cómo construir tu portafolio web de datos a finales de 2026: guía para Javi (Data Engineer híbrido DS+DE, AWS/Airflow/Spark, construyendo con IA)

**Respuesta corta:** construye un sitio estático con **Astro + Tailwind + MDX**, bilingüe (español/inglés), que funcione como índice de **3 proyectos insignia en formato de caso de estudio**. El sitio es la vitrina: lo que te contrata son los proyectos y sus repos. Empieza publicándolo gratis en GitHub Pages o Cloudflare Pages y, como uno de tus casos de estudio, **muévelo después a S3 + CloudFront con Terraform y GitHub Actions**. Así el propio hosting también demuestra AWS. Tu diferenciador no debe ser el diseño. Debe ser que el portafolio sea en sí un producto de datos, alimentado por un pipeline real y con el uso de IA documentado de forma verificable.

## TL;DR

- **Lo que pesa:** 2–3 proyectos realistas y bien documentados, con problema de negocio, arquitectura, decisiones y métricas, enlazados a repos impecables. Diseño llamativo, barras de "nivel de skill" y proyectos tipo Titanic/Iris no suman, e incluso restan. El sitio solo hace de puerta de entrada.
- **Stack recomendado:** Astro (contenido en Markdown/MDX, cero JavaScript por defecto, i18n nativo) + Tailwind + Mermaid/Excalidraw. Hosting gratis en GitHub Pages o Cloudflare Pages desde el día 1. Luego se migra a S3 + CloudFront (plan *flat-rate* gratuito) con Terraform y CI/CD en GitHub Actions como proyecto de AWS. Evita Vercel Hobby si algún día vas a monetizar.
- **Posicionamiento:** "Data Engineer que también entiende modelos". Un proyecto insignia de punta a punta en el sector turismo/viajes, con datos abiertos de Aerocivil, Airflow, Spark, AWS, un modelo de pronóstico y una capa LLM/RAG evaluada. Todo con un `AI_USAGE.md` que cuente qué hizo la IA y qué hiciste tú. Sitio en ES/EN, modo oscuro, foto real opcional pero recomendable.

---

## Key Findings

### 1. Cómo construyen hoy sus portafolios los perfiles de datos

**Hay tres patrones dominantes:**

1. **"Repo-portafolio" en GitHub.** Es el formato más común entre juniors y personas en transición. Es un README índice con tabla de proyectos, stack y enlaces, a menudo con diagramas Mermaid incrustados.
   - Canyon White (github.com/canyonwhite/data-engineer-portfolio) organiza cinco proyectos en estados *in progress* / *planned* y dibuja cada arquitectura con Mermaid (p. ej., "AWS S3 raw files and manifests", "Airflow orchestration").
   - Douglas Merelo (dmerelo.github.io/data-engineering-portfolio) se centra en un proyecto insignia: "AWS Incremental Data Pipeline" con PySpark estilo Glue, Airflow, watermark, idempotencia y reprocesamiento.
   - Vedanth Baliga (github.com/vedanthv/data-engineering-portfolio) usa una tabla índice por tecnología y dominio.
2. **Sitio personal + blog técnico.** Es el patrón de los perfiles más visibles del sector:
   - Mehdi Ouazza (mehdio.com, Next.js): página de proyectos con etiquetas de tecnología y estrellas de GitHub.
   - Simon Späti (ssp.sh, Hugo): blog y un "segundo cerebro" de más de 1.000 notas en un grafo interactivo.
   - Eugene Yan (eugeneyan.com): sección de prototipos con una línea, fecha y enlaces a código y demo.
   - Hamel Husain (hamel.dev, Quarto en GitHub Pages): página de open source con su rol en cada proyecto.
3. **Sitio-caso de estudio para juniors.** Es tu categoría.
   - Shaun Lin (shaundataanalytics.github.io, Next.js): dibuja cada pipeline etapa por etapa con "tiles" de métricas y una línea de tiempo en lugar de CV.
   - Samuel Tseng (samueltyh.github.io, Jekyll Chirpy): posts tipo "Airflow + dbt pipeline" con reto, arquitectura y decisiones.
   - Deshraj Jogiya (deshraj-jogiya.github.io, Python + Jinja2 propio): botón "Recruiter Tour", un asistente de IA que responde sobre su experiencia y el CV visible dentro de la página.

Estos ejemplos vienen de la recopilación "24 Best Data Science Portfolio Examples 2026" de Colorlib (un vendedor de plantillas, así que tómala como curaduría y no como consenso de comunidad). Los nombres de Ouazza, Späti, Yan y Husain sí son referentes reconocidos.

**Qué dicen quienes contratan (y en qué no coinciden):**

- **Data Engineer Academy (Chris Garzon, enero 2026).** Recomienda **2–3 proyectos realistas** con Airflow, Spark, dbt y nube, y avisa que los reclutadores "no se impresionan con proyectos genéricos de libro de texto" como **Titanic**. "Un proyecto profundo y bien documentado que imita un pipeline real vale más que cinco demos superficiales." También afirma que menos de 1 de cada 10 juniors incluye portafolio, pero lo presenta como "observación de la industria" sin dato verificable. Además, es una academia que vende cursos.
- **Hacker News** muestra el matiz real. El usuario bradlys lo resume en el hilo "Ask HN: Did you personal website help you get hired?": "the projects got me hired but the portfolio website itself didn't" ("los proyectos me consiguieron el trabajo, el sitio en sí no"). Otro: "el contenido de los proyectos es un orden de magnitud más importante que el diseño del sitio, salvo que busques roles de frontend". Otros cuentan que entrevistadores abandonaron su guion para preguntar por proyectos del portafolio, o que un post técnico en portada de HN les trajo reclutadores.
- **Conclusión para ti:** el sitio no es lo que te contrata. Sirve para que un reclutador entienda en 60 segundos quién eres y llegue al mejor proyecto en dos clics. Invierte más o menos el 20% del esfuerzo en el sitio y el 80% en los proyectos y su documentación.

**Qué hacen los juniors en tu posición (y el error típico):** los repos-portafolio de cursos (Udacity "Sparkify", "Twitter data pipeline with Airflow", "YouTube data analysis") son tan repetidos que ya no diferencian. Si haces uno de esos, debe ser apenas un ejercicio. Tus proyectos insignia tienen que salir de un dominio que conoces: **viajes corporativos**.

### 2. Secciones que aportan valor vs. relleno

| Sección | Valor | Por qué |
|---|---|---|
| Hero con propuesta de valor en una frase + CTA a proyecto insignia y CV | **Alto** | El reclutador decide en segundos. Ej.: "Data Engineer (AWS · Airflow · Spark) con base en ciencia de datos. Construyo pipelines que terminan en modelos y decisiones." |
| Proyectos destacados (3) en formato caso de estudio | **Crítico** | Es lo que se evalúa y lo que se pregunta en entrevista. |
| CV descargable (PDF, ES y EN) | **Alto** | Muchos procesos lo exigen. Que sea idéntico en contenido al sitio. |
| Sobre mí (breve, con foto) | **Medio** | Contexto humano: transición desde SQL Server/SSIS, estudios nocturnos, Bogotá, disponibilidad remota. |
| Blog / notas técnicas | **Medio-alto** | Es el canal que en HN más se asocia a contactos entrantes de reclutadores. Demuestra comunicación escrita en inglés. |
| "Cómo construyo con IA" / Lab | **Medio-alto (para ti)** | Diferenciador si es verificable (ver §7). |
| Now page / changelog | **Bajo-medio** | Señal de actividad. Barata de mantener. |
| Contacto (email + LinkedIn + GitHub) | **Alto** | Sin fricción, sin formularios innecesarios. |
| Barras o porcentajes de "nivel" en skills | **Relleno/negativo** | No significan nada y en entrevista se vuelven en tu contra. Usa una lista de stack agrupada y enlazada a dónde la usaste. |
| Galería de 15 notebooks de cursos | **Negativo** | Diluye a los 3 buenos. |
| Testimonios genéricos, contadores animados, carruseles | **Relleno** | Distraen y pesan. |
| Logos de certificaciones sin contexto | **Bajo** | Mejor una línea en el CV y en LinkedIn. En el sitio, solo si son AWS relevantes. |

**Cómo se interconectan:** cada caso de estudio enlaza a su repo, demo, post del blog que lo explica y la sección del CV donde aparece. Cada repo enlaza de vuelta al caso de estudio en el sitio. El README de perfil de GitHub apunta al sitio y a los 3 repos fijados. LinkedIn (sección "Destacados") enlaza al sitio y al proyecto insignia. Los posts del blog terminan con "Ver el proyecto completo →". El objetivo es que cualquier punto de entrada (LinkedIn, GitHub, Google, un post) lleve al proyecto insignia en dos clics como máximo.

### 3. Arquitectura del sitio propuesta (mapa de secciones)

```
/ (es)  ·  /en/ (inglés)
├── Inicio
│   ├── Hero: titular + 3 badges de stack + [Ver proyecto insignia] [Descargar CV]
│   ├── 3 proyectos destacados (tarjetas con diagrama miniatura + métrica clave)
│   ├── "Métricas en vivo" (widget alimentado por tu propio pipeline, §6)
│   └── Últimos 3 posts
├── /proyectos
│   ├── filtros por tipo: Pipelines · ML/Modelos · Analytics/BI · IA/LLM
│   └── /proyectos/[slug]  ← plantilla de caso de estudio (§ Plantilla)
├── /blog  (MDX; RSS; etiquetas)
├── /lab   (experimentos pequeños, prototipos, notebooks, "cómo construyo con IA")
├── /sobre-mi  (historia, foto, stack, certificaciones, idiomas)
├── /cv  (HTML + PDF ES/EN)
├── /now  (en qué estoy ahora; fecha de actualización)
└── /changelog (generado desde commits/releases)
```

**Cómo mostrar proyectos sin interfaz visual (backend/datos):**

- **Diagrama de arquitectura** como pieza central. Usa Mermaid en el MDX (se renderiza también en GitHub) o Excalidraw/draw.io exportado a SVG.
- **Captura del grafo del DAG en Airflow** y de la vista Gantt de una ejecución real, con duración y reintentos.
- **"Evidencia de ejecución":** logs resumidos, tabla de *data quality checks* pasados/fallados, tiempos de Spark antes y después de una optimización.
- **Documentación navegable:** si usas dbt, publica el sitio estático de `dbt docs` (linaje incluido) en GitHub Pages y enlázalo.
- **Notebooks:** Quarto o nbconvert los renderiza a HTML para incrustarlos o enlazarlos. No obligues al reclutador a abrir Jupyter.
- **Demo interactiva:**
  - Streamlit Community Cloud sigue siendo gratis. Según la documentación oficial de Streamlit, las apps duermen tras 12 horas sin tráfico y la memoria va de 690 MB mínimo a 2,7 GB máximo.
  - **Ojo con Hugging Face Spaces:** la documentación oficial (Spaces Overview) dice ahora que "Gradio and Docker Spaces run on compute and require a paid plan to create" (PRO para cuentas personales). Los *Static Spaces* siguen gratis y las cuentas gratuitas pueden tener hasta 2 Spaces de Gradio en ZeroGPU. Varios blogs que aún dicen "CPU Basic es gratis" están desactualizados.
- **Video de 2 minutos** (Loom o similar) recorriendo la ejecución. Hiring managers de IA lo recomiendan explícitamente.

### 4. Stack técnico: recomendación y comparación

**Recomendación: Astro (v6/v7) + Tailwind CSS v4 + Content Collections en Markdown/MDX + Mermaid + i18n nativo.**

| Opción | Pros | Contras | Veredicto para Javi |
|---|---|---|---|
| **Astro** | Cero JavaScript por defecto ("islands"), ideal para contenido. MDX nativo. i18n en el router. Cientos de plantillas (Starfolio, Astro Nano, AstroPaper, Dante, Astro TUI Portfolio). Exporta archivos estáticos a cualquier host. | Curva de JS/TS ligera. | **Elegido.** Equilibrio entre mantenimiento bajo y libertad para piezas interactivas (gráficos, widget de métricas). |
| **Quarto** | Nativo para ciencia de datos: renderiza `.ipynb`/`.qmd`, ecuaciones y gráficos de Python. Publica a GitHub Pages en una línea. Lo usan Hamel Husain y muchos estudiantes. | Diseño más "académico". Menos flexible para un sitio de marca personal. i18n más artesanal. | Excelente **complemento**: úsalo para notebooks/reportes dentro de los repos y enlázalos. |
| **Hugo** | El más rápido compilando. Sin dependencias de Node. | Plantillas Go poco amigables. Sin modelo de componentes (difícil incrustar gráficos interactivos). | Bueno si solo quieres blog. |
| **Next.js** | Máxima potencia y ecosistema React/shadcn. | Envía unos 80 KB+ de runtime aunque la página sea texto. Más mantenimiento. Su hogar natural (Vercel Hobby) es solo no comercial. | Exceso para un portafolio. |
| **Jekyll** | Integración histórica con GitHub Pages (tema Chirpy). | Ruby, ecosistema estancado. | Solo si quieres cero configuración. |
| **MkDocs/Docusaurus/Starlight** | Excelentes para documentación. | No son sitios de marca personal. | Úsalos para docs de un proyecto grande, no para el portafolio. |
| **Gatsby** | — | Pierde mantenimiento y comunidad; compila lento. | Evitar. |

**Piezas del stack:**

- **Estilos:** Tailwind v4. shadcn/ui solo si añades islas React. Para un sitio de contenido bastan componentes Astro propios.
- **Diagramas:** Mermaid para flujos y DAGs (versionables como texto). Excalidraw para el diagrama "hero" de cada proyecto. Iconos oficiales de AWS en draw.io si quieres un look de arquitectura cloud.
- **Visualizaciones interactivas:** Observable Plot, ECharts o Vega-Lite como isla Astro. Lee JSON generado por tu pipeline.
- **Plantilla de partida:** Starfolio (Astro v6), que concentra bio, proyectos y blog en un solo archivo de datos tipado, o Astro Nano si prefieres minimalismo. Personalízala lo suficiente para que no sea reconocible: cambia tipografía, paleta y hero.

### 5. Hosting gratuito, dominio y CI/CD

| Host | Límites gratuitos clave (2026) | Comentario |
|---|---|---|
| **GitHub Pages** | Gratis para repos públicos. Límite blando de 100 GB/mes de ancho de banda. No permitido para e-commerce o negocio online. | Arranque más simple. Deploy con GitHub Actions. |
| **Cloudflare Pages** | Ancho de banda y peticiones estáticas ilimitadas. 500 builds/mes. Permite uso comercial. | **Mejor plan B/espejo.** CDN global rápida en LATAM. |
| **Netlify Free** | 300 créditos/mes (a 20 créditos/GB de ancho de banda y 15 créditos por deploy de producción, equivale a ≈15 GB o 20 deploys). Los proyectos **se pausan** al agotarse. | Riesgo innecesario. |
| **Vercel Hobby** | 100 GB, generoso en builds, pero **"restricted to non-commercial personal use only"**. | Válido para portafolio personal, pero no lo atas a nada monetizable. |
| **AWS S3 + CloudFront** | Plan **flat-rate Free de CloudFront** (lanzado en noviembre de 2025): $0/mes, 1 millón de peticiones, 100 GB de transferencia, 5 GB de créditos S3, WAF y DDoS incluidos y **sin cargos por excedente**. Hasta 3 planes gratuitos por cuenta. | **Suma puntos para tu perfil AWS** si lo haces con IaC y lo documentas como proyecto. |

**¿Alojarlo en AWS suma puntos?** Sí, pero solo si el hosting es parte de la evidencia: Terraform/SAM, OIDC de GitHub Actions a un rol IAM con mínimo privilegio, S3 privado con Origin Access Control y CloudFront. Es el espíritu de la **Cloud Resume Challenge** de Forrest Brazeal, reto de 16 pasos que pide certificación Cloud Practitioner, S3, CloudFront, DNS, API Gateway + Lambda + DynamoDB para un contador de visitas, IaC y CI/CD, con un compromiso proyectado de 50–70 horas en 6 semanas según el libro de Brazeal. Tú puedes hacer la **versión de datos**: en lugar de un contador de visitas, una API que sirve métricas producidas por tu pipeline.

**Cuidado con la cuenta AWS:** desde el 15 de julio de 2025, las cuentas nuevas eligen entre plan Free y Paid. Ambas reciben $100 en créditos más hasta $100 adicionales por actividades. El **plan Free se cierra a los 6 meses o al agotar créditos**. Para un sitio que debe vivir años necesitas el **plan Paid** con AWS Budgets y alertas, y apoyarte en el plan flat-rate gratuito de CloudFront y en los servicios *always free*. Por eso la ruta sensata es **arrancar en GitHub Pages o Cloudflare Pages** y migrar a AWS cuando tengas la IaC lista, conservando el host gratuito como respaldo.

**Dominio propio:** sí vale la pena (p. ej., `javi-datos.dev` o `nombreapellido.com`). Da control sobre lo que aparece al buscar tu nombre, un correo profesional y permite mover el sitio de host sin romper enlaces. Un `.com` suele costar del orden de 10–15 USD/año. Compara precio de **renovación**, no solo el del primer año.

**CI/CD con GitHub Actions:** un workflow `build → test (link checker, Lighthouse CI, validación de i18n) → deploy`. Para AWS: `aws s3 sync ./dist s3://bucket --delete` + invalidación de CloudFront, autenticado por OIDC (sin llaves en el repo, lo que la Cloud Resume Challenge advierte explícitamente). Un segundo workflow programado (cron) ejecuta el pipeline que regenera los datos del sitio.

### 6. Cómo no verse genérico

**Idea central: el portafolio es un producto de datos.**

- **Pipeline que alimenta el sitio.**
  - Un DAG diario de Airflow (o un GitHub Action programado para no pagar infraestructura permanente) extrae datos abiertos de transporte aéreo de Aerocivil, los transforma con Spark/PySpark y publica un JSON pequeño en S3.
  - El sitio muestra un widget "Pulso del turismo aéreo en Colombia" con pasajeros del último mes, variación interanual y rutas top.
  - Aerocivil publica en datos.gov.co el conjunto **"Transporte Aéreo Comercial – Tráfico Origen-Destino"** (2020–2026: aerolínea, año/mes, origen/destino, tipo de tráfico, pasajeros, carga). Según la Oficina de Analítica de la Aeronáutica Civil, entre enero y agosto de 2026 se movilizaron 39,4 millones de pasajeros (+4,6% frente a 2025): 22,3 millones en vuelos nacionales (+4,9%) y 17,1 millones internacionales (+4,1%), con 5,1 millones solo en agosto. Es material real, local y conectado con tu industria.
- **Página "Estado del sistema":** última ejecución del pipeline, duración, filas procesadas y checks de calidad pasados. Es lo que un hiring manager de DE quiere ver: observabilidad.
- **Changelog y now page** generados desde commits y releases.
- **Elementos lúdicos con moderación:** una terminal interactiva (`> whoami`, `> projects --aws`) existe incluso como plantilla Astro (Astro TUI Portfolio). Úsala como easter egg, no como navegación principal, porque perjudica la accesibilidad y la lectura rápida del reclutador.
- **Errores comunes a evitar:**
  - Titanic, Iris, Housing de Boston y MNIST.
  - Plantillas sin modificar.
  - Proyectos sin README ni "por qué".
  - Copiar tutoriales de YouTube paso a paso (los hiring managers los reconocen).
  - Notebooks sin conclusiones.
  - Enlaces rotos y demos dormidas sin aviso.
  - Copyright de hace dos años.

### 7. Mostrar que construyes con IA (sin perder credibilidad)

El consenso de 2026 es claro: usar IA no resta, **ocultarla o no poder explicar el código sí**. Lo que convence es lo verificable:

- **`AI_USAGE.md` por repo (mapa de contribución):** qué hizo la IA (scaffolding, tests candidatos, explicar una API), qué hiciste tú (modelado, decisiones, lógica de negocio) y **una sugerencia de la IA que rechazaste y por qué**. Guías de entrevistas de 2026 proponen exactamente este paquete: mapa de contribución, registro de decisiones, diff legible, evidencia de verificación y una sugerencia rechazada.
- **`DECISIONS.md` (ADRs):** por qué Airflow y no Step Functions, por qué Parquet particionado por mes, por qué este tamaño de chunk en RAG.
- **Evals:** si hay LLM, incluye un set de 30–50 preguntas con respuestas esperadas y métricas (exactitud, fidelidad al contexto, latencia, costo por consulta). La verificación es la señal más valorada.
- **Proyecto con LLM *aplicado a datos*, no un chatbot genérico.** Ejemplos: un agente que traduce preguntas de negocio a SQL sobre tu warehouse con *guardrails* (solo SELECT, límite de filas, catálogo de tablas), o un RAG sobre políticas de viaje corporativo. Los chatbots, analizadores de sentimiento y fine-tunes triviales en Hugging Face ya los tiene "cada otro candidato".
- **Post del blog "Cómo uso Claude Code / Copilot / Cursor en un pipeline de datos":** flujo, *prompts* reutilizables, revisión y tests. En el CV, sigue la fórmula **herramienta + contexto + resultado**, no "entusiasta de la IA".
- **Puedes ser capaz de reproducir lo clave sin el asistente.** Prepárate para eso en la entrevista.

### 8. ¿Multilenguaje? Sí: inglés como versión completa, español como versión nativa

Buscas empleo local y remoto internacional. El mercado nearshore desde Colombia está muy activo en 2026: el "2026 State of LatAm Hiring Report" de Near (más de 2.000 colocaciones) sitúa a Colombia como fuente n.º 1 de talento nearshore con el 23%, por delante de Argentina (21%) y Brasil (14%). Son datos de empresas de staffing, con sesgo comercial, pero la dirección es consistente entre fuentes. Un sitio en inglés es tu prueba escrita de inglés profesional.

**Implementación en Astro:**

```js
// astro.config.mjs
export default defineConfig({
  i18n: {
    locales: ["es", "en"],
    defaultLocale: "es",
    routing: { prefixDefaultLocale: false } // /proyectos (es) · /en/projects (en)
  }
});
```

- Contenido en `src/content/projects/es/*.mdx` y `src/content/projects/en/*.mdx`. Las cadenas de UI van en `src/i18n/ui.ts`.
- Usa `getRelativeLocaleUrl()` de `astro:i18n` para el selector de idioma y añade `hreflang` en el `<head>`.
- Regla de mantenimiento: **escribe primero en inglés los casos de estudio** (son los que leen reclutadores internacionales) y tradúcelos con IA + revisión tuya. El blog puede tener posts solo en un idioma, marcados claramente.
- **Alternativa válida:** si en algún momento el mantenimiento bilingüe te frena, deja **inglés como idioma por defecto** (los reclutadores locales en Bogotá para roles de Data Engineer también leen inglés) con la página "Sobre mí" y el CV en ambos idiomas.

### 9. Modo oscuro, diseño, accesibilidad, rendimiento, SEO y analítica

- **Modo oscuro: sí**, pero respetando `prefers-color-scheme` con un toggle persistente y sin parpadeo (script inline en `<head>`). Revisa que los diagramas Mermaid/SVG tengan versión clara y oscura.
- **Diseño:** una tipografía para texto y una monoespaciada para código. Máximo 1–2 colores de acento. Mucho espacio en blanco. Prioriza escaneabilidad: el reclutador dedica 2–3 minutos por portafolio según guías de contratación de IA.
- **Accesibilidad:** contraste AA, `alt` descriptivo en diagramas (con resumen textual de la arquitectura), navegación por teclado y `prefers-reduced-motion`.
- **Rendimiento:** objetivo Lighthouse 95–100. Astro lo da casi gratis. Imágenes con `<Image />` (AVIF/WebP), sin carruseles ni fuentes pesadas.
- **SEO:**
  - `title` y `description` por página, Open Graph con imagen por proyecto y `sitemap.xml`.
  - JSON-LD `Person` (con `jobTitle`, `sameAs` a GitHub y LinkedIn) y `BlogPosting`.
  - URLs legibles y canonical + `hreflang` por idioma.
- **Analítica:** privada y ligera (Cloudflare Web Analytics, GoatCounter, Umami o Plausible autoalojado), sin banner de cookies. Truco documentado en HN: durante la búsqueda activa, mira visitas desde ciudades o empresas tras cada postulación. Bonus DE: exporta tus métricas de visitas a S3 y procésalas en tu propio pipeline ("el sitio se analiza a sí mismo").

### 10. ¿Foto propia?

**Recomendación: sí, una foto real y reciente en "Sobre mí"** (opcionalmente pequeña en el hero), no en el CV.

- Encuesta de Ringover a 1.087 reclutadores de EE. UU. (junio de 2024, reportada por TechRadar): el **74,4%** se inclina más a entrevistar candidatos con foto, y el **67,5%** rechaza una foto mala (muy posada, baja calidad, informal o con filtros).
- La misma encuesta dice que el **66%** se desanimaría si detecta que es generada por IA, y el 88% cree que debe declararse; además, los reclutadores solo identificaron correctamente los headshots generados por IA el 39,5% de las veces. **No uses foto generada por IA**: contradice la credibilidad que construyes en §7.
- **Contrapeso:** hay riesgo de sesgo. Por eso hay quien la omite, y la foto nunca sustituye a los proyectos. Un celular con luz natural, fondo neutro y mirada a cámara basta. Usa la misma foto en LinkedIn y GitHub para reconocimiento entre plataformas.

### 11. Relación con GitHub, LinkedIn, CV, blog y certificaciones

- **README de perfil de GitHub:** 2–3 frases (quién eres, qué buscas), stack, enlaces al sitio, LinkedIn y correo, y los 3 proyectos insignia con una línea cada uno.
- **Repos fijados:** los 3 insignia + 1 de utilidades. Archiva o haz privados los de cursos.
- **Calidad de repo:** README con problema → arquitectura → cómo ejecutar (`make up`) → decisiones → resultados → aprendizajes. También:
  - tests (`pytest`) y CI en verde;
  - `.env.example`, `docker-compose` y `Makefile`;
  - licencia y commits con mensajes claros;
  - nada de credenciales.

  Joseph Machado (Start Data Engineering) ofrece plantillas libres que ya traen esta estructura: Airflow, Postgres, DuckDB, Spark, MinIO como S3 local, Quarto para el dashboard, IaC, CI/CD y checks de calidad. Es un buen punto de partida que luego debes adaptar a tu dominio.
- **LinkedIn:** titular con las mismas palabras clave que el hero. "Destacados" con el sitio y el proyecto insignia. Un post por proyecto terminado. Experiencia actual reescrita con resultados (p. ej., "migré X paquetes SSIS…, reduje tiempo de carga de reportes SSRS en Y%").
- **CV descargable:** PDF de 1 página por idioma, generado desde la misma fuente que el sitio (p. ej., JSON Resume o Markdown → PDF en CI) para que nunca diverjan.
- **Blog:** publica en **tu dominio** (dueño del contenido y del SEO) y **repúblicalo** en dev.to, Hashnode o Medium con URL canónica apuntando a tu sitio. AWS Builder Center sirve para posts orientados a AWS y te da visibilidad en esa comunidad. Cadencia realista: 1 post por mes o por proyecto.
- **Certificaciones:** para tu meta, **AWS Certified Data Engineer – Associate** tiene más peso que Cloud Practitioner. Esta última es requisito de la Cloud Resume Challenge, cuesta $100 y es útil como primer paso. Muéstralas en el CV y LinkedIn, y en el sitio solo como badge en "Sobre mí", enlazadas a Credly.

---

## Plantilla de caso de estudio (para cada proyecto)

```markdown
---
title: "Pulso del turismo aéreo en Colombia"
summary: "Pipeline diario en AWS que ingiere datos de Aerocivil, los modela y pronostica demanda por ruta."
role: "Diseño, desarrollo e IaC (proyecto individual)"
stack: [Python, Airflow, PySpark, AWS S3, Glue Catalog, Athena, Terraform, Prophet/LightGBM]
type: [pipeline, ml]
repo: https://github.com/...
demo: https://...
status: "En producción (ejecución diaria)"
---

## 1. Resumen en 30 segundos
Problema → solución → resultado principal (1 métrica) + diagrama.

## 2. Contexto y problema de negocio
Quién usaría esto (p. ej., un equipo de viajes corporativos que negocia tarifas) y qué decisión habilita.

## 3. Datos
Fuentes, volumen (filas/GB), frecuencia, problemas encontrados (nulos, cambios de esquema, códigos IATA inconsistentes).

## 4. Arquitectura
Diagrama (Mermaid/Excalidraw) + recorrido por capas: ingesta → raw (S3) → transformación (Spark) → curated (Parquet particionado) → consumo (Athena/dashboard/modelo).

## 5. Decisiones técnicas y trade-offs
3–5 decisiones con alternativa descartada y motivo (formato ADR breve).

## 6. Calidad, pruebas y observabilidad
Checks de datos, tests unitarios, idempotencia/reprocesamiento, alertas, costos.

## 7. Modelo / análisis (si aplica)
Baseline vs. modelo, métrica de validación (MAPE, AUC…), cómo se reentrena.

## 8. Resultados
Métricas concretas: tiempo de ejecución, costo mensual en AWS, precisión, filas/día.

## 9. Uso de IA en el desarrollo
Qué hizo la IA / qué hice yo / sugerencia rechazada / cómo verifiqué (enlace a AI_USAGE.md).

## 10. Qué haría distinto y próximos pasos

## 11. Enlaces
Repo · Demo · Post del blog · Video de 2 min · dbt docs / notebook renderizado
```

---

## Ideas de proyectos que demuestran el perfil híbrido DS+DE

**Proyecto insignia (obligatorio), turismo/viajes: "SkyPulse CO".**

- **Ingesta:** pipeline batch mensual/diario sobre el dataset origen-destino de Aerocivil (datos.gov.co, API Socrata), opcionalmente enriquecido con festivos colombianos y TRM del Banco de la República.
- **Stack:** Airflow (local con Docker o MWAA solo para la demo) → S3 raw → PySpark (local o AWS Glue) → Parquet particionado → Glue Catalog + Athena.
- **Modelo:** pronóstico de pasajeros por ruta con detección de anomalías.
- **Salida:** JSON para el widget del sitio + dashboard.
- **Por qué funciona:** demuestra DE (orquestación, Spark, AWS, IaC, calidad), DS (modelo, validación) y conocimiento de dominio (tu trabajo en viajes corporativos).

**Proyecto 2, financiero: "Gasto de viaje corporativo + FX".**

- Genera datos **sintéticos realistas** de gastos de viaje: millones de filas, con errores inyectados deliberadamente (duplicados, monedas mal codificadas, outliers).
- Construye un modelo dimensional (hechos/dimensiones) con dbt sobre DuckDB o Athena.
- Detección de anomalías de gasto (Isolation Forest) y conversión con TRM histórica.
- Muestra el puente con tu stack actual: **migración de un paquete SSIS + reporte SSRS a Airflow + dbt + Power BI/Streamlit**, documentando equivalencias. Es un caso que muchas empresas en Colombia están viviendo.

**Proyecto 3, IA aplicada a datos: "Pregúntale al warehouse".**

- Agente text-to-SQL sobre el warehouse del proyecto 1 o 2.
- **Guardrails:** solo lectura, catálogo semántico y límite de costo.
- **Evals:** set de preguntas con respuesta esperada, exactitud de SQL y latencia.
- Variante RAG: políticas de viaje corporativo + datos de gasto ("¿este viaje cumple la política?").
- **Despliegue:** Lambda + API Gateway o Streamlit Community Cloud (ten en cuenta que HF Spaces con Gradio/Docker ahora exige PRO).

**Proyecto opcional, educativo: "Deserción y desempeño en educación superior".** Con datos abiertos colombianos de educación (p. ej., resultados Saber Pro o estadísticas del SNIES): pipeline + modelo de clasificación + análisis de equidad. Útil si te interesa el sector edtech. Hazlo solo después de los tres anteriores.

**Proyecto "meta" (el propio sitio):** S3 + CloudFront + Terraform + GitHub Actions OIDC + API de métricas. Es tu versión DE de la Cloud Resume Challenge, documentada como caso de estudio corto.

---

## Recommendations: plan de ejecución (12 semanas, ritmo de estudiante nocturno)

1. **Semanas 1–2:**
   - Plantilla Astro personalizada, i18n ES/EN, páginas Inicio, Sobre mí, CV y Proyectos (vacía pero con estructura).
   - Deploy en GitHub Pages o Cloudflare Pages y dominio propio.
   - README de perfil de GitHub y LinkedIn alineados.
2. **Semanas 3–7:** proyecto insignia SkyPulse CO completo, con caso de estudio en inglés y español, video de 2 minutos y post del blog.
3. **Semanas 8–9:**
   - Migración del hosting a S3 + CloudFront con Terraform y OIDC.
   - Widget de métricas en vivo alimentado por el pipeline.
   - Página de "estado del sistema".
4. **Semanas 10–12:** proyecto 3 (LLM sobre el warehouse) con evals y `AI_USAGE.md`. Empieza a preparar AWS Data Engineer Associate.
5. **Después:** proyecto 2 (finanzas/migración SSIS), un post mensual y revisión trimestral del sitio (fechas, enlaces, demos).

## Checklist de lanzamiento

- [ ] Titular claro en el hero (ES y EN) + CTA a proyecto insignia y CV
- [ ] 3 proyectos con caso de estudio completo, diagrama, métricas y enlaces funcionando
- [ ] Cada repo: README con problema/arquitectura/cómo ejecutar, tests, CI en verde, `DECISIONS.md`, `AI_USAGE.md`, sin secretos
- [ ] CV PDF de 1 página en ES y EN, consistente con el sitio
- [ ] i18n: selector de idioma, `hreflang`, sin textos sin traducir
- [ ] Modo oscuro sin parpadeo; diagramas legibles en ambos temas
- [ ] Lighthouse ≥ 95 en rendimiento, accesibilidad, buenas prácticas y SEO (móvil)
- [ ] Open Graph con imagen por página; `sitemap.xml`; JSON-LD `Person`
- [ ] Analítica ligera y sin cookies activa
- [ ] Link checker en CI; demos despiertas o con aviso ("puede tardar ~30 s en despertar")
- [ ] Dominio con HTTPS; redirección `www` → raíz
- [ ] AWS: plan Paid + AWS Budgets con alertas, rol OIDC de mínimo privilegio, bucket privado con OAC
- [ ] Foto real reciente en "Sobre mí"; misma foto en LinkedIn y GitHub
- [ ] README de perfil de GitHub, repos fijados, LinkedIn "Destacados" apuntando al sitio
- [ ] Página `/now` con fecha; footer con año actual
- [ ] Prueba con 2–3 personas: "¿en 60 segundos sabes qué hago y cuál es mi mejor proyecto?"

## Caveats

- **Calidad de fuentes:** buena parte del consejo "qué buscan los hiring managers" viene de academias, vendedores de plantillas o empresas de staffing con interés comercial (Data Engineer Academy, Colorlib, empresas nearshore). Las uso cuando coinciden entre sí y con testimonios de practicantes en Hacker News. Cifras como "menos de 1 de cada 10 juniors tiene portafolio" no están respaldadas por un estudio verificable.
- **Precios y límites cambian rápido:**
  - El cambio de Hugging Face Spaces (Gradio/Docker requieren PRO según la documentación oficial actual) contradice a muchos blogs.
  - Las páginas de AWS se contradicen sobre si los créditos vencen a los 6 o a los 12 meses. Revisa la consola de facturación de tu propia cuenta.
  - Verifica los límites de Netlify, Vercel y CloudFront el día que despliegues.
- **El sitio no sustituye las entrevistas:** prepara SQL, modelado de datos y diseño de pipelines. Los proyectos solo te abren la conversación.
- **La encuesta de fotos (Ringover)** es de reclutadores generales, no específica de roles de datos ni de Colombia.
- **Nombres de versión:** las plantillas citadas mencionan Astro 6 y 7. Usa la versión estable que recomiende la documentación oficial el día que empieces.

---

## Fuentes

- https://github.com/canyonwhite/data-engineer-portfolio
- https://github.com/dmerelo/data-engineering-portfolio
- https://github.com/vedanthv/data-engineering-portfolio
- https://colorlib.com/wp/data-science-portfolio-examples/
- https://dataengineeracademy.com/blog/data-engineer-portfolio-review-checklist-2026-what-hiring-managers-actually-score/
- https://news.ycombinator.com/item?id=40860643
- https://news.ycombinator.com/item?id=41656015
- https://news.ycombinator.com/item?id=35164819
- https://github.com/cybergeekgyan/Data-Engineering-Portfolio
- https://github.com/jonathankamau/data-engineering-portfolio
- https://news.ycombinator.com/item?id=24426312
- https://huggingface.co/datasets/John6666/knowledge_base_md_for_rag_1/blob/main/hf_spaces_debug_guide_20260723.md
- https://www.lilachbullock.com/is-hugging-face-free/
- https://dev.to/klement_gunndu/5-ai-portfolio-projects-that-actually-get-you-hired-in-2026-5bpl
- https://adminlte.io/blog/free-astro-templates/
- https://themefisher.com/best-astro-portfolio-templates
- https://astro.build/themes/details/starfolio/
- https://getastrothemes.com/free-astro-themes-templates/
- https://platoltheme.com/blog/astro-vs-nextjs
- https://joshbrake.github.io/quarto-portfolio-website/workshop/
- https://aileapers.com/articles/42-static-site-generators-2026-comparison.html
- https://mouhrad-bendjillali.com/blog/why-i-chose-astro/
- https://www.sofast.host/blog/is-vercel-free/
- https://thesoftwarescout.com/best-static-site-generators-2026-astro-next-js-hugo-more/
- https://www.stork.ai/blog/how-to-host-a-website-for-free-2026
- https://unfoldcms.com/blog/cloudflare-pages-vs-netlify-vs-vercel-headless-cms-hosting
- https://www.promptstoproduct.com/vercel-free-tier-limits
- https://formsubmit.app/blog/vercel-free-plan-limits
- https://marzouk.io/posts/cloudfront-flat-rate
- https://akalcloud.ai/blog/cloudfront-pricing/
- https://costbench.com/software/cdn-edge/aws-cloudfront/
- https://builder.aws.com/content/3Kkt4kNiDSUnO3n6db2weSNubzE/the-dollar0-aws-account-in-2026-free-plan-credits-guardrails
- https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/
- https://citadelcloudmanagement.com/blogs/news/the-cloud-resume-challenge-how-to-stand-out-in-2026
- https://cloudresumechallenge.dev/docs/the-challenge/aws/
- https://www.datos.gov.co/en/Transporte/Transporte-A-reo-Comercial-Tr-fico-Origen-Destino-/gb6w-ynu4
- http://the-adaptist.com/career/build-ai-portfolio-get-hired-2026
- https://myseera.com/blog/portfolio-stand-out-to-recruiters
- https://interviewaibox.co/en/blog/ai-generated-work-portfolio-proof-2026
- https://blog.corecv.ai/which-ai-skills-actually-help-you-get-hired-in-2026/
- https://www.usestandout.today/blog/how-to-show-ai-skills-on-resume-2026/
- https://github.com/withastro/docs/blob/96ce08fd5cdb42525db07c348a460f9eafaa524a/src%2Fcontent%2Fdocs%2Fen%2Fguides%2Finternationalization.mdx
- https://www.glassdoor.ca/Community/ui-and-ux-designers/how-do-you-guys-feel-about-people-putting-their-photos-on-the-homepage-of-their-portfolio-websitei-heard-someone-say-how
- https://atlialearning.com/blog/how-to-build-an-ai-portfolio
- https://github.com/josephmachado/data_engineering_project_template
- https://www.startdataengineering.com/post/data-engineering-projects-with-free-template/
- https://www.startdataengineering.com/post/data-engineering-project-for-beginners-batch-edition/
- https://www.aerocivil.gov.co/publicaciones/3900/datos-abiertos/
- https://fastero.com/blog/streamlit-community-cloud-vs-paid-hosting-options

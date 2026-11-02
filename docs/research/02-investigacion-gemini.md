> Investigación realizada con Gemini (Deep Research), aportada por Javi. Documento de referencia; las decisiones vinculantes viven en `specs/`.

# **Guía de Arquitectura, Estrategia y Diseño para Portafolios Profesionales en Ingeniería y Ciencia de Datos**

La evolución del mercado tecnológico en el ámbito del análisis y procesamiento de datos ha transformado los criterios de evaluación de talento técnico. La tradicional presentación de repositorios aislados o cuadernos de análisis estáticos resulta insuficiente para demostrar competencias avanzadas de ingeniería. Para un perfil híbrido situado en la intersección entre la ciencia de datos y la ingeniería de datos, el portafolio profesional debe concebirse como una plataforma web funcional que evidencie arquitectura de sistemas, modularidad de código, orquestación de *pipelines* y prácticas modernas de desarrollo de software1.  
La convergencia entre la capacidad analítica y estadística (orientada a la extracción de valor y el modelado) y la infraestructura técnica (enfocada en la escalabilidad, automatización y gobierno de datos) representa una ventaja competitiva diferencial2. Lograr que un portafolio transmita con precisión esta dualidad requiere decisiones deliberadas respecto al stack tecnológico de publicación, el diseño de la experiencia de usuario, la estructura modular de los proyectos y la integración de tecnologías emergentes como la inteligencia artificial generativa3.

## **El Posicionamiento del Perfil Híbrido: Ciencia e Ingeniería de Datos**

El sesgo predominante en los portafolios de nivel inicial radica en la sobresaturación de análisis exploratorios sobre conjuntos de datos públicos hiperutilizados, como Titanic, Iris o MNIST, desplegados en archivos únicos sin estructura de paquete1. Los evaluadores técnicos en empresas de alto crecimiento priorizan la calidad estructural y la madurez de ingeniería sobre la cantidad de repositorios acumulados1.  
Un portafolio competitivo se compone de tres a cinco proyectos exhaustivamente desarrollados que abarquen el ciclo de vida completo del dato: desde la ingesta de fuentes heterogéneas hasta la entrega de tablas analíticas optimizadas o el despliegue de modelos de aprendizaje automático en producción1. La demostración de habilidades híbridas implica fundamentar las decisiones de diseño mediante razones técnicas medibles, como la elección de procesamiento por lotes (*batch*) frente a transmisión continua (*streaming*), la implementación de pruebas automatizadas de calidad de datos y la cuantificación del rendimiento computacional o los costos en la nube1.

| Dimensión de Evaluación | Enfoque Convencional de Ciencia de Datos | Enfoque Requerido en Ingeniería de Datos | Integración en el Perfil Híbrido |
| :---- | :---- | :---- | :---- |
| **Artifact Principal** | Cuaderno de Jupyter (.ipynb) con código monolítico y gráficos explicativos1. | Módulos de Python estructurados, scripts SQL parametrizados y DAGs de orquestación1. | Arquitectura de paquetes consumibles con cuadernos restringidos al análisis exploratorio inicial1. |
| **Tratamiento del Dato** | Ingesta de archivos planos locales (CSV/JSON) sin validación de esquema1. | Pipelines de extracción, transformación y carga (ETL/ELT) idempotentes con modelos en estrella1. | Ingesta desde APIs o sistemas de eventos hacia un almacenamiento en capas (Bronze, Silver, Gold)2. |
| **Garantía de Calidad** | Validación visual mediante inspección de gráficos o métricas puntuales del modelo1. | Pruebas unitarias de código (pytest) y validación estricta de datos (dbt tests, Great Expectations)1. | Cobertura de pruebas automatizadas en CI/CD que certifiquen tanto el código del pipeline como los esquemas de datos1. |
| **Despliegue y Ejecución** | Ejecución local en entornos de desarrollo no contenerizados1. | Contenerización mediante Docker, infraestructura como código y servicios administrados de nube1. | Entornos aislados reproducibles mediante un solo comando, compatibles con entornos multi-nube1. |

## **Evaluación del Stack Tecnológico Web y Opciones de Hosting Gratuito**

La infraestructura web seleccionada para publicar el portafolio actúa como la primera demostración de criterio técnico del candidato. Las alternativas de desarrollo basadas en plataformas visuales cerradas (*no-code*) limitan la personalización y transmiten una desconexión con los estándares modernos del desarrollo web. Por ello, la práctica recomendada consiste en adoptar generadores de sitios estáticos (SSG) vinculados a flujos de integración y despliegue continuo (CI/CD) mediante repositorios de código abierto4.

### **Comparativa de Frameworks: Astro frente a Quarto**

Las dos herramientas líderes en el ecosistema técnico para la construcción de sitios personales son **Astro** y **Quarto**6. Ambas opciones permiten un alojamiento libre de costos mediante servicios como GitHub Pages, Vercel o Netlify, pero difieren significativamente en su arquitectura subyacente y casos de uso óptimos6.

| Criterio de Comparación | Astro (Modern Web Engineering Framework) | Quarto (Scientific & Data Publishing System) |
| :---- | :---- | :---- |
| **Paradigma de Arquitectura** | Arquitectura de Islas con renderizado estático y cero JavaScript enviado al cliente por defecto4. | Sistema de publicación basada en Pandoc y Bootstrap optimizado para documentación técnica8. |
| **Soporte de Entradas** | Markdown, MDX, componentes de UI (React, Svelte, Vue) y Tailwind CSS7. | Quarto Markdown (.qmd), cuadernos de Jupyter (.ipynb), Markdown estándar6. |
| **Desempeño y Carga Web** | Carga ultra-rápida, consumo mínimo de ancho de banda y puntuaciones Lighthouse óptimas (95-100)4. | Rendimiento sólido en escritorio, aunque con mayor peso por librerías Bootstrap y dependencias CSS9. |
| **Procesamiento de Código** | Renderizado de sintaxis estático (Shiki/Prism). No ejecuta entornos de Python/R durante el build9. | Ejecuta y compila cuadernos o scripts durante el *build*, incrustando tablas y figuras actualizadas9. |
| **Mantenimiento y Estilo** | Personalización total del diseño mediante CSS moderno, variables globales y componentes modulares7. | Configuración orientada a archivos YAML (\_quarto.yml) con temas predefinidos de Bootstrap6. |
| **Interacción con Modelos IA** | Comprensión excepcional por parte de LLMs debido al uso masivo de sintaxis estándar web12. | Comprensión moderada por LLMs debido a directivas específicas de YAML y Pandoc12. |

La elección entre Astro y Quarto debe alinearse con la prioridad profesional del candidato:

* **Selección de Astro:** Es la alternativa recomendada cuando el objetivo principal es exhibir habilidades de ingeniería de software avanzadas, control total sobre la experiencia visual, tiempos de carga mínimos y la integración fluida de Tailwind CSS o componentes interactivos en tiempo real4.  
* **Selección de Quarto:** Es la alternativa ideal cuando la prioridad es la velocidad de publicación sin necesidad de escribir código HTML/CSS, permitiendo compilar directamente análisis ejecutados en Python o R con soporte nativo para ecuaciones matemáticas, bibliografía y tablas de datos avanzadas6.

### **Infraestructura de Alojamiento Gratuito y Mantenimiento**

Para garantizar la sostenibilidad a largo plazo sin costos de mantenimiento, la plataforma debe utilizar proveedores de hosting estático con automatización por eventos6:

> 1. **GitHub Pages:** Integración directa con repositorios de GitHub mediante GitHub Actions. Permite compilar el código fuente y publicar el sitio estático automáticamente con cada actualización en la rama principal6.  
> 2. **Netlify / Vercel:** Ofrecen pipelines de construcción optimizados, vistas previas automáticas del sitio por cada *Pull Request* creado, gestión simplificada de dominios personalizados y certificados SSL gratuitos7.

## **Arquitectura de Navegación, Experiencia de Usuario (UX) y Componentes Clave**

Un portafolio técnico efectivo debe diseñarse para minimizar la fricción en la lectura. Los reclutadores e ingenieros líderes dedican en promedio menos de dos minutos a la primera revisión de un sitio personal, por lo que la jerarquía de la información debe guiar la atención hacia la evidencia técnica de forma inmediata1.

| Sección del Sitio Web | Componentes UX Obligatorios | Propósito Técnico y Estratégico |
| :---- | :---- | :---- |
| **Página Principal (Home)** | Encabezado sintético con declaración de rol en menos de 15 palabras, enlaces a GitHub/LinkedIn y métricas clave5. | Establecer de inmediato el posicionamiento del perfil híbrido y facilitar el acceso a redes profesionales5. |
| **Matriz de Proyectos (Projects)** | Cuadrícula filtrable por etiquetas tecnológicas (ejemplo: *Data Pipelines*, *Cloud Architecture*, *MLOps*, *GenAI*)14. | Mostrar la diversidad técnica sin abrumar al visitante, permitiendo filtrar por interés específico14. |
| **Casos de Estudio (Deep Dives)** | Artículos detallados en formato MDX por cada proyecto, con diagramas, decisiones de diseño y resultados1. | Explicar la lógica de ingeniería y el valor del negocio antes de redirigir al código crudo en GitHub1. |
| **Trayectoria y CV (About/Resume)** | Historial académico y profesional interactivo, certificaciones verificables y stack técnico estructurado6. | Ofrecer una versión web legible del currículum junto con un botón para descargar la versión en formato PDF6. |
| **Página /now (Opcional)** | Breve resumen actualizado periodicamente sobre tecnologías en aprendizaje, proyectos activos o lecturas7. | Transmitir compromiso con el aprendizaje continuo y la evolución tecnológica en un mercado cambiante7. |

### **Elementos de Valor Diferencial**

* **Soporte de Modo Oscuro (Dark/Light Mode):** La inclusión de un selector de tema o el respeto automático a las preferencias de color del sistema operativo es un estándar fundamental en las plataformas dirigidas a audiencias desarrolladoras6.  
* **Estructura Multilenguaje (Inglés / Español):** Aunque la redacción técnica en inglés es indispensable para acceder al mercado global de software, contar con una arquitectura i18n que permita alternar entre español e inglés incrementa el alcance regional y demuestra atención al detalle en la construcción del sitio.  
* **Fotografía Profesional:** La integración de una imagen personal limpia e iluminada en la sección sobre el autor humaniza la interacción, transmite transparencia profesional y diferencia al sitio web de plantillas anónimas6.

## **Diseño de Proyectos para el Perfil Híbrido: Lakehouse, Streaming e IA Generativa**

Para sostener la afirmación de dominar tanto la ciencia como la ingeniería de datos, los proyectos exhibidos deben cubrir los patrones de diseño más relevantes de la industria moderna2. Se recomienda centrar el desarrollo en tres proyectos emblemáticos que demuestren capacidad técnica integral1.

### **Proyecto 1: Data Lakehouse Cloud y Modelado Dimensional (Foco de Ingeniería de Datos)**

El objetivo de este proyecto es construir una infraestructura completa de ingesta y transformación sobre un entorno de nube administrado2.

* **Mecanismo:** Ingesta automatizada de datos semiestructurados desde una API pública hacia un almacenamiento de objetos en la nube (AWS S3 o Azure ADLS Gen2), seguido de una estructuración en capas (Bronze para datos crudos, Silver para datos limpios y deduplicados, y Gold para esquemas dimensionales)2.  
* **Stack Tecnológico:** Python (boto3 / azure-storage-blob), dbt-core para la transformación SQL y modelado en estrella, Snowflake o Amazon Redshift como almacén de datos, y Apache Airflow o Dagster para la orquestación2.  
* **Evidencia de Ingeniería:** Implementación de cargas incrementales, pruebas de calidad de datos automáticas (dbt test para restricciones de integridad), particionamiento eficiente de archivos Parquet y control de costos de computación1.

### **Proyecto 2: Pipeline de Ingesta en Tiempo Real y Event-Driven (Foco de Procesamiento Distribuido)**

El propósito de esta arquitectura es capturar y procesar flujos continuos de datos con baja latencia2.

* **Mecanismo:** Simulación o captura de eventos en tiempo real (por ejemplo, transacciones financieras o lecturas de sensores IoT) enviados hacia un gestor de mensajes, procesados mediante agregaciones en ventanas de tiempo e ingertados en un almacenamiento de consulta rápida2.  
* **Stack Tecnológico:** Apache Kafka o Redpanda para la mensajería, PySpark Structured Streaming o Apache Flink para el procesamiento analítico, PostgreSQL o Delta Lake como destino de almacenamiento, y Grafana para la visualización en vivo2.  
* **Evidencia de Ingeniería:** Manejo de datos retrasados mediante marcas de agua (*watermarking*), garantías de procesamiento *at-least-once*, serialización eficiente y aislamiento de servicios mediante Docker Compose2.

### **Proyecto 3: Plataforma MLOps y Sistema de IA Generativa / RAG (Foco Híbrido DS/DE)**

Este proyecto combina el entrenamiento y servido de modelos de aprendizaje automático con la integración de arquitecturas avanzadas de IA generativa3.

* **Mecanismo:** Construcción de un pipeline automatizado de ingesta de documentos no estructurados, conversión a representaciones vectoriales y servicio de un sistema RAG (Retrieval-Augmented Generation) expuesto como API REST y conectado a un modelo LLM3.  
* **Stack Tecnológico:** Python, LangChain / LlamaIndex, bases de datos vectoriales (Qdrant, Pinecone o pgvector), MLflow para el registro de experimentos y parámetros, FastAPI para el servido, y GitHub Actions para el despliegue de la API3.  
* **Evidencia de Ingeniería:** Automatización del flujo de trabajo de *feature engineering*, evaluación estricta de métricas de precisión y fidelidad del RAG, pruebas de carga sobre la API y monitoreo de latencia en las inferencias3.

| Categoría de Proyecto | Ingesta y Captura | Almacenamiento y Formato | Transformación y Analítica | Orquestación y Calidad |
| :---- | :---- | :---- | :---- | :---- |
| **Batch Analytics Lakehouse**2 | Python, AWS Lambda, dlt (data load tool)2 | AWS S3, Parquet, Snowflake, Delta Lake2 | dbt-core, SQL Avanzado (Window functions, CTEs)2 | Apache Airflow, Great Expectations2 |
| **Real-Time Streaming Pipeline**2 | Apache Kafka, Debezium (CDC)2 | Delta Lake, Apache Iceberg, PostgreSQL2 | PySpark Structured Streaming, DuckDB2 | Docker Compose, PyTest, DuckDB checks3 |
| **MLOps & IA Generativa (RAG)**3 | Scrapers en Python, Document Loaders3 | Pgvector, Qdrant, MLflow Artifact Store3 | PyTorch, Scikit-Learn, LangChain, OpenAI API3 | GitHub Actions CI/CD, FastAPI, Evidently AI3 |

## **Diagramación de Arquitectura, Estructura de Repositorios y Colaboración con IA**

La claridad gráfica en la explicación de los sistemas desarrollados evita que el evaluador deba deducir la infraestructura a partir de la inspección directa del código fuente1.

### **Visualización de Arquitecturas con Mermaid.js**

La representación de flujos de datos debe integrarse dinámicamente en las páginas web utilizando **Mermaid.js**, lo que permite definir diagramas utilizando sintaxis basada en texto Markdown9. Esto garantiza que los diagramas mantengan una nitidez vectorial en cualquier pantalla y puedan someterse al control de versiones del repositorio sin requerir herramientas gráficas externas9.  
El procesamiento en capas de un pipeline analítico híbrido se describe mediante la secuencia operativa del dato:

> 1. **Origen e Ingesta:** Las fuentes de datos operacionales emiten registros semiestructurados que son recopilados por scripts de extracción idempotentes ejecutados en entornos contenerizados1.  
> 2. **Capa Bronze (Raw Storage):** Los datos crudos se depositan sin modificaciones en contenedores de almacenamiento en la nube, organizados por particiones temporales estrictas1.  
> 3. **Capa Silver (Limpieza y Estandarización):** Motores de procesamiento distribuido como Spark o transformadores SQL como dbt filtran registros nulos, corrigen tipos de datos y aplican reglas de integridad operacional1.  
> 4. **Capa Gold (Modelado y Servido):** Se consolidan las tablas en estrella para consultas analíticas de alto rendimiento o se alimentan bases de datos vectoriales para el consumo de modelos analíticos y motores de inteligencia artificial2.

### **Estructura Profesional de Repositorios en GitHub**

La organización interna de los repositorios de GitHub vinculados al portafolio debe reflejar las mejores prácticas de la ingeniería de software1. A continuación se detalla la distribución modular estándar recomendada para proyectos de datos1:

| Directorio / Archivo | Función dentro del Proyecto de Datos |
| :---- | :---- |
| .github/workflows/ci.yml | Pipeline automatizado de CI/CD para ejecutar linter (flake8/ruff), pytest y validaciones de dbt1. |
| config/config.example.yaml | Plantilla de configuración pública con variables del sistema, omitiendo claves privadas y credenciales1. |
| data/sample/ | Muestra sintética o anonimizada de tamaño reducido que permite ejecutar demostraciones locales completas1. |
| docs/architecture.md | Documentación técnica detallada con diagramas de flujo de datos, esquemas de tablas y decisiones de diseño1. |
| infra/Dockerfile | Archivo de configuración de imagen Docker para reproducir el entorno de ejecución del proyecto1. |
| infra/docker-compose.yml | Definición de servicios locales auxiliares (PostgreSQL, Kafka, LocalStack, Airflow)2. |
| sql/models/ | Modelos de dbt organizados en capas (staging, intermediate, marts) con sus respectivos archivos YAML de documentación1. |
| src/ingestion/ | Módulos de Python orientados a la ingesta, extracción y conexión con APIs o fuentes de datos1. |
| src/pipelines/ | Lógica principal de los flujos de transformación y procesamiento analítico1. |
| tests/ | Conjunto de pruebas unitarias y de integración desarrolladas con pytest1. |
| Makefile | Script de automatización para simplificar comandos habituales (make build, make test, make run)1. |
| pyproject.toml | Especificación de dependencias y configuración del entorno de Python mediante Poetry, UV o Pip1. |
| README.md | Documentación ejecutiva principal del repositorio orientada a la lectura rápida1. |

### **Marco de Documentación del README**

El documento README.md de cada repositorio debe estructurarse mediante cinco pilares clave1:

> 1. **Definición del Problema:** Contextualización clara del problema técnico o de negocio que el proyecto resuelve, especificando el volumen de datos e impacto esperado1.  
> 2. **Justificación de la Solución:** Diagrama de la arquitectura y explicación detallada de por qué se seleccionó el stack tecnológico utilizado en lugar de otras alternativas1.  
> 3. **Instrucciones de Ejecución en Un Solo Comando:** Pasos sencillos respaldados por un Makefile o docker-compose up que permitan clonar el repositorio y probar el pipeline localmente sin requerir cuentas de nube pagadas1.  
> 4. **Validación y Métricas de Rendimiento:** Exposición de resultados reales obtenidas en la ejecución, incluyendo cobertura de pruebas, tiempos de procesamiento y métricas de calidad de datos1.  
> 5. **Análisis de Compromisos (Tradeoffs) y Límites:** Discusión honesta sobre las limitaciones del sistema, costos asociados y posibles mejoras en futuras iteraciones de arquitectura1.

### **Construcción Colaborativa junto a la IA**

Mostrar competencia en el desarrollo asistido y acoplado con inteligencia artificial implica ir más allá del uso de LLMs para la generación de código básico. En el entorno contemporáneo de datos, esto se traduce en integrar patrones de IA directamente en la infraestructura3:

* **Integración del Model Context Protocol (MCP):** Desarrollar conectores que permitan a agentes inteligentes consultar esquemas de bases de datos o inspeccionar la salud de los pipelines a través de la especificación MCP3.  
* **Evaluación de Sistemas de IA:** Implementar pipelines de validación automatizada para medir la alucinación y la precisión de recuperación en sistemas RAG antes de su despliegue3.  
* **Generación de Datos Sintéticos:** Diseñar programas que utilicen LLMs para simular esquemas corruptos o registros atípicos con el fin de auditar la resiliencia de los chequeos de calidad de datos1.

## **Síntesis Estratégica y Recomendaciones de Implementación**

La edificación de un portafolio de datos con impacto profesional no exige la acumulación masiva de tecnologías, sino la demostración rigurosa de principios de ingeniería de software aplicados al procesamiento de datos1.  
Para garantizar un posicionamiento efectivo como perfil híbrido en ciencia e ingeniería de datos, se deben consolidar tres decisiones clave: seleccionar un generador de sitios estáticos de alto desempeño (Astro para control web absoluto o Quarto para simplicidad basada en cuadernos), restringir el alcance a tres o cinco proyectos emblemáticos que abarquen patrones de Lakehouse, streaming y MLOps/GenAI, y documentar cada proyecto mediante un enfoque riguroso respaldado por diagramas de arquitectura, pruebas automáticas de calidad y ejecutabilidad directa en entornos contenerizados1.

#### **Works cited**

> 1. GitHub for Data Engineers: Present Projects That Get Read, [https\://dataengineeracademy.com/blog/github-for-data-engineers-how-to-present-your-projects/](https://dataengineeracademy.com/blog/github-for-data-engineers-how-to-present-your-projects/)  
> 2. Checklist for Building a Cloud Data Engineer Portfolio \- DataExpert.io, [https\://www\.dataexpert.io/blog/checklist-building-cloud-data-engineer-portfolio](https://www.dataexpert.io/blog/checklist-building-cloud-data-engineer-portfolio)  
> 3. Top Data Engineering GitHub Projects for Your Portfolio \- Scaler, [https\://www\.scaler.com/blog/blog-data-engineering-projects-github-for-your-portfolio/](https://www.scaler.com/blog/blog-data-engineering-projects-github-for-your-portfolio/)  
> 4. I moved my portfolio website from Next.js to Astro. Best decision ever., [https\://dev.to/alexcloudstar/-i-moved-my-portfolio-website-from-nextjs-to-astro-best-decision-ever-40fe](https://dev.to/alexcloudstar/-i-moved-my-portfolio-website-from-nextjs-to-astro-best-decision-ever-40fe)  
> 5. 7 Data Science Portfolio Examples Worth Studying \[2026\] \- Seera, [https\://myseera.com/blog/data-science-portfolio-examples](https://myseera.com/blog/data-science-portfolio-examples)  
> 6. Data Science Portfolio with Quarto, [https\://deepshamenghani.quarto.pub/portfolio-with-quarto-workshop/](https://deepshamenghani.quarto.pub/portfolio-with-quarto-workshop/)  
> 7. Minimal Portfolio Template for Software Engineer using Astro and, [https\://github.com/vinitshahdeo/portfolio](https://github.com/vinitshahdeo/portfolio)  
> 8. Astro vs. Quarto: 2026 Market Share & Usage Comparison, [https\://www\.wmtips.com/technologies/compare/astro-vs-quarto/](https://www.wmtips.com/technologies/compare/astro-vs-quarto/)  
> 9. Migrating from Quarto to Astro: samforeman.me → samf.sh, [https\://samf.sh/posts/2026/06/28/](https://samf.sh/posts/2026/06/28/)  
> 10. What is the cheapest and easiest way to create AND maintain a, [https\://mimansajaiswal.github.io/posts/personal-website-hosting/](https://mimansajaiswal.github.io/posts/personal-website-hosting/)  
> 11. I built my new portfolio with Astro\! Looking for feedback. : r/astrojs, [https\://www\.reddit.com/r/astrojs/comments/1na10yh/i\_built\_my\_new\_portfolio\_with\_astro\_looking\_for/](https://www.reddit.com/r/astrojs/comments/1na10yh/i_built_my_new_portfolio_with_astro_looking_for/)  
> 12. Building a Portfolio Website \| Noah Weidig, [https\://noahweidig.com/blog/astro-portfolio/](https://noahweidig.com/blog/astro-portfolio/)  
> 13. My data science portfolio website. Made with Quarto in R. \- GitHub, [https\://github.com/oliverfanderson/quarto-portfolio](https://github.com/oliverfanderson/quarto-portfolio)  
> 14. 24 Data Science & Data Analyst Portfolio Examples 2026 \- Colorlib, [https\://colorlib.com/wp/data-science-portfolio-examples/](https://colorlib.com/wp/data-science-portfolio-examples/)  
> 15. Data architecture diagrams: Practical 2026 guide with examples, [https\://www\.instaclustr.com/education/data-architecture/data-architecture-diagrams-practical-2026-guide-with-examples/](https://www.instaclustr.com/education/data-architecture/data-architecture-diagrams-practical-2026-guide-with-examples/)  
> 16. Mermaid \| Diagramming and charting tool, [https\://mermaid.js.org/](https://mermaid.js.org/)  
> 17. Architecture Diagrams \- What is Paradime.io, [https\://docs.paradime.io/integrations/mermaid-js/architecture-diagrams](https://docs.paradime.io/integrations/mermaid-js/architecture-diagrams)
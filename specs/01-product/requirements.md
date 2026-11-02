# Requisitos

> Cada requisito tiene ID estable, prioridad (MoSCoW) y la feature que lo implementa. Estado: **Propuesto**
>
> Prioridad: **M** = Must, **S** = Should, **C** = Could, **W** = Won't (por ahora).

## Requisitos funcionales (FR)

### Navegación y estructura

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-001 | El sitio tiene header con navegación a Inicio, Proyectos, Blog, Sobre mí, CV y selector de idioma y tema. | M | F-001 | Pendiente |
| FR-002 | El footer muestra enlaces a GitHub, LinkedIn, email, RSS y el año actual. | M | F-001 | Pendiente |
| FR-003 | Todas las páginas existen en `/` (ES) y `/en/` (EN). El selector lleva a la página equivalente. | M | F-002 | Pendiente |
| FR-004 | Página 404 propia, bilingüe, con enlace a inicio y al proyecto insignia. | S | F-001 | Pendiente |

### Inicio

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-010 | Hero con titular (≤ 15 palabras), subtítulo, 3 a 5 badges de stack y 2 CTA: "Ver proyecto insignia" y "Descargar CV". | M | F-003 | Pendiente |
| FR-011 | Sección con 3 proyectos destacados (tarjeta: título, resumen, diagrama miniatura, métrica clave, etiquetas). | M | F-003 | Pendiente |
| FR-012 | Sección con los últimos 3 posts. | S | F-003 | Pendiente |
| FR-013 | Widget "métricas en vivo" alimentado por un pipeline propio. | S | F-007 | Pendiente |

### Proyectos

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-020 | Listado de proyectos con filtro por tipo: Pipelines, ML/Modelos, Analytics/BI, IA/LLM. | M | F-005 | Pendiente |
| FR-021 | Cada proyecto tiene página de caso de estudio según `04-content/case-study-template.md`. | M | F-006 | Pendiente |
| FR-022 | Los diagramas Mermaid se renderizan en el sitio y son legibles en tema claro y oscuro. | M | F-006 | Pendiente |
| FR-023 | Cada caso de estudio muestra enlaces a repo, demo, post y video si existen. | M | F-006 | Pendiente |
| FR-024 | Cada proyecto muestra su estado: En progreso, En producción, Archivado. | S | F-005 | Pendiente |

### Blog y contenido

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-030 | Blog con posts en MDX, etiquetas, fecha, tiempo de lectura e idioma. | S | F-010 | Pendiente |
| FR-031 | Feed RSS por idioma. | S | F-010 | Pendiente |
| FR-032 | Un post puede existir en un solo idioma y lo indica. | S | F-010 | Pendiente |
| FR-033 | Página `/now` con fecha de última actualización. | C | F-011 | Pendiente |
| FR-034 | Página `/lab` con experimentos y "cómo construyo con IA". | C | F-009 | Pendiente |

### Sobre mí y CV

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-040 | Página "Sobre mí" con foto real, historia breve, stack agrupado (sin niveles), certificaciones e idiomas. | M | F-004 | Pendiente |
| FR-041 | Página CV en HTML + PDF descargable en ES y EN, generados desde la misma fuente. | M | F-004 | Pendiente |
| FR-042 | Datos de contacto visibles sin formulario. | M | F-001 | Pendiente |

### Datos en vivo y observabilidad

| ID | Requisito | Prioridad | Feature | Estado |
|---|---|---|---|---|
| FR-050 | Un pipeline programado produce un JSON que el sitio consume. | S | F-007 | Pendiente |
| FR-051 | Página "Estado del sistema": última ejecución, duración, filas, checks de calidad. | C | F-008 | Pendiente |
| FR-052 | Si el JSON no está disponible, el widget muestra el último dato conocido y la fecha, nunca un error. | S | F-007 | Pendiente |

## Requisitos no funcionales (NFR)

| ID | Categoría | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|---|
| NFR-001 | Rendimiento | Lighthouse ≥ 95 en Performance (móvil) en home y caso de estudio. | Lighthouse CI en el workflow | M |
| NFR-002 | Rendimiento | ≤ 50 KB de JS en la home (sin contar islas opcionales cargadas bajo demanda). | Reporte de build | S |
| NFR-003 | Accesibilidad | WCAG 2.2 AA: contraste, foco visible, navegación por teclado, `alt` en imágenes y diagramas. | Lighthouse + axe | M |
| NFR-004 | Accesibilidad | Respeta `prefers-reduced-motion` y `prefers-color-scheme`. | Revisión manual | M |
| NFR-005 | SEO | `title`, `description`, Open Graph, `canonical`, `hreflang`, `sitemap.xml`, JSON-LD `Person`. | Lighthouse SEO + validador | M |
| NFR-006 | Mantenibilidad | Agregar un proyecto = 1 archivo MDX por idioma + assets. Sin tocar componentes. | Prueba al agregar el primer proyecto | M |
| NFR-007 | Mantenibilidad | El build falla si un contenido no cumple el esquema o falta una traducción de UI. | CI | M |
| NFR-008 | Calidad | Cero enlaces rotos internos. | Link checker en CI | M |
| NFR-009 | Seguridad | Sin secretos en el repo; deploy por OIDC / token de Pages. | Revisión + secret scanning | M |
| NFR-010 | Costo | 0 USD/mes de hosting. | Factura | M |
| NFR-011 | Disponibilidad | Deploy automático en cada push a `main`; rollback = revert del commit. | Workflow | M |
| NFR-012 | Privacidad | Analítica sin cookies, sin banner. | Revisión | S |
| NFR-013 | Compatibilidad | Funciona en las 2 últimas versiones de Chrome, Firefox, Safari, Edge y en móvil desde 360 px. | Revisión manual | M |

## Requisitos descartados (W)

| ID | Requisito | Motivo |
|---|---|---|
| FR-W01 | Barras o porcentajes de nivel por tecnología | No aportan evidencia y se vuelven en contra en entrevista (PR-01). |
| FR-W02 | Carruseles y contadores animados | Peso y distracción. |
| FR-W03 | [[POR DEFINIR]] | |

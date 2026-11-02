# Catálogo de proyectos

> Qué proyectos van en el portafolio y por qué. Máximo 3 destacados (PR-02). Estado: **Propuesto** (combina ambas investigaciones).

## Criterios de entrada

Un proyecto entra al portafolio solo si:

- [ ] Resuelve un problema de negocio identificable (idealmente turismo, finanzas o educación).
- [ ] No usa datasets de tutorial (PR-12).
- [ ] Tiene repo con README completo, tests y CI en verde.
- [ ] Demuestra al menos una habilidad objetivo: AWS, Airflow, Spark, modelado, calidad, IA aplicada.
- [ ] Tiene caso de estudio según la plantilla.

## Matriz de cobertura de habilidades

| Habilidad | P1 SkyPulse | P2 Gasto/FX | P3 Warehouse IA | P4 Meta (sitio) |
|---|---|---|---|---|
| Ingesta desde API | ● | | | |
| Airflow | ● | ○ | | |
| Spark / PySpark | ● | | | |
| AWS (S3, Glue, Athena) | ● | ○ | ○ | ● |
| dbt / modelado dimensional | ○ | ● | | |
| Calidad de datos | ● | ● | | |
| ML / pronóstico / anomalías | ● | ● | | |
| LLM / RAG / agentes + evals | | | ● | |
| IaC (Terraform) + CI/CD | ○ | | | ● |
| Migración desde SSIS/SSRS | | ● | | |

● principal · ○ secundario. [[POR DEFINIR: ajustar]]

## Proyectos

### P1. SkyPulse CO (insignia, turismo)

- **Problema:** [[POR DEFINIR]] Ej.: un equipo de viajes corporativos necesita anticipar demanda por ruta para negociar tarifas.
- **Datos:** Aerocivil origen-destino (datos.gov.co), festivos, TRM.
- **Stack propuesto:** Airflow, PySpark / Glue, S3, Parquet, Glue Catalog, Athena, Terraform, modelo de pronóstico.
- **Salida:** dashboard + `metrics.json` para el widget del sitio.
- **Estado:** Idea. Repo: [[POR DEFINIR]]

### P2. Gasto de viaje corporativo + FX (finanzas)

- **Problema:** [[POR DEFINIR]]
- **Datos:** sintéticos realistas con errores inyectados + TRM histórica.
- **Stack propuesto:** dbt + DuckDB/Athena, Isolation Forest, comparación SSIS/SSRS → Airflow/dbt.
- **Alternativa (investigación Gemini):** pipeline de streaming con Redpanda/Kafka + Spark Structured Streaming para transacciones en tiempo real. [[POR DEFINIR: ¿batch con migración SSIS o streaming?]]
- **Estado:** Idea.

### P3. Pregúntale al warehouse (IA aplicada)

- **Problema:** usuarios de negocio que no saben SQL.
- **Stack propuesto:** agente text-to-SQL o RAG, guardrails, set de evals (30 a 50 preguntas), FastAPI o Lambda, MCP opcional.
- **Estado:** Idea.

### P4. El propio sitio (meta)

- **Qué demuestra:** SDD, IaC, CI/CD, OIDC, hosting en AWS.
- **Estado:** En progreso (este repo).

## Proyectos existentes a evaluar

| Repo | ¿Entra? | Acción |
|---|---|---|
| `data-eng-portfolio-hotel-lakehouse` | [[POR DEFINIR]] | ¿Base de P1 o proyecto aparte? |
| `ingestor_trm` | [[POR DEFINIR]] | Posible componente de P1/P2 |
| `CV-as-Code` | [[POR DEFINIR]] | Posible fuente del CV (F-004) |
| `Monthly_Bank_Report` / `Monthly_Activity_Report` | [[POR DEFINIR]] | ¿Lab? |
| `claude-usage-monitor` / `Terminal-Heartbeat` | [[POR DEFINIR]] | ¿Lab "construyo con IA"? |
| Detección de cápsulas YOLOv5 (Feria Ucompensar) | [[POR DEFINIR]] | ¿Lab / ML? |
| Otros repos antiguos (calculadora, piedra-papel-tijera...) | No | Archivar o dejar sin fijar |

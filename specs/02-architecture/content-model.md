# Modelo de contenido

> Esquemas de las Content Collections. Son el contrato entre el contenido y los componentes: si un archivo no cumple, el build falla (NFR-007). Estado: **Propuesto**

## Organización en disco

```
src/content/
├── projects/
│   ├── es/<slug>.mdx
│   └── en/<slug>.mdx
├── posts/
│   ├── es/<slug>.mdx
│   └── en/<slug>.mdx
├── profile/
│   ├── es.yaml        datos de "Sobre mí" y hero
│   └── en.yaml
├── resume/
│   └── resume.yaml    fuente única del CV (con campos por idioma)
└── now/
    ├── es.md
    └── en.md
```

Regla: el `slug` es igual en ambos idiomas para poder emparejar traducciones.

## Colección `projects`

| Campo | Tipo | Requerido | Descripción |
|---|---|---|---|
| `title` | string | sí | Nombre del proyecto. |
| `summary` | string (≤ 160) | sí | Resumen de una línea. Se usa en tarjetas y meta description. |
| `role` | string | sí | Qué hizo Javi ("diseño, desarrollo e IaC, individual"). |
| `type` | enum[] | sí | `pipeline` · `ml` · `analytics` · `ai` · `infra`. |
| `stack` | string[] | sí | Tecnologías. Deben existir en el catálogo de stack [[POR DEFINIR: ¿catálogo cerrado?]]. |
| `domain` | enum | sí | `turismo` · `finanzas` · `educacion` · `otro`. |
| `status` | enum | sí | `en-progreso` · `produccion` · `archivado`. |
| `featured` | boolean | no | Aparece en la home (máximo 3). |
| `order` | number | no | Orden en la home. |
| `keyMetric` | `{ label, value }` | no | Métrica destacada de la tarjeta. |
| `cover` | image | no | Diagrama o captura para la tarjeta. |
| `repo` | url | no | |
| `demo` | url | no | |
| `video` | url | no | |
| `post` | referencia a `posts` | no | |
| `startDate` / `updatedDate` | date | sí / no | |
| `draft` | boolean | no | No se publica si es `true`. |
| `lang` | `es` · `en` | derivado de la carpeta | |

## Colección `posts`

| Campo | Tipo | Requerido |
|---|---|---|
| `title` | string | sí |
| `description` | string (≤ 160) | sí |
| `pubDate` | date | sí |
| `updatedDate` | date | no |
| `tags` | string[] | sí |
| `project` | referencia a `projects` | no |
| `canonicalUrl` | url | no (si se publicó primero en otro sitio) |
| `translationOf` | slug | no (si el post solo existe en un idioma, se omite) |
| `draft` | boolean | no |

## Datos `profile` (YAML)

```yaml
name: Javi Rodríguez Giraldo        # [[POR DEFINIR: nombre público]]
headline: "..."                     # titular del hero
subheadline: "..."
location: Bogotá, Colombia
availability: "[[POR DEFINIR: remoto / híbrido / presencial]]"
email: "[[POR DEFINIR: correo público]]"
links:
  github: https://github.com/Bimbitor
  linkedin: "[[POR DEFINIR]]"
  builderCenter: "[[POR DEFINIR]]"
stackGroups:
  - name: Ingeniería de datos
    items: [Python, SQL, Airflow, Spark, dbt]
  - name: Nube
    items: [AWS S3, Glue, Athena, Lambda]
  - name: Ciencia de datos
    items: [pandas, scikit-learn, PyTorch]
  - name: BI y bases de datos
    items: [SQL Server, SSIS, SSRS, Power BI]
certifications: []
languages:
  - { name: Español, level: Nativo }
  - { name: Inglés, level: "[[POR DEFINIR]]" }
photo: ./photo.jpg
```

## Datos `resume` (YAML, fuente única del CV)

Basado en [JSON Resume](https://jsonresume.org/schema) con campos `es`/`en` donde haya texto. [[POR DEFINIR: confirmar formato]]

## Reglas de validación extra

- Máximo 3 proyectos con `featured: true`.
- Todo proyecto `featured` debe existir en ambos idiomas.
- `summary` y `description` ≤ 160 caracteres.
- Toda imagen requiere `alt`.

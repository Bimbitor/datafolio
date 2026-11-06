# Fase 1 — Contrato HTTP: Sitio base

**Feature**: `001-sitio-base` | **Fecha**: 2026-11-05

Esta es la superficie pública completa del despliegue al cerrar la feature. Lo que no está aquí no
existe todavía y debe responder con la página de error.

---

## 1. Direcciones del sitio

Nueve secciones por dos idiomas. Los slugs salen del mapa único de rutas; los de abajo son los
acordados.

| Sección               | Inglés                 | Español                  | Entrega                                               |
| --------------------- | ---------------------- | ------------------------ | ----------------------------------------------------- |
| Raíz                  | `/`                    | `/`                      | **Servidor**, sin caché. Redirige por idioma (ver §2) |
| Inicio                | `/en/`                 | `/es/`                   | Estática                                              |
| Experiencia           | `/en/experience/`      | `/es/experiencia/`       | Estática                                              |
| Catálogo de proyectos | `/en/projects/`        | `/es/proyectos/`         | Servidor + caché de CDN 60 s                          |
| Ficha de proyecto     | `/en/projects/[slug]/` | `/es/proyectos/[slug]/`  | Servidor; **404** mientras no haya contenido          |
| Índice del blog       | `/en/blog/`            | `/es/blog/`              | Servidor + caché de CDN 60 s                          |
| Artículo              | `/en/blog/[slug]/`     | `/es/blog/[slug]/`       | Servidor; **404** mientras no haya contenido          |
| Contacto              | `/en/contact/`         | `/es/contacto/`          | Estática                                              |
| Política de datos     | `/en/data-policy/`     | `/es/politica-de-datos/` | Estática                                              |
| Error                 | cualquier otra         | cualquier otra           | **Servidor**, sin caché, estado **404** (ver §2 bis)  |

**Nota sobre las rutas de servidor**: en esta feature no hay contenido administrable. El catálogo y el
índice del blog sirven un armazón con la indicación de contenido pendiente; las **rutas de detalle
devuelven 404** con cualquier identificador, porque no existe lo que piden. Nacen ya renderizadas en servidor porque cambiar
el modo de entrega de una ruta después obliga a rehacer su estructura; nacer en el modo definitivo
cuesta lo mismo hoy y nada mañana.

**Archivos de apoyo**

| Dirección      | Contenido                                                                                                                         | Entrega  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `/sitemap.xml` | Las direcciones indexables de los dos idiomas —las secciones con `enIndice`, excluido el error—, generadas desde el mapa de rutas | Estática |
| `/robots.txt`  | Excluye `/admin`, declara el sitemap                                                                                              | Estática |

---

## 2. Redirección de la raíz

```http
GET /
```

| Condición                                                    | Respuesta      |
| ------------------------------------------------------------ | -------------- |
| Cabecera `Accept-Language` que pide español                  | `302` a `/es/` |
| Cualquier otro caso, incluida la cabecera ausente o ilegible | `302` a `/en/` |

Cabeceras de la respuesta: `Cache-Control: no-store`. La redirección depende de la petición, así que
no se puede cachear.

**La raíz no recuerda nada.** No hay cookie de idioma, así que resuelve por detección en cada visita.
Una vez dentro, la dirección lleva el idioma y eso basta para conservarlo al navegar y al recargar.

**No se registra nada** de la petición: ni la cabecera, ni la dirección de origen, ni el resultado.

---

## 2 bis. Página de error

```http
GET /cualquier-cosa-que-no-existe
```

| Condición                               | Respuesta                               |
| --------------------------------------- | --------------------------------------- |
| La dirección pedida empieza por `/es/`  | `404` con la página de error en español |
| La dirección pedida empieza por `/en/`  | `404` con la página de error en inglés  |
| La dirección no tiene prefijo de idioma | `404` con la página de error en inglés  |

Cabeceras: `Cache-Control: no-store`.

**Por qué en servidor y no estática**: una única página de error estática solo puede estar en un
idioma, y el idioma correcto depende de la dirección que se pidió. Resolverlo en servidor es la forma
más corta que funciona de verdad, y un 404 es una respuesta rara: no tiene presupuesto de
rendimiento que defender.

## 3. Cabeceras de toda respuesta del sitio

| Cabecera        | Valor                                                                                                                                                               | Hasta cuándo                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `X-Robots-Tag`  | `noindex`                                                                                                                                                           | Se retira en la feature 02, al publicarse el contenido real |
| `Cache-Control` | `no-store` en la raíz, en `/admin/*` y en `/api/*`; caché de CDN de 60 s en las rutas de servidor del sitio; el valor por defecto de la plataforma en las estáticas | Permanente                                                  |

Cada página declara además, en su encabezado:

```html
<link rel="canonical" href="https://{dominio}/{idioma}/{slug}/" />
<link rel="alternate" hreflang="en" href="https://{dominio}/en/{slug-en}/" />
<link rel="alternate" hreflang="es" href="https://{dominio}/es/{slug-es}/" />
<link rel="alternate" hreflang="x-default" href="https://{dominio}/en/{slug-en}/" />
```

`x-default` apunta al inglés, que es el idioma por defecto del sitio. Las cuatro etiquetas se generan
desde el mapa de rutas; ninguna se escribe a mano en una página.

---

## 4. Servicio de la API

El servicio responde bajo `/api/*` **del mismo dominio que el sitio**. Que esto sea cierto es el
criterio de aceptación de la historia P1: sin un origen común, la cookie de sesión del administrador
no viaja, y la feature 03 habría que rehacerla.

### `GET /api/estado`

Único endpoint público de la API en esta feature. Existe para probar la convivencia de los dos
servicios, no para informar de nada.

```http
GET /api/estado
```

```json
{ "servicio": "api", "version": "0.1.0" }
```

| Aspecto            | Valor      |
| ------------------ | ---------- |
| Estado             | `200`      |
| `Cache-Control`    | `no-store` |
| Autenticación      | Ninguna    |
| Datos que registra | Ninguno    |

### `GET /api/cookie-prueba`

Endpoint **temporal**, exclusivo de la verificación de la historia P1. Devuelve una cookie de prueba
sin ningún valor sensible, para comprobar desde el navegador que vuelve en la petición siguiente al
mismo dominio.

```http
GET /api/cookie-prueba
→ 204
   Set-Cookie: datafolio_prueba=1; Path=/; HttpOnly; Secure; SameSite=Strict
```

**Se elimina al cerrar la feature.** Queda escrito aquí para que su eliminación sea una tarea y no un
olvido. `atajo: endpoint de verificación, se borra al terminar la historia P1.`

---

## 5. Comprobación programada

**No tiene dirección pública.** Es una función privada invocada por la tarea programada de la
plataforma cada seis horas. No se puede disparar desde internet, así que no necesita secreto que la
proteja.

**Qué hace, en orden:**

1. Escribe la fila de `salud` en la base de datos con el momento y el resultado.
2. Si el paso 1 falla, envía un correo al titular con la causa, y espera a que el envío termine antes
   de devolver.
3. Si el envío del correo también falla, deja el fallo original en el registro de la plataforma.

| Resultado                          | Qué queda                                                             |
| ---------------------------------- | --------------------------------------------------------------------- |
| Correcto                           | Fila actualizada; ejecución correcta en el historial de la plataforma |
| Fallo de base de datos             | Correo al titular; ejecución fallida en el historial                  |
| Fallo de base de datos y de correo | Ejecución fallida en el historial, con la causa original              |

---

## 6. Variables de entorno

Nombres, nunca valores. Todos se configuran en la plataforma, en ningún archivo del repositorio.
Son **siete**.
`.env.example` lleva solo esta lista.

| Variable                    | Para qué                                                                                   | Qué servicio la lee |
| --------------------------- | ------------------------------------------------------------------------------------------ | ------------------- |
| `SUPABASE_URL`              | Dirección del proyecto de datos                                                            | API                 |
| `SUPABASE_SERVICE_ROLE_KEY` | Clave de servicio para escribir en `salud`                                                 | API                 |
| `SMTP_USER`                 | Cuenta de Gmail que envía                                                                  | API                 |
| `SMTP_PASSWORD`             | Contraseña de aplicación de esa cuenta                                                     | API                 |
| `ADMIN_EMAIL`               | Dirección que recibe los avisos de fallo. No es la dirección pública de contacto           | API                 |
| `SITE_URL`                  | Dominio público, para construir `canonical` y `hreflang`                                   | Sitio               |
| `PUBLIC_CONTACT_EMAIL`      | Dirección pública del titular, para el enlace de correo del pie. Distinta de `ADMIN_EMAIL` | Sitio               |

La clave de la base de datos y la del correo **solo** las lee el servicio de la API. El sitio no tiene
acceso a ninguna de las dos, y eso es una propiedad de la arquitectura, no una convención.

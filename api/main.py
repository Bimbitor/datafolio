"""API de Datafolio.

En esta feature la API existe para una sola cosa: demostrar que el sitio y ella responden
bajo el mismo dominio. De eso depende que la cookie de sesion del administrador viaje, y por
tanto que la autenticacion de la feature 03 sea posible.

Contrato: specs/001-sitio-base/contracts/http.md, seccion 4.
"""

import os

from fastapi import FastAPI, Request, Response

import salud as comprobacion

# Sin documentacion interactiva: FastAPI publicaria /docs, /redoc y /openapi.json, que
# describirian el login del administrador en cuanto exista. Nadie pidio esa superficie.
app = FastAPI(
    title="Datafolio API",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

VERSION = "0.1.0"

# La reescritura de la plataforma CONSERVA el prefijo: este servicio recibe /api/estado tal
# cual. Comprobado en el despliegue de vista previa del 2026-11-06 pidiendo /api/api/estado,
# que devolvio 404; si el prefijo se quitara, habria devuelto 200. Por eso ya no hay rutas
# duplicadas.


@app.get("/api/estado")
def estado() -> Response:
    """Estado del servicio. Sin autenticacion y sin registrar nada de la peticion."""
    # shortcut: diagnostico temporal, se borra al cerrar la historia P1 de la US6.
    # Dice si cada variable LLEGA al servicio, nunca su valor. Los nombres ya son
    # publicos -estan en .env.example, y el repositorio es publico-, asi que esto no
    # revela nada nuevo. Existe para distinguir "el secreto no coincide" de "el
    # servicio no recibe variables", que dan el mismo 401 y tienen arreglos opuestos.
    esperadas = (
        "CRON_SECRET",
        "SUPABASE_URL",
        "SUPABASE_SERVICE_ROLE_KEY",
        "SMTP_USER",
        "SMTP_PASSWORD",
        "ADMIN_EMAIL",
    )
    presentes = ",".join('"%s":%s' % (v, "true" if os.environ.get(v) else "false") for v in esperadas)
    return Response(
        content='{"servicio":"api","version":"%s","variables":{%s}}' % (VERSION, presentes),
        media_type="application/json",
        headers={"Cache-Control": "no-store"},
    )


@app.post("/api/salud")
def salud(peticion: Request) -> Response:
    """Comprobacion programada. La dispara la tarea de la plataforma cada seis horas.

    La ruta es publica porque el destino de funcion privada exigiria hacer privada toda
    la API, que es una sola aplicacion ASGI. Lo que la protege es el secreto que la
    plataforma envia en cada peticion suya. Ver research.md, D-03.
    """
    secreto = os.environ.get("CRON_SECRET")
    if not secreto or peticion.headers.get("authorization") != f"Bearer {secreto}":
        # Antes de cualquier trabajo, y sin decir por que: a quien llame sin el secreto no
        # se le explica si falta la variable o si el valor es otro.
        return Response(status_code=401, headers={"Cache-Control": "no-store"})

    comprobacion.comprobar()
    return Response(status_code=204, headers={"Cache-Control": "no-store"})


@app.get("/api/cookie-prueba")
def cookie_prueba() -> Response:
    """Entrega una cookie de prueba sin ningun valor sensible.

    Sirve para comprobar desde el navegador que una cookie SameSite=Strict vuelve en la
    peticion siguiente al mismo dominio, que es el cuarto paso de la historia P1.
    """
    # shortcut: endpoint de verificacion, se borra al cerrar la feature -no al cerrar la
    # historia P1-, porque la misma comprobacion hay que repetirla sobre produccion cuando
    # la rama se integre. Es la tarea T069.
    respuesta = Response(status_code=204, headers={"Cache-Control": "no-store"})
    respuesta.set_cookie(
        "datafolio_prueba",
        "1",
        path="/",
        httponly=True,
        secure=True,
        samesite="strict",
    )
    return respuesta

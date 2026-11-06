"""API de Datafolio.

En esta feature la API existe para una sola cosa: demostrar que el sitio y ella responden
bajo el mismo dominio. De eso depende que la cookie de sesion del administrador viaje, y por
tanto que la autenticacion de la feature 03 sea posible.

Contrato: specs/001-sitio-base/contracts/http.md, seccion 4.
"""

from fastapi import FastAPI, Response

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
    return Response(
        content='{"servicio":"api","version":"%s"}' % VERSION,
        media_type="application/json",
        headers={"Cache-Control": "no-store"},
    )


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

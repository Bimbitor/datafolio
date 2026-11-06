"""API de Datafolio.

En esta feature la API existe para una sola cosa: demostrar que el sitio y ella responden
bajo el mismo dominio. De eso depende que la cookie de sesion del administrador viaje, y por
tanto que la autenticacion de la feature 03 sea posible.

Contrato: specs/001-sitio-base/contracts/http.md, seccion 4.
"""

from fastapi import FastAPI, Response

app = FastAPI(title="Datafolio API", version="0.1.0")

VERSION = "0.1.0"

# El prefijo que ve este servicio depende de como la plataforma reescriba /api/*, y eso solo
# se confirma desplegando. Hasta entonces cada endpoint se declara con las dos formas.
# shortcut: rutas duplicadas con y sin /api mientras no se confirme la reescritura,
# se deja una sola al cerrar la historia P1.


@app.get("/api/estado")
@app.get("/estado")
def estado() -> Response:
    """Estado del servicio. Sin autenticacion y sin registrar nada de la peticion."""
    return Response(
        content='{"servicio":"api","version":"%s"}' % VERSION,
        media_type="application/json",
        headers={"Cache-Control": "no-store"},
    )


@app.get("/api/cookie-prueba")
@app.get("/cookie-prueba")
def cookie_prueba() -> Response:
    """Entrega una cookie de prueba sin ningun valor sensible.

    Sirve para comprobar desde el navegador que una cookie SameSite=Strict vuelve en la
    peticion siguiente al mismo dominio, que es el cuarto paso de la historia P1.
    """
    # atajo: endpoint de verificacion, se borra al terminar la historia P1
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

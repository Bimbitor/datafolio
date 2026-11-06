"""Los dos endpoints contra el contrato.

Fija lo que `specs/001-sitio-base/contracts/http.md`, seccion 4, promete. Llama a las
funciones directamente: no hace falta servidor ni cliente HTTP, asi que no entra ninguna
dependencia nueva para probar.
"""

import json

from main import app, cookie_prueba, estado


def test_no_publica_documentacion_interactiva():
    """FastAPI monta /docs, /redoc y /openapi.json por defecto. Aqui no deben existir:
    en cuanto haya login, describirian la autenticacion a cualquiera que entre."""
    rutas = {r.path for r in app.routes}
    for publicada in ("/docs", "/redoc", "/openapi.json", "/docs/oauth2-redirect"):
        assert publicada not in rutas


def test_solo_existen_las_rutas_del_contrato():
    """La reescritura de la plataforma conserva el prefijo /api, comprobado en el despliegue
    del 2026-11-06. Si alguien vuelve a anadir rutas sin prefijo, son inalcanzables: el
    servicio solo recibe lo que empieza por /api."""
    rutas = {r.path for r in app.routes if r.path.startswith("/")}
    assert {"/api/estado", "/api/cookie-prueba"} <= rutas
    assert "/estado" not in rutas
    assert "/cookie-prueba" not in rutas


def test_estado_devuelve_lo_pactado():
    respuesta = estado()
    assert respuesta.status_code == 200
    assert json.loads(respuesta.body) == {"servicio": "api", "version": "0.1.0"}
    assert respuesta.headers["cache-control"] == "no-store"








def test_cookie_de_prueba_viaja_con_las_defensas_puestas():
    """La cookie existe para comprobar el origen unico en la historia P1. Nace con las
    mismas defensas que tendra la de sesion, porque es lo que se esta probando."""
    respuesta = cookie_prueba()
    assert respuesta.status_code == 204
    galleta = respuesta.headers["set-cookie"]
    for pieza in ("datafolio_prueba=1", "Path=/", "HttpOnly", "Secure", "SameSite=strict"):
        assert pieza in galleta
    assert respuesta.headers["cache-control"] == "no-store"

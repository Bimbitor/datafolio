"""La comprobacion programada: la puerta del secreto y el manejo de fallos.

Nada de red. Se sustituye la escritura y el envio por funciones de mentira, porque lo que
hay que fijar es la decision -que hace cuando algo falla-, no que urllib funcione.
"""

import os

import pytest
import salud
from fastapi.testclient import TestClient
from main import app

SECRETO = "secreto-de-prueba-no-es-real"


@pytest.fixture
def cliente(monkeypatch):
    monkeypatch.setenv("CRON_SECRET", SECRETO)
    return TestClient(app)


def test_sin_el_secreto_no_entra(cliente, monkeypatch):
    """Y no se hace NADA de trabajo: si la puerta no cierra antes, da igual que exista."""
    llamadas = []
    monkeypatch.setattr(salud, "comprobar", lambda: llamadas.append(1))

    assert cliente.post("/api/salud").status_code == 401
    assert cliente.post("/api/salud", headers={"Authorization": "Bearer otra-cosa"}).status_code == 401
    assert cliente.post("/api/salud", headers={"Authorization": SECRETO}).status_code == 401
    assert llamadas == []


def test_sin_la_variable_puesta_tampoco_entra(monkeypatch):
    """Un despliegue al que se le olvido la variable debe cerrar, no abrirse."""
    monkeypatch.delenv("CRON_SECRET", raising=False)
    respuesta = TestClient(app).post("/api/salud", headers={"Authorization": "Bearer "})
    assert respuesta.status_code == 401


def test_con_el_secreto_corre_la_comprobacion(cliente, monkeypatch):
    llamadas = []
    monkeypatch.setattr(salud, "comprobar", lambda: llamadas.append(1) or {"resultado": "correcto"})

    respuesta = cliente.post("/api/salud", headers={"Authorization": f"Bearer {SECRETO}"})
    assert respuesta.status_code == 204
    assert respuesta.headers["cache-control"] == "no-store"
    assert len(llamadas) == 1


def test_escritura_correcta(monkeypatch):
    escrituras = []
    monkeypatch.setattr(salud, "_escribir_fila", lambda r, d: escrituras.append((r, d)))
    assert salud.comprobar() == {"resultado": "correcto"}
    assert escrituras == [("correcto", None)]


def test_si_la_base_falla_avisa_por_correo_y_deja_constancia(monkeypatch):
    """Avisa Y lanza: el correo es para enterarse, y la excepcion es para que la ejecucion
    conste como fallida en el historial de la plataforma."""
    avisos = []

    def romper(resultado, detalle):
        raise ConnectionError("la base no responde")

    monkeypatch.setattr(salud, "_escribir_fila", romper)
    monkeypatch.setattr(salud, "enviar", lambda asunto, cuerpo: avisos.append((asunto, cuerpo)))

    with pytest.raises(RuntimeError, match="la base no responde"):
        salud.comprobar()

    assert len(avisos) == 1
    assert "la base no responde" in avisos[0][1]


def test_si_el_aviso_tampoco_sale_el_fallo_original_viaja_en_el_mensaje(monkeypatch):
    """Es lo unico que quedara en el registro, asi que tiene que bastar para diagnosticar."""

    def romper(resultado, detalle):
        raise ConnectionError("la base no responde")

    def romper_correo(asunto, cuerpo):
        raise TimeoutError("el servidor de correo no contesta")

    monkeypatch.setattr(salud, "_escribir_fila", romper)
    monkeypatch.setattr(salud, "enviar", romper_correo)

    with pytest.raises(RuntimeError) as capturado:
        salud.comprobar()

    mensaje = str(capturado.value)
    assert "la base no responde" in mensaje
    assert "el servidor de correo no contesta" in mensaje


def test_la_peticion_no_finge_ser_un_navegador(monkeypatch):
    """La clave secreta de Supabase devuelve 401 si el agente de usuario parece navegador."""
    capturada = {}

    class RespuestaFalsa:
        status = 204

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

    def espiar(peticion, timeout=None):
        capturada["headers"] = dict(peticion.headers)
        capturada["metodo"] = peticion.get_method()
        return RespuestaFalsa()

    monkeypatch.setenv("SUPABASE_URL", "https://ejemplo.supabase.co")
    monkeypatch.setenv("SUPABASE_SERVICE_ROLE_KEY", "sb_secret_de_prueba")
    monkeypatch.setattr(salud.urllib.request, "urlopen", espiar)

    salud.comprobar()

    cabeceras = {k.lower(): v for k, v in capturada["headers"].items()}
    assert cabeceras["apikey"] == "sb_secret_de_prueba"
    assert "authorization" not in cabeceras
    assert "mozilla" not in cabeceras["user-agent"].lower()
    assert capturada["metodo"] == "PATCH"


def test_la_variable_de_entorno_que_falta_se_nota(monkeypatch):
    """Mejor un fallo ruidoso que una comprobacion que cree haber escrito y no escribio."""
    monkeypatch.delenv("SUPABASE_URL", raising=False)
    monkeypatch.setattr(salud, "enviar", lambda asunto, cuerpo: None)
    with pytest.raises(RuntimeError, match="KeyError"):
        salud.comprobar()
    assert "SUPABASE_URL" not in os.environ

"""Comprobacion programada.

Existe por un fallo conocido y silencioso: el proyecto gratuito de datos se suspende tras
una semana sin actividad, y un portafolio recien publicado pasa semanas sin visitas. El
fallo aparecería justo ante el primer visitante despues de una pausa.

Corre cada seis horas. Cuatro escrituras diarias siguen siendo un consumo irrelevante, y
mueven la señal de actividad del terreno de "tipicamente suficiente" al de holgado: el
proveedor advierte que su umbral no esta garantizado con poco trafico.

Ver specs/001-sitio-base/research.md, D-04 y D-12.
"""

import json
import os
import urllib.request
from datetime import datetime, timezone

from correo import enviar

TIEMPO_LIMITE = 15


def _escribir_fila(resultado: str, detalle: str | None) -> None:
    """Actualiza la fila unica de `salud`. Esta escritura es la actividad que cuenta.

    La clave va en la cabecera `apikey`, no en `Authorization: Bearer`: asi se envian las
    claves nuevas de Supabase. Y el agente de usuario no puede parecer un navegador, porque
    la clave secreta devuelve 401 cuando lo parece.
    """
    base = os.environ["SUPABASE_URL"].rstrip("/")
    peticion = urllib.request.Request(
        f"{base}/rest/v1/salud?id=eq.1",
        data=json.dumps(
            {
                "comprobado_en": datetime.now(timezone.utc).isoformat(),
                "resultado": resultado,
                "detalle": detalle,
            }
        ).encode("utf-8"),
        method="PATCH",
        headers={
            "apikey": os.environ["SUPABASE_SERVICE_ROLE_KEY"],
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
            "User-Agent": "datafolio-salud/1.0",
        },
    )
    with urllib.request.urlopen(peticion, timeout=TIEMPO_LIMITE) as respuesta:
        if respuesta.status >= 300:
            raise RuntimeError(f"la base de datos respondio {respuesta.status}")


def comprobar() -> dict:
    """Escribe la fila y devuelve el resultado.

    Si la escritura falla, avisa por correo y LANZA, para que la ejecucion conste como
    fallida en el historial de la plataforma. Si el aviso tampoco sale, el fallo original
    viaja en el mensaje: es lo unico que quedara, y tiene que bastar para diagnosticar.

    `resultado` solo toma el valor `correcto` hoy: lo unico que puede fallar en esta
    comprobacion es la propia escritura, y si falla no hay donde registrar nada. El valor
    `fallido` queda disponible para cuando la comprobacion tenga pasos que puedan fallar
    despues de que la base responda.
    """
    try:
        _escribir_fila("correcto", None)
    except Exception as fallo:
        causa = f"{type(fallo).__name__}: {fallo}"
        try:
            enviar(
                "Datafolio: la comprobacion programada fallo",
                "La comprobacion periodica no pudo escribir en la base de datos.\n\n"
                f"Causa: {causa}\n\n"
                "Mientras no se arregle, el proyecto de datos se acerca al umbral de\n"
                "suspension por inactividad, que son siete dias.",
            )
        except Exception as fallo_del_aviso:
            raise RuntimeError(
                f"{causa} || y el aviso por correo tampoco salio: "
                f"{type(fallo_del_aviso).__name__}: {fallo_del_aviso}"
            ) from fallo
        raise RuntimeError(causa) from fallo

    return {"resultado": "correcto"}

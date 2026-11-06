"""Envio de correo desde el servidor, con la biblioteca estandar.

Sin dependencias: smtplib y email.message bastan para veinte lineas.

Dos condiciones que la constitucion fija como restriccion tecnica y que aqui se cumplen:
el envio se completa ANTES de devolver -una funcion sin servidor descarta el trabajo
pendiente al responder, asi que un envio no esperado se pierde en silencio- y nunca corre
en un entorno sin sockets TCP.
"""

import os
import smtplib
import ssl
from email.message import EmailMessage

SERVIDOR = "smtp.gmail.com"
PUERTO = 587  # Vercel bloquea el 25; el 587 con STARTTLS esta abierto.
TIEMPO_LIMITE = 20


def enviar(asunto: str, cuerpo: str) -> None:
    """Envia un correo a la direccion de administracion.

    Lanza si algo falla. Quien llama decide que hacer con eso: aqui no se traga nada,
    porque un aviso que se pierde en silencio es peor que no tener aviso.
    """
    usuario = os.environ["SMTP_USER"]
    clave = os.environ["SMTP_PASSWORD"]
    destino = os.environ["ADMIN_EMAIL"]

    mensaje = EmailMessage()
    mensaje["From"] = usuario
    mensaje["To"] = destino
    mensaje["Subject"] = asunto
    mensaje.set_content(cuerpo)

    with smtplib.SMTP(SERVIDOR, PUERTO, timeout=TIEMPO_LIMITE) as servidor:
        servidor.starttls(context=ssl.create_default_context())
        servidor.login(usuario, clave)
        servidor.send_message(mensaje)

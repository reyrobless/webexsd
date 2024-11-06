import os
from dotenv import load_dotenv
from webexteamssdk import WebexTeamsAPI

# Cargar las variables de entorno
load_dotenv()
WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
TARGET_ROOM_ID = os.getenv("TARGET_ROOM_ID")

# Configurar el cliente de Webex con el token de acceso
api = WebexTeamsAPI(access_token=WEBEX_TOKEN)

# Función para obtener mensajes y reenviarlos
def handle_messages():
    # Obtener los mensajes más recientes en la cuenta del bot
    messages = api.messages.list()
    for message in messages:
        # Evitar que el bot reenvíe sus propios mensajes
        # if message.personEmail != "email_del_bot@dominio.com":
            # Reenviar el mensaje al grupo de destino
            api.messages.create(TARGET_ROOM_ID, text=message.text)

import time

# Ciclo continuo para verificar nuevos mensajes y reenviar
if __name__ == "__main__":
    print("Bot iniciado y escuchando en Webex.")
    while True:
        handle_messages()
        time.sleep(10)  # Intervalo de 10 segundos entre cada consulta

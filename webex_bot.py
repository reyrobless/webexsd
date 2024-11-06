import os
from dotenv import load_dotenv
from webexteamssdk import WebexTeamsAPI

import os
from dotenv import load_dotenv
from webexteamssdk import WebexTeamsAPI

# Cargar las variables de entorno
load_dotenv()
WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
TARGET_ROOM_ID = os.getenv("TARGET_ROOM_ID")

# Configurar el cliente de Webex con el token de acceso
api = WebexTeamsAPI(access_token=WEBEX_TOKEN)

# Obtener el ID del bot para evitar reenviar sus propios mensajes
bot_info = api.people.me()
BOT_ID = bot_info.id

# Función para manejar mensajes directos y reenviarlos a la sala de destino
def handle_direct_messages():
    # Obtener los mensajes más recientes que el bot ha recibido
    messages = api.messages.list()
    for message in messages:
        # Filtrar mensajes para:
        # - Ignorar mensajes que no son directos (no tienen "roomType" de "direct")
        # - Evitar que el bot reenvíe sus propios mensajes
        if message.roomType == "direct" and message.personId != BOT_ID:
            # Reenviar el mensaje al grupo de destino
            api.messages.create(TARGET_ROOM_ID, text=f"Mensaje de {message.personEmail}: {message.text}")

import time

# Ciclo continuo para verificar nuevos mensajes y reenviar
if __name__ == "__main__":
    print("Bot iniciado y escuchando mensajes directos en Webex.")
    while True:
        handle_direct_messages()
        time.sleep(10)  # Intervalo de 10 segundos entre cada consulta


import os
import tgcrypto
from pyrogram import Client, filters

Bot = Client(
    "YouTube-Thumbnail-Downloader",
    bot_token = os.environ.get("BOT_TOKEN"),
    api_id = int(os.environ.get("API_ID")),
    api_hash = os.environ.get("API_HASH")
)

# © chat.openai.com
@Bot.on_message(filters.command("start"))
def start_command_handler(client: Client, message: Message):
    client.send_message(message.chat.id, "Hello! I'm your Telegram bot.")
   
 

Bot.run()

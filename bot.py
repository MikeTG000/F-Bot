import os
import tgcrypto
from pyrogram import Client, filters

Bot = Client(
    "FirstBot",
    bot_token = os.environ.get("BOT_TOKEN"),
    api_id = int(os.environ.get("API_ID")),
    api_hash = os.environ.get("API_HASH")
)

#Start command
@Bot.on_message(filters.command("start"))
async def start_command(client, message):
	await message.reply_text("Hi :) how is it going?")

Bot.run()

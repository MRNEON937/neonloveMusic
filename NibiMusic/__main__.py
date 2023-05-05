from pyrogram import idle
from pyrogram import Client as Bot
from NibiMusic.Modules.cache.clientbot import run
from NibiMusic.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":LOVExMUSIC:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="LOVExMUSIC/Plugins")
)

bot.start()
run()
idle()

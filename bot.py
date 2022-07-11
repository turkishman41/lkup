# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging
import os
import time
from config import STRING_SESSION, BOT_TOKEN, APP_ID, API_HASH, DOWNLOAD_LOCATION, OWNER_ID, SESSION_NAME, SEND_LOGS_WHEN_DYING
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from functions.utils import ReadableTime
from pyromod import listen

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

class User(Client):

    def __init__(self):
        super().__init__(
            name=SESSION_NAME,
            session_string=STRING_SESSION,
            api_id=APP_ID,
            api_hash=API_HASH,
            workers=343,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION_NAME,
            BOT_TOKEN=BOT_TOKEN,
            api_id=APP_ID,
            api_hash=API_HASH,
            workers=343,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        if not os.path.isdir(DOWNLOAD_LOCATION): os.makedirs(DOWNLOAD_LOCATION)
        await super().start()
        if OWNER_ID != 0:
            try:
                await self.send_message(text="Karanlığın küllerinden yeniden doğdum.",
                    chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.error(str(t))

    async def stop(self, *args):
        if OWNER_ID != 0:
            texto = f"Son nefesimi verdim.\nÖldüğümde yaşım: {ReadableTime(time.time() - botStartTime)}"
            try:
                if SEND_LOGS_WHEN_DYING:
                    await self.send_document(document='log.txt', caption=texto, chat_id=OWNER_ID)
                else:
                    await self.send_message(text=texto, chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.warning(str(t))
        await super().stop()
        LOGGER.info(msg="App Stopped.")
        exit()
bot = Bot() 
bot.run()

app = User()
app.run()

# HuzunluArtemis - 2021 (Licensed under GPL-v3)

import logging
import os
import time
from config import BOT_TOKEN, APP_ID, API_HASH, DOWNLOAD_LOCATION, OWNER_ID, SESSION_NAME, SEND_LOGS_WHEN_DYING, STRING_SESSION, app, userbot
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from functions.utils import ReadableTime
from pyromod import listen

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

app.run()

#userbot.run()

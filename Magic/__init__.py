import logging
import asyncio

from aiohttp import ClientSession
from Magic.helpers._load import *
from Magic.helpers._database import * 

aiosession = ClientSession()

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()

FORMAT = "[Magic] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("pymongo", "redis").setLevel(logging.WARNING)

LOGGER = logging.getLogger('[Magic]')
LOGGER.info("Ubot is starting. | An Magic Project Parts. | Licensed under GPLv3.")
LOGGER.info("Not affiliated to other anime or Villain in any way whatsoever.")
LOGGER.info("Project maintained by: github.com/Team-Pesulap (t.me/pesulaptelegram)")

bot = MPBot()

ubot = MPUser()

MDB = DBMagic()

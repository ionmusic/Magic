import logging
import sys
import asyncio

from aiohttp import ClientSession

from config import *
from pyrogram import *

from Magic.helpers._database import *
from Magic.helpers._load import *

aiosession = ClientSession()

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()

MDB = DBMagic()

bot = Client(
  name="bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
)

ubot = Client(
  name="ubot",
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=SESSION,
  device_model="MagicProject",
)



if not API_ID:
    print("Silakan Masukkan API_ID")
    sys.exit()

if not API_HASH:
    print("Silakan Masukkan API_HASH")
    sys.exit()

if not BOT_TOKEN:
    print("Silakan Masukkan BOT_TOKEN")
    sys.exit()

if not SESSION:
    print("Silakan Masukkan SESSION")
    sys.exit()


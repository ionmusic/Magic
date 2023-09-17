
import asyncio

from aiohttp import ClientSession
from Magic.helpers._load import *

aiosession = ClientSession()

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()


bot = MPBot()

ubot = MPUser()
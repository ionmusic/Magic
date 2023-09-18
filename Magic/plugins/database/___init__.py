import motor.motor_asyncio
from Magic.helpers._database import MDB

from .dbgcast import *

from config import MONGO_URL
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

db = cli.program

from pyrogram import Client
from pyrogram.types import Message
from datetime import datetime
from Magic import *
from Magic.plugins import *
from config import *

@ubot.on_message(filters.command("ping", prefix) & filters.me)
async def pinx(client: Client, message: Message):
    mulai = datetime.now()
    berhenti = datetime.now()
    durasi = (berhenti - mulai).microseconds / 1000
    await message.reply_text(f"**Sepong!**\n" f"`%sms`" % (durasi))


@ubot.on_message(filters.command("woi", prefix) & filters.me)
async def test(client: Client, message: Message):
    await message.reply_text("asu")

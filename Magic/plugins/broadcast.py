import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.flood_420 import FloodWait

from Magic import *
from Magic.plugins import *
from config import *

__MODULE__ = "Gcast"
__HELP__ = """
 Bantuan Untuk Gcast

• Perintah : <code>{0}gcast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua grup.
"""


def extract_argument(message: Message):
    pesan = message.text
    pesan = pesan.replace(" ", "", 1) if pesan[1] == " " else pesan
    split = pesan[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

async def get_target(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)
    return chats

@ubot.on_message(filters.command("gcast", prefix) & filters.me)
async def global_broadcast(client: Client, message: Message):
    if message.reply_to_message or extract_argument(message):
        msg = message.reply_to_message
        ea = extract_argument(message)
        amg = await message.reply("`Globally Broadcasting...`")
    else:
        return await message.reply("`Please reply or leave a message.`")
    berhasil = 0
    gagal = 0
    target = await get_target(client, "group")

    for gc_id in target:
        if gc_id not in BLACKLIST_CHAT:
            try:
                if message.reply_to_message:
                    await msg.copy(gc_id)
                else:
                    await client.send_message(gc_id, ea)
                berhasil += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                if message.reply_to_message:
                    await msg.copy(gc_id)
                else:
                    await client.send_message(gc_id, ea)
                berhasil += 1
            except Exception:
                pass

    await amg.edit(f"**Successfully Sent Message To `{berhasil}` Groups chat. Failed: `{gagal}`**.")

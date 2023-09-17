#Moga Kaga error yak, pertama kali bikin module sendiri
#Credit? Lumiere dan semua yang ngerasa berguna aja 

import os 

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *
from Magic import *
from config import *
from Magic.helpers import get_arg
from . import *

__MODULE__ = "Copy"

__HELP__ = """
 Bantuan Untuk Copy

• Perintah : <code>{0}copy</code> [link]
• Penjelasan : Untuk mengambil pesan melalui link telegram.
"""

@ubot.on_message(filters.command("copy", prefix) & filters.me)
async def copy(client, message):
    await message.edit("Processing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            bkp = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Something is went wrong...")
    else:
        try:
            chat = str(link.split("/")[-2])
            bkp = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Something is went wrong...")
    laras = bkp.caption or None
    if bkp.text:
        await bkp.copy(message.chat.id)
        await message.delete()
    if bkp.photo:
        xpt = await client.download_media(bkp)
        await client.send_photo(message.chat.id, xpt, laras)
        await message.delete()
        os.remove(xpt)

    if bkp.video:
        xvid = await client.download_media(bkp)
        await client.send_video(message.chat.id, xvid, laras)
        await message.delete()
        os.remove(xvid)

    if bkp.audio:
        xaud = await client.download_media(bkp)
        await client.send_audio(message.chat.id, xaud, laras)
        await message.delete()
        os.remove(xaud)

    if bkp.voice:
        xvc = await client.download_media(bkp)
        await client.send_voice(message.chat.id, xvc, laras)
        await message.delete()
        os.remove(xvc)

    if bkp.document:
        xdoc = await client.download_media(bkp)
        await client.send_document(message.chat.id, xdoc, laras)
        await message.delete()
        os.remove(xdoc)
    else:
        await message.edit("Failed to downloading the content.....")

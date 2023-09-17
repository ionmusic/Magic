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
            if bkp.text or bkp.photo or bkp.video or bkp.audio or bkp.voice or bkp.document:
            media = await client.download_media(bkp)
            if bkp.text:
                await bkp.copy(message.chat.id)
            elif bkp.photo:
                await client.send_photo(message.chat.id, media, caption=laras)
            elif bkp.video:
                await client.send_video(message.chat.id, media, caption=laras)
            elif bkp.audio:
                await client.send_audio(message.chat.id, media, caption=laras)
            elif bkp.voice:
                await client.send_voice(message.chat.id, media, caption=laras)
            elif bkp.document:
                await client.send_document(message.chat.id, media, caption=laras)
            os.remove(media)
        else:
            await message.edit("Failed to download the content...")
        
        await message.delete()

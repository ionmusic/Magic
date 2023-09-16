#TeamPesulap
#kyaa><
# @PesulapTelegram


from datetime import datetime, timedelta
from pyrogram import Client, filters
import asyncio

from Magic import *
from config import *

@ubot.on_message(filters.command("limit", prefix) & filters.me)
async def spamban(client, message):
    await message.edit("Tunggu sebentar...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    async for ysj in client.get_chat_history("spambot", limit=1):
        await message.edit(ysj.text)


@ubot.on_message(filters.command("kickall", prefix) & filters.me)
async def kickallmem(client, message):
    await message.edit("Mengeluarkan semua anggota grup...!")
    member = client.get_chat_members(message.chat.id)
    async for all in member:
        try:
            await client.ban_chat_member(message.chat.id, all.user.id, 0)
        except:
            pass

@ubot.on_message(filters.command("zombie", prefix) & filters.me)
async def zmbie(client, message):
    await message.edit("Processing...")
    member = client.get_chat_members(message.chat.id)
    hantu = 0
    async for all in member:
        try:
            y = all.user.first_name
            if all.user.first_name == None:
                await client.ban_chat_member(message.chat.id, all.user.id, datetime.now() + timedelta(days=1))
                deleted += 1
        except:
            pass
    await message.edit(f"Berhasil Mengeluarkan {hantu} Akun terhapus!")

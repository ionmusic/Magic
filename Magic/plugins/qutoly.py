#TeamPesulap
#kyaa><
# @PesulapTelegram

import asyncio

from pyrogram.types import Message
from pyrogram import filters, Client

from Magic.helpers import *
from Magic import *
from config import *
from . import *


@ubot.on_message(filters.command("q", prefix) & filters.me)
async def quotly(client: Client, message: Message):
    anu = get_arg(message)
    if not message.reply_to_message and not anu:
        return await message.edit("`Reply pesan untuk membuat quotly`")
    anuan = "quotlybot"
    if message.reply_to_message:
        await message.edit("`Sedang membuat quotly anda . . .`")
        await client.unblock_user(anuan)
        if anu:
            await client.send_message(anuan, f"/qcolor {anu}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(anuan)
        await asyncio.sleep(5)
        async for quote in client.search_messages(anuan, limit=1):
            if quote:
                await message.delete()
                await message.reply_sticker(
                    sticker=quote.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("`Gagal Membuat Quotly`")
        await client.delete_messages(anuan, 2)

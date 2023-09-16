#TeamPesulap
#kyaa><


import random
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message

from config import *
from Magic import *



def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

spam_chats = []

@ubot.on_message(filters.command("mention", prefix) & filters.me)
async def mentionall(client, message):
    await message.delete()
    chat_id = message.chat.id
    rep = message.reply_to_message
    args = get_arg(message)
    if not rep and not args:
        return await message.reply("`Berikan saya pesan atau balas ke pesan !`")

    spam_chats.append(chat_id)
    usrnum = 0
    txt = ""
    emoji = [ 
         "👍", 
         "👎", 
         "❤", 
         "🔥", 
         "🥰", 
         "😁", 
         "👏", 
         "🤔", 
         "🤯", 
         "😱", 
         "🤬", 
         "😢", 
         "🎉", 
         "🤩", 
         "🤮", 
         "💩", 
         "🙏", 
         "👌", 
         "🕊", 
         "🤡", 
         "🥱", 
         "🥴", 
         "😍", 
         "🐳", 
         "🌚", 
         "💯", 
         "🌭", 
         "🤣", 
         "⚡", 
         "🍌", 
         "🏆", 
         "💔", 
         "🤨", 
         "😐", 
         "🍓", 
         "🍾", 
         "😡", 
         "👾", 
         "🤷", 
         "😎", 
         "🙊", 
         "💊", 
         "😘", 
         "🦄", 
         "🙉", 
         "💘", 
         "🆒", 
         "🗿", 
         "🤪", 
         "💅", 
         "☃", 
         "🎄", 
         "🎅", 
         "🤗", 
         "✍", 
         "🤝", 
         "😨", 
         "😇", 
         "🙈", 
         "🎃", 
         "👀", 
         "👻", 
         "🤓", 
         "😭", 
         "😴", 
         "😈", 
         "🖕", 
         "💋", 
  ]
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        emote = random.choice(emoji)
        txt += f"[{emote}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
           if args:
               tx = f"{args}\n\n{txt}"
               await client.send_message(chat_id, tx)
           elif rep:
               await rep.reply(txt)
           await sleep(2)
           usrnum = 0
           txt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@ubot.on_message(filters.command("cancel", prefix) & filters.me)
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("`Tidak ada mention disini!.`")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("`Memberhentikan Mention.`")

import os
from pyrogram import Client, emoji, filters
from pyrogram.types import Message

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def get_args(message: Message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message
    return list(filter(lambda x: len(x) > 0, split))
    
async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    anu = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await anu(*args, **kwargs)

async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    kontol = text.strip()

    if is_int(kontol):
        return int(kontol)

    meledak = message.entities
    kocok = message._client
    if len(entities) < 2:
        return (await kocok.get_users(kontol)).id
    mmk = meledak[1]
    if mmk.type == "mention":
        return (await kocok.get_users(kontol)).id
    if mmk.type == "text_mention":
        return mmk.user.id
    return None

async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

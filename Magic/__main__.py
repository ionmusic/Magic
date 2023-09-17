from asyncio import get_event_loop_policy
from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle
from Magic import *
from Magic.helpers import *

async def done():
    try:
        await ubot.join_chat("pesulaptelegram")
        await ubot.send_message(-1001861414061, "Halo... Aku Berhasil Mengaktifkan Userbot")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    try:
        cek_db = MDB
        if bot:
            await bot.start()
            bot_id = (await bot.get_me()).username
            print(f"Bot ID: {bot_id} Berhasil Diaktifkan.")
            
        if ubot:
            await ubot.start()
            client_id = (await ubot.get_me()).id
            print(f"Client ID: {client_id} Berhasil Diaktifkan")
            
        await loadPlugins()
        await done()
        await idle()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())

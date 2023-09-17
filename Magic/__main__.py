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
        LOGGER(_name__).info(f"Koneksi Ke Database {MDB.name}...")
        if MDB.ping():
            LOGGER(_name__).info(f"Koneksi Berhasil Ke {MDB.name}..")
        if bot:
            await bot.start()
            bot_id = (await bot.get_me()).username
            print(f"Bot ID: {bot_id} Berhasil Diaktifkan.")
            
        if ubot:
            await ubot.start()
            client_id = (await ubot.get_me()).id
            MDB.set_key("OWNER_ID", ubot.me.id)
            print(f"Client ID: {client_id} Berhasil Diaktifkan")
            
        await loadPlugins()
        await done()
        await idle()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install()
    heroku()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

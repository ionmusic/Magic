import asyncio

from pyrogram import idle
from Magic import *
from Magic.helpers import *
from Magic.helpers._database import *
from Magic.helpers._load import *
from uvloop import install

async def done():
    try:
        await ubot.join_chat("pesulaptelegram")
        await ubot.send_message(-1001861414061, "Halo... Aku Berhasil Mengaktifkan Userbot")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    try:
        
        if bot:
            await bot.start()
            bot_id = (await bot.get_me()).username
            LOGGER(__name__).info(f"Bot ID: {bot_id} Berhasil Diaktifkan.")
            
        if ubot:
            await ubot.start()
            client_id = (await ubot.get_me()).id
            MDB.set_key("OWNER_ID", ubot.me.id)
            LOGGER(__name__).info(f"Client ID: {client_id} Berhasil Diaktifkan")
        LOGGER(__name__).info(f"Koneksi Ke Database {MDB.name}...")
        if MDB.ping():
            LOGGER(__name__).info(f"Koneksi Berhasil Ke {MDB.name}..")
        await loadPlugins()
        
        await done()
        await idle()
        await aiosession.close()
    except Exception as e:
        LOGGER(__name__).error(f"Error: {e}")

if __name__ == "__main__":
    install()
    heroku()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())

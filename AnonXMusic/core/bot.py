from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.21375449,
            api_hash=config.ae7f34fdcb82d66247909059b12c0913,
            bot_token=config.7852409818:AAHi-FLX3vhLZry6jsvJGlHIt8VIXP3JfTE,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

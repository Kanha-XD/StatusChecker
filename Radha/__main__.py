import asyncio
import datetime
import logging

import pytz
from pyrogram import Client
from pyrogram.errors import FloodWait

import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    async with Client(
        "bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        session_string=config.STRING_SESSION,
    ) as app:
        logger.info("Starting Status Checker...")
        while True:
            try:
                TEXT = "✨ <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴛᴇᴀᴍ ɪɴsᴀɴᴇ ʙᴏᴛ's sᴛᴀᴛᴜs ᴄʜᴀɴɴᴇʟ</b>\n\n❄ ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙᴏᴛs ᴡᴇ ᴏᴡɴ ᴀɴᴅ ᴛʜᴇɪʀ sᴛᴀᴛᴜs (ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ), ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜᴘᴅᴀᴛᴇᴅ <b>ᴇᴠᴇʀʏ 10 ᴍɪɴᴜᴛᴇs.</b>"
                for bots in config.BOT_LIST:
                    bot = await app.get_users(f"@{bots}")
                    try:
                        await app.send_message(bots, "/statuscheck")
                        await asyncio.sleep(5)
                        async for message in app.get_chat_history(bots, limit=1):
                            msg = message.text
                        if msg == "/statuscheck":
                            TEXT += f"\n\n╭⎋ {bot.mention}\n╰⊚ sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄"
                            await app.read_chat_history(bots)
                        else:
                            TEXT += f"\n\n╭⎋ {bot.mention}  : ᴀʟɪᴠᴇ ✨\n╰⊚ {msg}"
                            await app.read_chat_history(bots)
                    except FloodWait as e:
                        await asyncio.sleep(e.value)
                    except Exception as e:
                        logger.error(
                            f"Failed to send message to {bot.first_name}\nreason: {e}"
                        )
                now = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                date = now.strftime("%d %b %Y")
                time = now.strftime("%I:%M %p")
                TEXT += f"\n\n<b>ʟᴀꜱᴛ ᴄʜᴇᴄᴋ ᴏɴ :</b>\n<b>ᴅᴀᴛᴇ :</b> {date}\n<b>ᴛɪᴍᴇ :</b> {time}\n\n"
                try:
                    await app.edit_message_text(
                        config.CHANNEL_ID, config.MESSAGE_ID, TEXT
                    )
                except Exception as e:
                    logger.error(f"Error: {e}")
                await asyncio.sleep(600)
            except Exception as e:
                logger.error(f"Error: {e}")
                await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())

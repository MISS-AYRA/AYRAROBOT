from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from AyraRobot import pbot as client


Ayra = "https://telegra.ph/file/395d6af16f462c011b19b.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Ayra,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴀʏʀᴀ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/Miss_Ayra_bot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [-❛𝑴𝑹♡︎𝑪𝑶𝑽𝑰𝑫🥀𝑩𝑨𝑩𝑨♡︎𓆪̥](tg://user?id=5230222509)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴀʏʀᴀ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="https://t.me/COVIDBABA"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/MISS-AYRA/AyraRobot"),
                    InlineKeyboardButton(
                        "• ʙʜᴀɪ •", url="https://t.me/BANNA_XD")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"

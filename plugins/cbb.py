#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👤 Creator : <a href='tg://user?id={OWNER_ID}'>WhitE_DevuL09</a>\n🗣️ Language : Python3\n🛠️ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n⚙️ Source Code : <a href='https://t.me/newdvdupdate'>Click Here</a>\n🔮 Channel : @NewDVDupdatE\n🔧 Support Group : @MalluMoviezGroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

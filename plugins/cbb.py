# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ​:\n\n👑 ᴏᴡɴᴇʀ​: <a href='https://t.me/{OWNER}'>Owner</a>\n📣 ᴄʜᴀɴɴᴇʟ​: <a href='https://t.me/{CHANNEL}'>Channel</a>\n👥 ɢʀᴏᴜᴘ​: <href='https://t.me/{GROUP}'>Grup</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass

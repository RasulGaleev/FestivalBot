from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

kb_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️Назад", callback_data="menu")]
])

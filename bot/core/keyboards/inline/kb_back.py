from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_kb_back(callback_data: str = "menu") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=callback_data)]
    ])

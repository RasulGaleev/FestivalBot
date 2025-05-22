from typing import List, Dict

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb_platform_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Расписание мероприятий", callback_data="schedule")],
    [InlineKeyboardButton(text="Как добраться и план площадки", callback_data="infrastructure")],
    [InlineKeyboardButton(text="⬅️Назад", callback_data="platform")],
])


def get_kb_platform(platforms: List[Dict[str, str]]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for p in platforms:
        kb.button(text=p['title'], callback_data=f"platform:{p['id']}")
    kb.button(text="⬅️Назад", callback_data="menu")
    kb.adjust(1)
    return kb.as_markup()

from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb_platform_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Расписание мероприятий", callback_data="schedule")],
    [InlineKeyboardButton(text="Как добраться и план площадки", callback_data="platform_infrastructure")],
    [InlineKeyboardButton(text="⬅️Назад", callback_data="platform")],
])


def get_kb_platform(platform_list: List[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for i in range(len(platform_list)):
        kb.button(text=platform_list[i], callback_data=f"platform:{i}")
    kb.button(text="⬅️Назад", callback_data="menu")
    kb.adjust(1)
    return kb.as_markup()

from typing import List

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb_schedule_date(dates: List[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for d in dates:
        kb.button(text=d, callback_data=f"schedule:{d}")
    kb.button(text="Назад", callback_data="menu")
    kb.adjust(1)
    return kb.as_markup()


def get_kb_schedule_titles(titles: List[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for t in titles:
        kb.button(text=t, web_app=WebAppInfo(url="https://teatr.mos.ru/"))
    kb.button(text="Назад", callback_data="schedule")
    kb.adjust(1)
    return kb.as_markup()

from typing import List, Dict

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb_schedule_date(dates: List[str]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for d in dates:
        kb.button(text=d, callback_data=f"schedule:{d}")
    kb.button(text="⬅️Назад", callback_data="menu")
    kb.adjust(1)
    return kb.as_markup()


def get_kb_schedule_events(events: List[Dict[str, str]]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for e in events:
        kb.button(text=e['title'], web_app=WebAppInfo(url=e['url']))
    kb.button(text="⬅️Назад", callback_data="schedule")
    kb.adjust(1)
    return kb.as_markup()

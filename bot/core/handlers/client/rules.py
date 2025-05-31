from aiogram import types
from aiogram.enums import ParseMode

from core.keyboards import kb_rules, get_kb_back
from core.messages import rules_message, rules_map


async def rules_handler(query: types.CallbackQuery) -> None:
    await query.message.answer(rules_message, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_rules)
    await query.message.delete()


async def rules_message_handler(query: types.CallbackQuery) -> None:
    rules_theme = query.data.split(":")[1]
    rules_text = rules_map[rules_theme]
    await query.message.answer(rules_text, reply_markup=get_kb_back("rules"))
    await query.message.delete()

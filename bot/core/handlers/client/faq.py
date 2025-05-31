from aiogram import types

from core.keyboards import kb_faq, get_kb_back
from core.messages import faq_message, faq_map


async def faq_handler(query: types.CallbackQuery) -> None:
    await query.message.answer(faq_message, reply_markup=kb_faq)
    await query.message.delete()


async def faq_message_handler(query: types.CallbackQuery) -> None:
    faq_question = query.data.split(":")[1]
    faq_answer = faq_map[faq_question]
    await query.message.answer(faq_answer, reply_markup=get_kb_back("faq"))
    await query.message.delete()

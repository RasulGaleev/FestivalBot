from aiogram import types

from core.keyboards import kb_question


async def question_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Часто задаваемые вопросы:", reply_markup=kb_question)
    await query.message.delete()

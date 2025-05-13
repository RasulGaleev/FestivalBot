from aiogram import types

from core.keyboards import kb_back


async def schedule_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Расписание мероприятий:", reply_markup=kb_back)
    await query.message.delete()

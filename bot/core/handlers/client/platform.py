from aiogram import types

from core.keyboards import kb_back


async def platform_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Площадки:", reply_markup=kb_back)
    await query.message.delete()

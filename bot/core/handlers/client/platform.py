from aiogram import types

from core.keyboards import kb_platform


async def platform_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Площадки:", reply_markup=kb_platform)
    await query.message.delete()

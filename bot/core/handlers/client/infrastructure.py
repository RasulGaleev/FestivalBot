from aiogram import types

from core.keyboards import kb_back


async def infrastructure_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Инфрастуктура фестиваля:", reply_markup=kb_back)
    await query.message.delete()

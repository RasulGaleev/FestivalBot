from aiogram import types


async def infrastructure_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Инфрастуктура фестиваля")
    await query.answer()

from aiogram import types

from core.keyboards import kb_platform

from core.messages import platform_message


async def platform_handler(query: types.CallbackQuery) -> None:
    await query.message.answer(platform_message, reply_markup=kb_platform)
    await query.message.delete()

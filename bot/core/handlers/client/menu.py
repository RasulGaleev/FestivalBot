import os

from aiogram import types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from core.keyboards import kb_menu
from core.messages import start_message


async def start_handler(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer_photo(photo=FSInputFile(os.path.join("core", "assets", "banner.jpg")),
                               caption=start_message,
                               parse_mode=ParseMode.MARKDOWN_V2,
                               reply_markup=kb_menu)


async def menu_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await query.message.answer_photo(photo=FSInputFile(os.path.join("core", "assets", "banner.jpg")),
                                     caption=start_message,
                                     parse_mode=ParseMode.MARKDOWN_V2,
                                     reply_markup=kb_menu)
    await query.message.delete()

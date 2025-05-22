from aiogram import types
from aiogram.fsm.context import FSMContext
from core.keyboards import get_kb_platform, kb_platform_menu
from core.messages import platform_message

platforms = [
    {"id": 1, "title": "Амфитеатр на Покровском бульваре"},
    {"id": 2, "title": "Музейный парк «Политех»"},
    {"id": 3, "title": "Патриаршие пруды"},
    {"id": 4, "title": "Новопушкинский сквер"},
    {"id": 5, "title": "Покровский бульвар"},
    {"id": 6, "title": "Чистопрудный бульвар"},
]


async def platform_handler(query: types.CallbackQuery) -> None:
    await query.message.answer(platform_message, reply_markup=get_kb_platform(platforms))
    await query.message.delete()


async def platform_filter_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    platform_id = query.data.split(":")[-1]
    await state.update_data(platform_id=platform_id)
    await query.message.answer(f"{platforms[int(platform_id) - 1]['title']}", reply_markup=kb_platform_menu)
    await query.message.delete()

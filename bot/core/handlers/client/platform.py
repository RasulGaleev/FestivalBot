from aiogram import types
from aiogram.fsm.context import FSMContext
from core.keyboards import get_kb_platform, kb_platform_menu, get_kb_schedule_events
from core.messages import platform_message, platform_map
from core.misc import get_unique_platforms, get_events_by_platform
from core.services import GSheet


async def platform_handler(query: types.CallbackQuery, state: FSMContext, gsheet: GSheet) -> None:
    events = await gsheet.get_verified_events()
    await state.update_data(events=events)
    platforms = get_unique_platforms(events)
    await state.update_data(platforms=platforms)
    await query.message.answer(platform_message, reply_markup=get_kb_platform(platforms))
    await query.message.delete()


async def platform_filter_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    platform_id = int(query.data.split(":")[-1])
    data = await state.get_data()
    platform = data['platforms'][platform_id]
    await state.update_data(platform_id=platform_id)
    await query.message.answer(platform_map[platform], reply_markup=kb_platform_menu)
    await query.message.delete()


async def platform_schedule_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    platforms = data['platforms']
    platform_id = data['platform_id']
    platform = platforms[platform_id]
    filtered_events = get_events_by_platform(data['events'], platform)
    await query.message.answer(f"Мероприятия на {platform}:",
                               reply_markup=get_kb_schedule_events(filtered_events,
                                                                   back_data=f"platform:{platform_id}"))
    await query.message.delete()


async def platform_infrastructure_handler(query: types.CallbackQuery) -> None:
    await query.message.answer("Инфрастуктура фестиваля")
    await query.answer()

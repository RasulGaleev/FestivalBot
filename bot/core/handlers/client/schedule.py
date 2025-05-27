from aiogram import types
from aiogram.fsm.context import FSMContext
from core.keyboards import get_kb_schedule_date, get_kb_schedule_events
from core.misc import get_unique_dates, get_events_by_date
from core.services import GSheet


async def schedule_handler(query: types.CallbackQuery, state: FSMContext, gsheet: GSheet) -> None:
    events = await gsheet.get_verified_events()
    await state.update_data(events=events)
    dates = get_unique_dates(events)
    await query.message.answer("Расписание мероприятий:", reply_markup=get_kb_schedule_date(dates))
    await query.message.delete()


async def schedule_filter_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    date = query.data.split(":")[-1]
    data = await state.get_data()
    events = data['events']
    filtered_events = get_events_by_date(events, date)
    await query.message.answer(f"Мероприятия на {date}:", reply_markup=get_kb_schedule_events(filtered_events))
    await query.message.delete()

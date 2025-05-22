from aiogram import types
from core.keyboards import get_kb_schedule_date, get_kb_schedule_titles
from core.services import GSheet


async def schedule_handler(query: types.CallbackQuery, gsheet: GSheet) -> None:
    dates = await gsheet.get_date_list()
    await query.message.answer("Расписание мероприятий:", reply_markup=get_kb_schedule_date(dates))
    await query.message.delete()


async def schedule_date_handler(query: types.CallbackQuery, gsheet: GSheet) -> None:
    date = query.data.split(":")[-1]
    events = await gsheet.get_event_list_by_date(date)
    await query.message.answer(f"Мероприятия на {date}:", reply_markup=get_kb_schedule_titles(events))
    await query.message.delete()

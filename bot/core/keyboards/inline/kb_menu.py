from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

kb_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Площадки", callback_data="platform")],
    [InlineKeyboardButton(text="Расписание мероприятий", callback_data="schedule")],
    [InlineKeyboardButton(text="Билеты", web_app=WebAppInfo(url="https://bilet.mos.ru/"))],
    [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="faq")],
    [InlineKeyboardButton(text="Правила посещения мероприятий", callback_data="rules")],
    [InlineKeyboardButton(text="Задать вопрос 🤖", callback_data="ask")],
])

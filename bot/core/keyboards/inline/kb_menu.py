from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

kb_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Площадки", callback_data="platform")],
    [InlineKeyboardButton(text="Расписание мероприятий", callback_data="schedule")],
    [InlineKeyboardButton(text="Билеты", web_app=WebAppInfo(url="https://bilet.mos.ru/"))],
    # [InlineKeyboardButton(text="Инфраструктура фестиваля", callback_data="infrastructure")],
    [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="question")],
    [InlineKeyboardButton(text="Правила посещения мероприятий", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Задать вопрос 🤖", callback_data="ask")],
])

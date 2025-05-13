from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

kb_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Как добраться", web_app=WebAppInfo(url="https://bilet.mos.ru/"))],
    [InlineKeyboardButton(text="Где проходит", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Сколько стоит", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Кто участвует", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Детям можно", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Места общепита", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Назад", callback_data="menu")],
])

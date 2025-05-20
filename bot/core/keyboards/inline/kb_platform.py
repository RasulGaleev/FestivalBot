from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

kb_platform = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Амфитеатр на Покровском бульваре", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Музейный парк «Политех»", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Патриаршие пруды", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Новопушкинский сквер", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Покровский бульвар", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="Чистопрудный бульвар", web_app=WebAppInfo(url="https://teatr.mos.ru/"))],
    [InlineKeyboardButton(text="⬅️Назад", callback_data="menu")],
])

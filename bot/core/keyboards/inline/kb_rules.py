from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_rules = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Общие правила пребывания на территории фестиваля", callback_data="rules:general")],
    [InlineKeyboardButton(text="Правила поведения у сцены во время спектаклей", callback_data="rules:scene")],
    [InlineKeyboardButton(text="Дополнительно важно знать", callback_data="rules:additional")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="menu")],
])

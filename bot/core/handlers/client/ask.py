import logging
from asyncio import sleep

from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from core.keyboards import kb_back
from core.services import YandexGPT
from core.states import AskStates


async def ask_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    await query.message.answer(text="Задать вопрос:", reply_markup=kb_back)
    await state.set_state(AskStates.waiting_for_ask)
    await query.message.delete()


async def process_ask_handler(message: types.Message, state: FSMContext, bot: Bot, yandex_gpt: YandexGPT):
    prompt = message.text

    data = await state.get_data()
    if 'messages' in data:
        messages = data['messages'][-10:]
    else:
        messages = []

    messages.append({"role": "user", "content": prompt})

    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        try:
            answer = await yandex_gpt.generate_text(messages=messages)
            messages.append({"role": "assistant", "content": answer})
            await state.update_data(messages=messages)
            await write_answer(chat_id=message.chat.id, answer=answer, bot=bot)

        except Exception as ex:
            await message.answer("Ошибка при генерации ответа. Попробуйте позже...")
            logging.error(ex)


async def write_answer(chat_id: int, answer: str, bot: Bot, parse_mode="Markdown") -> None:
    message_id = None
    length = len(answer)
    step = 20
    if length > 1000:
        step = 50
    try:
        for i in range(step, length, step):
            text = answer[:i]
            if i == step:
                message = await bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode,
                                                 disable_web_page_preview=True, protect_content=True)
                message_id = message.message_id
            else:
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=text, parse_mode=parse_mode, disable_web_page_preview=True)
            await sleep(0.5)

    except Exception as ex:
        logging.error(ex)

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                text=answer, parse_mode=parse_mode, disable_web_page_preview=True)

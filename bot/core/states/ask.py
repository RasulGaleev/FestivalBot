from aiogram.fsm.state import StatesGroup, State


class AskStates(StatesGroup):
    waiting_for_ask = State()

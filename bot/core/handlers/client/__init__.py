__all__ = ['register_client_handlers']

from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import any_state
from core.states import AskStates

from .ask import ask_handler, process_ask_handler
from .menu import start_handler, menu_handler
from .platform import platform_handler, platform_filter_handler, platform_infrastructure_handler
from .faq import faq_handler, faq_message_handler
from .schedule import schedule_handler, schedule_filter_handler
from .rules import rules_handler, rules_message_handler


def register_client_handlers(router: Router) -> None:
    router.message.register(start_handler, any_state, CommandStart())
    router.message.register(process_ask_handler, AskStates.waiting_for_ask)
    router.callback_query.register(menu_handler, F.data == 'menu')
    router.callback_query.register(platform_handler, F.data == "platform")
    router.callback_query.register(platform_filter_handler, F.data.startswith('platform:'))
    router.callback_query.register(platform_infrastructure_handler, F.data == "platform_infrastructure")
    router.callback_query.register(schedule_handler, F.data == "schedule")
    router.callback_query.register(schedule_filter_handler, F.data.startswith('schedule:'))
    router.callback_query.register(ask_handler, F.data == 'ask')
    router.callback_query.register(faq_handler, F.data == 'faq')
    router.callback_query.register(faq_message_handler, F.data.startswith('faq:'))
    router.callback_query.register(rules_handler, F.data == 'rules')
    router.callback_query.register(rules_message_handler, F.data.startswith('rules:'))

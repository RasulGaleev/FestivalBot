__all__ = ["start_message", "platform_message", "platform_map", "faq_message", "faq_map", "rules_message",
           "rules_map", ]

from .faq import faq_message, faq_map
from .menu import start_message
from .platform import platform_message, platform_map
from .rules import rules_message, rules_map

from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass()
class Bot:
    token: str
    admin_ids: List[int]


@dataclass()
class Redis:
    host: str
    port: int
    db: int


@dataclass()
class YandexGPT:
    token: str
    model_uri: str


@dataclass()
class GSheet:
    creds_path: str
    spreadsheet_id: str


@dataclass()
class Settings:
    bot: Bot
    yandex_gpt: YandexGPT
    gsheet: GSheet
    redis: Redis


def get_config(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bot=Bot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("BOT_ADMIN_ID"))),
        ),
        yandex_gpt=YandexGPT(
            token=env.str("YANDEX_GPT_TOKEN"),
            model_uri=env.str("YANDEX_GPT_MODEL_URI"),
        ),
        gsheet=GSheet(
            creds_path=env.str("GSHEET_CREDS_PATH"),
            spreadsheet_id=env.str("GSHEET_SPREADSHEET_ID"),
        ),
        redis=Redis(
            host=env.str("REDIS_HOST"),
            port=env.int("REDIS_PORT"),
            db=env.int("REDIS_DB"),
        ),
    )


config = get_config(".env")

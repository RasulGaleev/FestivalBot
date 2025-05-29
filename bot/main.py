import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from core.config import config
from core.handlers import register_client_handlers
from core.services import YandexGPT, GSheet


async def main():
    logging.basicConfig(
        level=logging.INFO,
        # filename="bot.log",
        format="%(asctime)s - [%(levelname)s]: %(message)s",
    )

    redis = Redis(db=config.redis.db, host=config.redis.host, port=config.redis.port)

    dp = Dispatcher(storage=RedisStorage(redis=redis))
    register_client_handlers(dp)

    yandex_gpt = YandexGPT(token=config.yandex_gpt.token, model_uri=config.yandex_gpt.model_uri)
    gsheet = GSheet(creds_path=config.gsheet.creds_path, spreadsheet_id=config.gsheet.spreadsheet_id, redis=redis)
    await gsheet.authorize()

    bot = Bot(token=config.bot.token)

    try:
        await dp.start_polling(bot, redis=redis, yandex_gpt=yandex_gpt, gsheet=gsheet)
    except (KeyboardInterrupt, SystemExit):
        logging.info('Бот остановлен!')
    except Exception as e:
        logging.error(f'Неизвестная ошибка: {e}')


if __name__ == '__main__':
    asyncio.run(main())

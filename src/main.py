import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from logger import init_logger
from messages import WELCOME_MESSAGE

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    id = message.from_user.id if message.from_user is not None and hasattr(
        message.from_user, 'id') else 'unknown'
    logging.info(f'Got a message from user with id: {id}. '
                 f'Message text: {message.text}')
    await message.answer(WELCOME_MESSAGE)


async def main() -> None:
    logging.info('Bot is starting...')
    BOT_TOKEN = getEnv()
    bot_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(BOT_TOKEN, default=bot_properties)
    await dp.start_polling(bot)  # type: ignore


def getEnv():
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if not BOT_TOKEN:
        sys.exit('BOT_TOKEN is not provided!\n'
                 'Specify BOT_TOKEN variable in .env file')

    return BOT_TOKEN


if __name__ == '__main__':
    init_logger()
    asyncio.run(main())

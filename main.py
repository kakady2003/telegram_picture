import asyncio
import logging

from aiogram.filters import CommandStart

from config import config
from aiogram import  Dispatcher, types, Bot

dp = Dispatcher()
bot = Bot(token=config.BOT_TOKEN)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hi")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

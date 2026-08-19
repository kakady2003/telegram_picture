import asyncio
import logging
from fastapi import FastAPI
from aiogram.filters import CommandStart
from users.router import router as user_router
from config import config
from aiogram import  Dispatcher, types, Bot

app = FastAPI()

dp = Dispatcher()
bot = Bot(token=config.BOT_TOKEN)

app.include_router(user_router)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hi")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

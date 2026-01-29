import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from aiogram import Bot, Dispatcher

from tg_app import commanbot

async def main():
    bot = Bot(token='')
    dp = Dispatcher()
    dp.include_router(commanbot.router_main)
    await dp.start_polling(bot)
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот выключен")
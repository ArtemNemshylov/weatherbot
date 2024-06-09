import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from os import getenv
from bot.handlers import user_commands, callback
import fasteners
import logging
from dotenv import load_dotenv

load_dotenv()

lock = fasteners.InterProcessLock(getenv('LOCK_PATH'))


async def main():
    logging.basicConfig(level=logging.INFO)  # на проде нужно выключить, бо ест много ресурсов
    bot = Bot(token=getenv('BOT_TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(user_commands.handlers_router)
    dp.include_router(callback.callback_router)

    with lock:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

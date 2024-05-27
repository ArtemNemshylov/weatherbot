from aiogram import Bot, Dispatcher
import os
from bot.handlers import user_commands


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher(bot)

    dp.include_router(user_commands.router)



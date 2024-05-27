import asyncio

from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == 'Привет')
async def cmd_start(message: Message):
    await message.answer('Привет, я бот')

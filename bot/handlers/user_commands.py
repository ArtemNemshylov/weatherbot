from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.types import Message

from bot.data.database_operations import inset_users
from bot.keyboards.markups import start_keyboard

handlers_router = Router()


@handlers_router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет, я бот', reply_markup=start_keyboard())


@handlers_router.message(F.location)
async def write_coords(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await inset_users(message.from_user.id, latitude, longitude)
    await message.answer('ваша локація збережена', reply_markup=start_keyboard())




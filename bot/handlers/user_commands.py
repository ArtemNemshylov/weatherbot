from aiogram import F, Router
from aiogram.types import Message
from bot.data.database_module import inset_users

handlers_router = Router()


@handlers_router.message(F.text == 'Привет')
async def cmd_start(message: Message):
    await message.answer('Привет, я бот')


@handlers_router.message(F.location)
async def cmd_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await inset_users(message.from_user.id, latitude, longitude)
    await message.answer(f'Ваши координаты: {latitude}, {longitude}')

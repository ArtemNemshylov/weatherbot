from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.markups import send_geo
from bot.middlewares.weather.forecast import get_forecast

callback_router = Router()


@callback_router.callback_query(F.data == 'geo')
async def geo(callback: CallbackQuery):
    await callback.message.answer('Відправ мені свою геолокацію щоб я міг знайти місто', reply_markup=send_geo())


@callback_router.callback_query(F.data == 'forecast')
async def forecast(callback: CallbackQuery):
    daily_forecast = await get_forecast(callback.from_user.id)
    await callback.message.answer(daily_forecast)

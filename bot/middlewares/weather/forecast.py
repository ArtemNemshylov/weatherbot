from os import getenv

import requests
from dotenv import load_dotenv

from bot.data.database_operations import get_coords

load_dotenv()


async def get_forecast(telegram_id):
    coords = await get_coords(telegram_id)
    lon, lat = coords[0], coords[1]
    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&'
           f'appid={getenv("API_TOKEN")}&units=metric')

    response = requests.get(url).json()
    temperature = response['main']['temp']
    clouds = response['weather'][0]['description']
    wind_speed = response['wind']['speed']
    city = response['name']
    print(response)
    return f'У вашому місті - {temperature} градусів'

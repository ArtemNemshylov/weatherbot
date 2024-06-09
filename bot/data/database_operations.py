from sqlalchemy import update, insert
from sqlalchemy.future import select

from bot.data.database_module import async_session, Users


# Асинхронная функция для вставки или обновления пользователя
async def inset_users(telegram_id, latitude, longitude):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                select(Users).where(Users.c.telegram_id == str(telegram_id))
            )
            user = result.fetchone()
            if user is None:
                stmt = insert(Users).values(
                    telegram_id=telegram_id, latitude=latitude, longitude=longitude
                )
                await session.execute(stmt)
            else:
                stmt = update(Users).where(Users.c.telegram_id == str(telegram_id)).values(
                    latitude=latitude, longitude=longitude
                )
                await session.execute(stmt)


# Асинхронная функция для получения координат пользователя
async def get_coords(telegram_id):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                select(Users.c.latitude, Users.c.longitude).where(Users.c.telegram_id == str(telegram_id))
            )
            coords = result.fetchone()
            if coords:
                return coords.latitude, coords.longitude
            else:
                return None

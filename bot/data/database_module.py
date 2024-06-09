from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()

# Создаем асинхронный движок
engine = create_async_engine(getenv("SQLALCHEMY_ENGINE"), echo=True)

meta = MetaData()

# Определение таблицы
Users = Table(
    "users",
    meta,
    Column('id', Integer, primary_key=True),
    Column("telegram_id", String, unique=True),
    Column("latitude", String),
    Column("longitude", String),
)

# Асинхронный сессионный объект
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Асинхронная функция для работы с базой данных
async def async_main():
    # Создание всех таблиц, если они не существуют
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

    # Работа с сессией
    async with async_session() as session:
        async with session.begin():
            # Здесь могут быть запросы к базе данных, например, добавление пользователя
            # Например, session.add(...)
            pass

if __name__ == '__main__':
    asyncio.run(async_main())

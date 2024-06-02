from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from dotenv import load_dotenv
from os import getenv

load_dotenv()

engine = create_engine(getenv("SQLALCHEMY_ENGINE"), echo=True)
conn = engine.connect()
meta = MetaData()

users = Table(
    "users",
    meta,
    Column('id', Integer, primary_key=True),
    Column("telegram_id", String, unique=True),
    Column("latitude", String),
    Column("longitude", String),
)


async def inset_users(telegram_id, latitude, longitude):
    conn.execute(users.insert().values(telegram_id=telegram_id, latitude=latitude, longitude=longitude))
    conn.commit()


if __name__ == '__main__':
    meta.create_all(engine)

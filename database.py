from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/warehouse_db"


engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, exppire_on_commit=False)


class Base(DeclarativeBase):
    pass

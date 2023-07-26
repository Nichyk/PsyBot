from typing import Union

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine as create_async_engine_
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return create_async_engine_(url=url, echo=True, encoding='utf-8', pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

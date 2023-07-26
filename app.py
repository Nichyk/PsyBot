from sqlalchemy.ext.asyncio import create_async_engine
from data import config
from utils.database import get_session_maker, proceed_schemas, BaseModel

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from handlers import dp
import logging


async def on_startup(dp):
    logging.basicConfig(level=logging.DEBUG)
    async_engine = create_async_engine(config.POSTGRES_URI)
    get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await set_default_commands(dp)
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

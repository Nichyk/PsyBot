from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from data import config

meta = MetaData()

BaseModel = declarative_base()

engine = create_async_engine(config.POSTGRES_URI)

Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

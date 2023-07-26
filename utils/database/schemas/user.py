import datetime

from sqlalchemy import Column, VARCHAR, DATE, BigInteger

from utils.database.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger(), unique=True, nullable=False, primary_key=True)

    name = Column(VARCHAR(32), unique=False, nullable=True)

    phone = Column(BigInteger(), unique=True, nullable=False)

    email = Column(VARCHAR(32), unique=True, nullable=False)

    reg_date = Column(DATE, default=datetime.date.today)

    def __str__(self):
        return f'<User: {self.user_id}'

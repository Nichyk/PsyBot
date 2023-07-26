from aiogram import types
from aiogram.dispatcher.filters import Command
from sqlalchemy import select

from keyboards import ikb_rules
from keyboards.default import kb_menu
from loader import dp
from states import UserStates
from utils.database import Session, User


@dp.message_handler(Command('start'))
@dp.message_handler(text='Перезапустить')
async def start(message: types.Message):
    async with Session() as session:
        async with session.begin():
            check = await session.execute(select(User).where(User.user_id == message.from_user.id))
            user_data = check.scalar()

            if user_data is None:
                await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                                     'Добро пожаловать в мой бот для записи на консультацию!\n\n'
                                     'Перед тем как перейти к регистрации, прошу ознакомиться с правилами ниже.\n'
                                     'Соблюдение правил является обязательным условием получения консультации.',
                                     reply_markup=ikb_rules)
            else:
                await message.answer(f'Привет, {user_data.name}!\n\n'
                                     f'Выбери, что ты хочешь сделать далее.', reply_markup=kb_menu)

    await UserStates.active.set()

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards import ikb_rules
from loader import dp
from states import UserStates


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                         'Добро пожаловать в мой бот для записи на консультацию!\n\n'
                         'Перед тем как перейти к регистрации, прошу ознакомиться с правилами ниже.\n'
                         'Соблюдение правил является обязательным условием получения консультации.',
                         reply_markup=ikb_rules)

    await UserStates.active.set()

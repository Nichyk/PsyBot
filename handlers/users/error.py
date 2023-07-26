from aiogram import types

from loader import dp
from states import UserStates


@dp.message_handler(state=UserStates.active)
async def command_error(message: types.Message):
    await message.answer(f'Команда {message.text} не существует, '
                         f'выберите один из предложенных вариантов.')


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer('Введи /start, чтобы продолжить работу')

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('stop'), state='*')
async def not_approve_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Работа с ботом завершена. Для начала новой сессии используйте команду /start',
                         reply_markup=types.ReplyKeyboardRemove())

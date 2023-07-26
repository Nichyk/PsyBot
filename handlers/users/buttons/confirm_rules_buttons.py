from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import ikb_register
from loader import dp
from states import UserStates


@dp.message_handler(text='Я согласен(на)', state=UserStates.active)
async def approve_rules(message: types.Message):
    await message.answer(f'Привет, я рада, что мы можем продолжить!', reply_markup=ikb_register)


@dp.message_handler(text='Я не согласен(на)', state=UserStates.active)
async def not_approve_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Работа с ботом завершена. Для начала новой сессии используйте команду /start',
                         reply_markup=types.ReplyKeyboardRemove())

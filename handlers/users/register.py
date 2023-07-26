from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


from keyboards import kb_cancel_reg, kb_restart
from loader import dp

from states import Register, UserStates
from utils.database import Session, User

SCOPES = ['https://www.googleapis.com/auth/calendar']


@dp.callback_query_handler(text='/register', state=UserStates.active)
async def register(call: CallbackQuery):
    await call.message.answer('Рада, что Вы здесь :)\n\n'
                              'Для записи на консультацию, мне необходимо получить Ваши контактные данные.\n'
                              'Для начала, укажите, пожалуйста, свое имя.', reply_markup=kb_cancel_reg)
    await Register.name.set()


@dp.message_handler(text='Отменить регистрацию', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Регистрация отменена.\n'
                         'Вы можете начать заново выполнив команду /start', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Register.name)
async def get_name(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name=answer)
    await message.answer(f'{answer}, укажите, пожалуйста, Ваш номер телефона для связи.', reply_markup=kb_cancel_reg)
    await Register.phone.set()


@dp.message_handler(state=Register.phone)
async def get_phone(message: types.Message, state: FSMContext):
    answer = message.text

    try:
        if answer.replace('+', '').isnumeric():
            await state.update_data(phone=answer)
            await message.answer(f'Укажите, пожалуйста, Ваш email для записи на консультацию.')
            await Register.email.set()
        else:
            await message.answer('Введите корректный номер телефона')
    except Exception:
        await message.answer('Введите корректный номер телефона', reply_markup=kb_cancel_reg)


@dp.message_handler(state=Register.email)
async def get_email(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(email=answer)

    data = await state.get_data()
    user = User(user_id=message.from_user.id, name=data.get('name'), phone=int(data.get('phone')),
                email=(data.get('email')))
    async with Session() as session:
        async with session.begin():
            session.add(user)

    await message.answer('Регистрация успешно завершена.', reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Теперь можно приступать к записи.\n'
                         'Для продолжения работы перезапустите бот нажав на кнопку', reply_markup=kb_restart)

    await state.finish()

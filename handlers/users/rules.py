from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards import kb_confirm_rules, kb_menu
from loader import dp
from states import UserStates


@dp.message_handler(Command('rules'), state=UserStates.active)
@dp.message_handler(text='Правила', state=UserStates.active)
async def rules(message: types.Message):
    await message.answer('Правила для ознакомления.', reply_markup=kb_menu)
    path = 'files/rules.pdf'
    try:
        with open(path, 'rb') as file:
            await message.answer_document(file)
    except Exception:
        await message.answer('Произошла ошибка при отправке файла')


@dp.callback_query_handler(text='/rules', state=UserStates.active)
async def send_rules(call: CallbackQuery):
    path = 'files/rules.pdf'
    try:
        with open(path, 'rb') as file:
            await call.message.answer_document(file)
    except Exception:
        await call.message.answer('Произошла ошибка при отправке файла')

    await call.message.answer('В случае, если Вы согласны с правилами, прошу подтвердить свой выбор нажав '
                              '"Я согласен(на)"\n\n'
                              'В ином случае, нажмите "Я не согласен(на)" и бот прекратит работу.',
                              reply_markup=kb_confirm_rules)



import webbrowser

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards import kb_menu
from loader import dp
from states import UserStates


@dp.message_handler(Command('networks'), state=UserStates.active)
@dp.message_handler(text='Подписаться', state=UserStates.active)
async def networks(message: types.Message):
    webbrowser.open('https://www.instagram.com')
    await message.answer('Ссылка успешно открылась в браузере.', reply_markup=kb_menu)

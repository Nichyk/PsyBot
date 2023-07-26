import webbrowser

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states import UserStates


@dp.message_handler(Command('networks'), state=UserStates.active)
async def networks():
    webbrowser.open('https://www.instagram.com')

from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    name = State()
    phone = State()
    email = State()
    sign_up_data = State()

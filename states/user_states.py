from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    active = State()
    stopped = State()


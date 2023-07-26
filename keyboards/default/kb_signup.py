from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_signup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Запись на консультацию'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

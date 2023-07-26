from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_restart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перезапустить'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

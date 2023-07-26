from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Записаться'),
        ],
        [
            KeyboardButton(text='Правила'),
        ],
        [
            KeyboardButton(text='Подписаться'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

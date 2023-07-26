from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_cancel_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отменить процесс регистрации'),
        ],
    ],
    resize_keyboard=True,
)

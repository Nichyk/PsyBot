from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_cancel_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отменить регистрацию'),
        ],
    ],
    resize_keyboard=True,
)

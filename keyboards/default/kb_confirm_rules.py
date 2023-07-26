from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_confirm_rules = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я согласен(на)'),
            KeyboardButton(text='Я не согласен(на)'),
        ],
    ],
    resize_keyboard=True,
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_register = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Регистрация', callback_data='/register'),
    ]
])

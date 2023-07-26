from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_signup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Запись на консультацию', callback_data='/signup'),
    ]
])

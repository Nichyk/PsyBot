from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_rules = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Правила', callback_data='/rules'),
    ]
])

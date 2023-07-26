
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp
from states import UserStates


@dp.message_handler(text='/calendar', state=UserStates.active)
async def cmd_calendar(message: types.Message, **kwargs):
    await message.answer('ok')
    # Получаем текущую дату
    now = datetime.now()

    # Создаем inline клавиатуру календаря
    calendar = InlineKeyboardMarkup(row_width=7)
    prev_month = now.month - 1 if now.month > 1 else 12
    prev_year = now.year - 1 if now.month == 1 else now.year
    calendar.add(InlineKeyboardButton("<<", callback_data=f"calendar,{prev_year},{prev_month}"))
    calendar.add(InlineKeyboardButton(now.strftime("%B %Y"), callback_data="ignore"))
    calendar.add(InlineKeyboardButton(">>", callback_data=f"calendar,{now.year},{now.month+1}"))

    # Получаем количество дней в текущем месяце
    days_in_month = (now.replace(month=now.month % 12 + 1, day=1) - now.replace(day=1)).days

    # Добавляем дни месяца в календарь
    for day in range(1, days_in_month + 1):
        calendar.add(InlineKeyboardButton(str(day), callback_data=f"calendar,{now.year},{now.month},{day}"))

    await message.reply("Выберите дату:", reply_markup=calendar)


@dp.callback_query_handler(lambda c: c.data.startswith('calendar'))
async def process_calendar(call: CallbackQuery, state: FSMContext, **kwargs):
    # Получаем выбранную дату из callback data
    _, year, month, day = call.data.split(',')

    # Преобразуем в числовые значения
    year, month, day = int(year), int(month), int(day)

    # Создаем объект даты из выбранной даты
    selected_date = datetime(year, month, day)

    # Отправляем сообщение с выбранной датой
    await call.message.answer(f"Вы выбрали дату: {selected_date.strftime('%Y-%m-%d')}")

    # Ответим на callback query, чтобы закрыть всплывающее окно с календарем
    await call.answer()

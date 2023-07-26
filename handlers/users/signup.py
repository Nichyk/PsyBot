from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from sqlalchemy import select, ScalarResult

from loader import dp
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from states import UserStates
from utils.database import Session, User

SCOPES = ['https://www.googleapis.com/auth/calendar']


@dp.message_handler(Command('signup'), state=UserStates.active)
async def get_sign(message: types.Message):
    async with Session() as session:
        async with session.begin():

            result = await session.execute(select(User.name).where(User.user_id == message.from_user.id))
            name = result.scalar()
            print(name)
            result = await session.execute(select(User.phone).where(User.user_id == message.from_user.id))
            phone = result.scalar()
            print(phone)
            result = await session.execute(select(User.email).where(User.user_id == message.from_user.id))
            email = result.scalar()
            print(email)

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': f'{name} test event',
            'location': 'Online',
            'description': f'Контакты для связи: {phone}',
            'start': {
                'dateTime': '2023-07-24T09:00:00',
                'timeZone': 'Asia/Tashkent',
            },
            'end': {
                'dateTime': '2023-07-24T12:00:00',
                'timeZone': 'Asia/Tashkent',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {'email': f'{email}'},
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')

    except HttpError as error:
        print(f'An error occurred: {error}')


@dp.callback_query_handler(text='/signup', state=UserStates.active)
async def get_sign(call: CallbackQuery, state=FSMContext):
    async with Session() as session:
        async with session.begin():
            result = await session.execute(select(User.name).where(User.user_id == call.message.from_user.id))
            name = result.scalar()
            result = await session.execute(select(User.phone).where(User.user_id == call.message.from_user.id))
            phone = result.scalar()
            result = await session.execute(select(User.email).where(User.user_id == call.message.from_user.id))
            email = result.scalar()
    # async with Session() as session:
    #     async with session.begin():
    #         result = await session.execute(select(User).where(User.user_id == call.message.from_user.id))
    #         user_data = result.scalar()
    #
    # print(user_data)
    #
    # if user_data:
    #     user = user_data.scalar_one()
    #
    # else:
    #     await call.message.answer('Вначале зарегистрируйтесь')



    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': f'{name} test event',
            'location': 'Online',
            'description': f'Контакты для связи: {phone}',
            'start': {
                'dateTime': '2023-07-24T09:00:00',
                'timeZone': 'Asia/Tashkent',
            },
            'end': {
                'dateTime': '2023-07-24T12:00:00',
                'timeZone': 'Asia/Tashkent',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {'email': f'{email}'},
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')

    except HttpError as error:
        print(f'An error occurred: {error}')

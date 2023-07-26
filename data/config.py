import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins_id = [
    465046603,
]

ip = os.getenv('ip')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = f'postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

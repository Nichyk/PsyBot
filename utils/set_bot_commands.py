from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бот'),
        types.BotCommand('sign_up', 'Записаться'),
        types.BotCommand('rules', 'Правила'),
        types.BotCommand('networks', 'Подписаться'),
        types.BotCommand('stop', 'Остановить выполнение бота'),
    ])

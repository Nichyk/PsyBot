from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бот'),
        types.BotCommand('rules', 'Правила'),
        types.BotCommand('signup', 'Записаться'),
        types.BotCommand('networks', 'Подписаться'),
        types.BotCommand('stop', 'Остановить выполнение бота'),
    ])

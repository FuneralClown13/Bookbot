import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, menu_handlers, other_handlers
from keyboards import set_main_menu


# Функция конфигурирования и запуска бота
async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(menu_handlers.router)
    dp.include_router(other_handlers.router)

    dp.startup.register(set_main_menu)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())

from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import LEXICON


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/library',
                   description=LEXICON['/library']),
        BotCommand(command='/contents',
                   description=LEXICON['/contents']),
        BotCommand(command='/book_marks',
                   description=LEXICON['/book_marks']),
        BotCommand(command='/setting',
                   description=LEXICON['/setting']),


    ]
    await bot.set_my_commands(main_menu_commands)
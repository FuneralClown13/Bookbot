from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON

router = Router()


@router.message(Command(commands='library'))
async def process_command_library(message: Message):
    await message.answer(text=LEXICON['/library'])


@router.message(Command(commands='contents'))
async def process_command_contents(message: Message):
    await message.answer(text=LEXICON['/contents'])


@router.message(Command(commands='book_marks'))
async def process_command_book_marks(message: Message):
    await message.answer(text=LEXICON['/book_marks'])

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards import create_pagination_keyboard
from icecream import ic
from database.database import db
from lexicon.lexicon import LEXICON
from services.file_handling import book

router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=create_pagination_keyboard(db['page'], len(book)))


@router.message(Command(commands='help'))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.callback_query(F.data.in_(['backward', 'forward']))
async def process_buttons_pagination(callback: CallbackQuery):
    page_number = db['page']
    edit_text_fl = False

    match ic(callback.data):
        case 'backward':
            if page_number - 1 > 0:
                db['page'] -= 1
                edit_text_fl = True
        case 'forward':
            if page_number + 1 < len(book):
                db['page'] += 1
                edit_text_fl = True

    ic(book[db['page']][:16])
    await callback.answer()
    if edit_text_fl:
        await callback.message.edit_text(book[db['page']],
                                         reply_markup=create_pagination_keyboard(db['page'], len(book)))


@router.callback_query()
async def process_button_add_mark(callback: CallbackQuery):
    ic(callback.data, db['page'])
    await callback.answer()

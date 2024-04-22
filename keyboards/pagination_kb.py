from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(page, len_book) -> InlineKeyboardMarkup:
    buttons = {
        'backward': LEXICON['backward'],
        'add_mark': f'{page}/{len_book}',
        'forward': LEXICON['forward'],

    }
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=text,
        callback_data=data) for data, text in buttons.items()]
                   )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

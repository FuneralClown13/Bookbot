import os
import re
import sys
from icecream import ic

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 650

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page = text[start:start+size]
    for i, s in enumerate(page[::-1]):
        if s in ',.!:;?':
            page = page[:size-i]
            break
    return page, len(page)


def create_page():
    ...


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        text = re.sub('\n{2,}', '\n\n', f.read())
        start = 0
        page_number = 1
        page, page_size = _get_part_text(text, start, PAGE_SIZE)
        while page_size:
            book[page_number] = page.lstrip()
            page_number += 1
            start += page_size
            page, page_size = _get_part_text(text, start, PAGE_SIZE)
    ic(f'book ready')


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))

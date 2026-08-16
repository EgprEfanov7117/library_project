from datetime import date

from models.book import Book


def test_book_str():
    book = Book(
        id=1,
        title="Война и мир",
        isbn="1234567890123",
        pages=500,
        price=1000.0,
        published_at=date(2020, 1, 1),
        is_available=True,
        author_id=1,
        publisher_id=1,
        author_name="Лев Толстой",
        publisher_name="Тестовое издательство"
    )

    result = str(book)

    assert result == (
        "ID: 1\n"
        "Название: Война и мир\n"
        "ISBN: 1234567890123\n"
        "Страниц: 500\n"
        "Стоимость: 1000.0 руб.\n"
        "Дата публикации: 2020-01-01\n"
        "Статус: True\n"
        "Автор: Лев Толстой\n"
        "Издание: Тестовое издательство"
    )
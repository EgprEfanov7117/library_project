from repositories.book_repository import BookRepository
from models.book import Book
from tests.conftest import get_test_connection

from datetime import date

def test_get_all(test_book):
    repository = BookRepository(get_test_connection)

    books = repository.get_all()

    assert len(books) == 1


def test_find_by_id(test_book):
    repository = BookRepository(get_test_connection)

    book = repository.find_by_id(test_book)

    assert book is not None
    assert book.id == test_book
    assert book.title == "Война и мир"
    assert book.isbn == "1234567890123"
    assert book.pages == 500
    assert book.price == 1000.00
    assert book.published_at == date(2020, 1, 1)
    assert book.is_available is True

def test_find_by_id_not_found():
    repository = BookRepository(get_test_connection)

    book = repository.find_by_id(999999)

    assert book is None

def test_add(test_author, test_publisher):
    repository = BookRepository(get_test_connection)

    book = Book(
        id=None,
        title="Преступление и наказание",
        isbn="9876543210987",
        pages=600,
        price=1200.00,
        published_at=date(1866, 1, 1),
        is_available=True,
        author_id=test_author,
        publisher_id=test_publisher,
    )

    repository.add(book)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                id,
                title,
                isbn,
                pages,
                price,
                published_at,
                is_available,
                author_id,
                publisher_id
            FROM books_join
            WHERE title = %s;
        """, (book.title,))

        row = cursor.fetchone()

        assert row is not None

        book_id = row[0]

        assert row[1:] == (
            "Преступление и наказание",
            "9876543210987",
            600,
            1200.00,
            date(1866, 1, 1),
            True,
            test_author,
            test_publisher,
        )

        cursor.execute(
            "DELETE FROM books_join WHERE id = %s;",
            (book_id,)
        )

    connection.commit()
    connection.close()

def test_update(test_book, test_author, test_publisher):
    repository = BookRepository(get_test_connection)

    book = repository.find_by_id(test_book)

    assert book is not None

    book.title = "Анна Каренина"
    book.isbn = "1111111111111"
    book.pages = 800
    book.price = 1500.00
    book.published_at = date(1878, 1, 1)
    book.is_available = False
    book.author_id = test_author
    book.publisher_id = test_publisher

    repository.update(book)

    updated_book = repository.find_by_id(test_book)

    assert updated_book is not None
    assert updated_book.title == "Анна Каренина"
    assert updated_book.isbn == "1111111111111"
    assert updated_book.pages == 800
    assert updated_book.price == 1500.00
    assert updated_book.published_at == date(1878, 1, 1)
    assert updated_book.is_available is False
    assert updated_book.author_id == test_author
    assert updated_book.publisher_id == test_publisher

def test_delete(test_author, test_publisher):
    repository = BookRepository(get_test_connection)

    book = Book(
        id=None,
        title="Книга для удаления",
        isbn="5555555555555",
        pages=300,
        price=500.00,
        published_at=date(2020, 1, 1),
        is_available=True,
        author_id=test_author,
        publisher_id=test_publisher,
    )

    repository.add(book)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id
            FROM books_join
            WHERE title = %s;
        """, (book.title,))

        row = cursor.fetchone()

    connection.close()

    assert row is not None

    book_id = row[0]

    repository.delete(book_id)

    deleted_book = repository.find_by_id(book_id)

    assert deleted_book is None
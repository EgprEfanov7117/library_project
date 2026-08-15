import pytest 
import psycopg
from unittest.mock import Mock

from validators.book_validator import BookValidator
from models.book import Book
from datetime import date


@pytest.fixture
def book_validator():
    author_repository = Mock()
    publisher_repository = Mock()

    return BookValidator(
        author_repository,
        publisher_repository
    )

@pytest.fixture
def valid_book():
    return Book(
        id=1,
        title="Война и мир",
        isbn="1234567890123",
        pages=500,
        price=1000.0,
        published_at=date(2020, 1, 1),
        is_available=True,
        author_id=1,
        publisher_id=1,
    )


def get_test_connection():
    return psycopg.connect(
        dbname="library_test",
        user="egor",
        host="localhost",
        port=5432
    )


@pytest.fixture
def db_connection():
    connection = get_test_connection()

    yield connection

    connection.close()


@pytest.fixture
def clean_authors():
    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM books_join;")
        cursor.execute("DELETE FROM authors;")
    
    connection.commit()
    connection.close()

@pytest.fixture
def db_connection():
    connection = get_test_connection()

    yield connection

    connection.close()

@pytest.fixture
def test_author(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO authors (name, birth_year, country)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (
            "Лев Толстой",
            1828,
            "Россия"
        ))

        author_id = cursor.fetchone()[0]

    db_connection.commit()

    yield author_id

    with db_connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM authors WHERE id = %s;",
            (author_id,)
        )

    db_connection.commit()

@pytest.fixture
def clean_publisher():
    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM books_join;")
        cursor.execute("DELETE FROM publishers;")
    
    connection.commit()
    connection.close()

@pytest.fixture
def test_publisher(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO publishers (name)
            VALUES (%s)
            RETURNING id;
        """, ("Тестовое издательство",))

        publisher_id = cursor.fetchone()[0]
    
    db_connection.commit()

    yield publisher_id

    with db_connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM publishers WHERE id = %s;",
            (publisher_id,)
        )

    db_connection.commit()
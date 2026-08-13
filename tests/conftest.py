import pytest 
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
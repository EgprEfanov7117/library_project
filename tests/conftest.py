import pytest 
from unittest.mock import Mock

from validators.book_validator import BookValidator

@pytest.fixture
def book_validator():
    author_repository = Mock()
    publisher_repository = Mock()

    return BookValidator(
        author_repository,
        publisher_repository
    )
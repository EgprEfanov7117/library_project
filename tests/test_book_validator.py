import pytest
from datetime import date, timedelta

from exception_library import EmptyBookTitleError, AuthorNotFound, PublisherNotFound


# ==========
#   TITLE
# ==========
@pytest.mark.parametrize(
    "title",
    [
        "",
        " ",
        "   ",
        "\t",
    ]
)
def test_invalid_book_title(book_validator, title):
    with pytest.raises(EmptyBookTitleError):
        book_validator._validate_title(title)

@pytest.mark.parametrize(
    "title",
    [
        "Война и мир",
        "Преступление и наказание",
        "Python для начинающих",
        "1984",
    ]
)
def test_valid_book_title(book_validator, title):
    book_validator._validate_title(title)

# ==========
#   ISBN
# ==========
@pytest.mark.parametrize(
    "isbn",
    [
        "123456789012",
        "12345678901234",
        "1234567890120000",
        "123456789012000000"
    ]   
)
def test_invalid_isbn(book_validator, isbn):
    with pytest.raises(ValueError):
        book_validator._validate_isbn(isbn)

@pytest.mark.parametrize(
    "isbn",
    [
        "1234567890123",
        "978-5-389-11342-8"
    ]
)
def test_valid_isbn(book_validator, isbn):
    book_validator._validate_isbn(isbn)

# ==========
#   PAGES
# ==========
@pytest.mark.parametrize(
    "pages",
    [
        -100,
        -1,
        0
    ]
)
def test_invalid_pages(book_validator, pages):
    with pytest.raises(ValueError):
        book_validator._validate_pages(pages)

@pytest.mark.parametrize(
    "pages",
    [
        1,
        100
    ]
)
def test_valid_pages(book_validator, pages):
    book_validator._validate_pages(pages)

# ==========
#   PRICE
# ==========
@pytest.mark.parametrize(
    "price",
    [
        0,
        -7,
        -7.7
    ]
)
def test_invalid_price(book_validator, price):
    with pytest.raises(ValueError):
        book_validator._validate_price(price)

@pytest.mark.parametrize(
    "price",
    [
        0.01,
        1,
        7,
        7.7
    ]
)
def test_valid_price(book_validator, price):
    book_validator._validate_price(price)

# ==========
#    DATE
# ==========
def test_future_published_date(book_validator):
    future_date = date.today() + timedelta(days=1)

    with pytest.raises(ValueError):
        book_validator._validate_date(future_date)


@pytest.mark.parametrize(
    "date",
    [
        date(2000, 1, 1),
        date(2020, 5, 15),
        date.today()
    ]
)
def test_valid_date(book_validator, date):
    book_validator._validate_date(date)

# ============
# AUTHOR BY ID 
# ============
def test_invalid_author_id(book_validator):
    book_validator.author_repository.find_by_id.return_value = None

    with pytest.raises(AuthorNotFound):
        book_validator._validate_author_by_id(999)
    
    book_validator.author_repository.find_by_id.assert_called_once_with(999) 

def test_valid_author_id(book_validator):
    book_validator.author_repository.find_by_id.return_value = object()

    book_validator._validate_author_by_id(1)

    book_validator.author_repository.find_by_id.assert_called_once_with(1) 

def test_none_author_id(book_validator):
    book_validator._validate_author_by_id(None)

    book_validator.author_repository.find_by_id.assert_not_called()

# ===============
# PUBLISHER BY ID
# ===============
def test_invalid_publisher_id(book_validator):
    book_validator.publisher_repository.find_by_id.return_value = None

    with pytest.raises(PublisherNotFound):
        book_validator._validate_publisher_by_id(999)
    
    book_validator.publisher_repository.find_by_id.assert_called_once_with(999)

def test_valid_publisher_id(book_validator):
    book_validator.publisher_repository.find_by_id.return_value = object()

    book_validator._validate_publisher_by_id(1)

    book_validator.publisher_repository.find_by_id.assers_called_once_with(1)

def test_none_publisher_id(book_validator):
    book_validator._validate_publisher_by_id(None)

    book_validator.publisher_repository.find_by_id.assert_not_called()
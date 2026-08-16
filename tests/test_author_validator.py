import pytest
from datetime import date

from models.author import Author
from validators.author_validator import AuthorValidator
from exception_library import EmptyNameError, EmptyCountryError


@pytest.fixture
def validator():
    return AuthorValidator()


@pytest.fixture
def valid_author():
    return Author(
        id=1,
        name="Лев Толстой",
        birth_year=1828,
        country="Россия"
    )


def test_valid_author(validator, valid_author):
    validator.validate(valid_author)


def test_empty_name(validator, valid_author):
    valid_author.name = ""

    with pytest.raises(EmptyNameError):
        validator.validate(valid_author)


def test_whitespace_name(validator, valid_author):
    valid_author.name = "   "

    with pytest.raises(EmptyNameError):
        validator.validate(valid_author)


def test_future_birth_year(validator, valid_author):
    valid_author.birth_year = date.today().year + 1

    with pytest.raises(ValueError):
        validator.validate(valid_author)


def test_empty_country(validator, valid_author):
    valid_author.country = ""

    with pytest.raises(EmptyCountryError):
        validator.validate(valid_author)


def test_whitespace_country(validator, valid_author):
    valid_author.country = "   "

    with pytest.raises(EmptyCountryError):
        validator.validate(valid_author)
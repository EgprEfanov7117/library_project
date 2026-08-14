import pytest
from unittest.mock import Mock

from exception_library import BookNotFound
from services.book_service import BookService

def test_get_all():
    repository = Mock()
    validator = Mock()

    books = [
        Mock(),
        Mock(),
        Mock()
    ]

    repository.get_all.return_value = books

    service = BookService(repository, validator)

    result = service.get_all()

    assert result == books



def test_find_by_id():
    repository = Mock()
    validator = Mock()

    book = Mock()
    repository.find_by_id.return_value = book

    service = BookService(repository, validator)

    result = service.find_by_id(1)

    assert result == book 
    repository.find_by_id.assert_called_once_with(1)

def test_find_by_id_not_found():
    repository = Mock()
    validator = Mock()

    repository.find_by_id.return_value = None

    service = BookService(repository, validator)
    
    with pytest.raises(BookNotFound):
        service.find_by_id(999)
    
    repository.find_by_id.assert_called_once_with(999)

def test_add():
    repository = Mock()
    validator = Mock()

    book = Mock()

    service = BookService(repository, validator)

    service.add(book)

    repository.add.assert_called_once_with(book)
    validator.validate.assert_called_once_with(book)

def test_add_validation_error():
    repository = Mock()
    validator = Mock()

    book = Mock()

    validator.validate.side_effect = ValueError("Ошибка валидации")
    
    service = BookService(repository, validator)

    with pytest.raises(ValueError):
        service.add(book)
    
    validator.validate.assert_called_once_with(book)
    repository.add.assert_not_called()

def test_update():
    repository = Mock()
    validator = Mock()

    book = Mock()
    book.id = 1

    repository.find_by_id.return_value = book

    service = BookService(repository, validator)

    service.update(book)

    repository.find_by_id.assert_called_once_with(1)
    validator.validate.assert_called_once_with(book)
    repository.update.assert_called_once_with(book)

def test_update_book_not_found():
    repository = Mock()
    validator = Mock()

    repository.find_by_id.return_value = None

    book = Mock()
    book.id = 999

    service = BookService(repository, validator)

    with pytest.raises(BookNotFound):
        service.update(book)

    repository.find_by_id.assert_called_once_with(999)
    validator.validate.assert_not_called
    repository.update.assert_not_called

def test_update_validation_error():
    repository = Mock()
    validator = Mock()

    book = Mock()
    book.id = 1

    repository.find_by_id.return_value = book
    validator.validate.side_effect = ValueError("Ошибка валидации")

    service = BookService(repository, validator)

    with pytest.raises(ValueError):
        service.update(book)
    
    repository.find_by_id.assert_called_once_with(1)
    validator.validate.assert_called_once_with(book)
    repository.update.assert_not_called()

def test_dalete():
    repository = Mock()
    validator = Mock()

    book = Mock()
    repository.find_by_id.return_value = book

    service = BookService(repository, validator)
    service.delete(1)

    repository.find_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(1)

def test_delete_book_not_found():
    repository = Mock()
    validator = Mock()

    repository.find_by_id.return_value = None

    service = BookService(repository, validator)

    with pytest.raises(BookNotFound):
        service.delete(999)
    
    repository.find_by_id.assert_called_once_with(999)
    repository.delete.assert_not_called()
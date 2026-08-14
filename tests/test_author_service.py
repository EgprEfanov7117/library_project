import pytest
from unittest.mock import Mock

from services.author_service import AuthorService
from exception_library import AuthorNotFound

def test_get_all():
    repository = Mock()
    validator = Mock()

    authors = [
        Mock(),
        Mock(),
        Mock()
    ]

    repository.get_all.return_value = authors

    service = AuthorService(repository, validator)

    result = service.get_all()

    assert result == authors

def test_find_by_id():
    repository = Mock()
    validator = Mock()

    author = Mock()

    repository.find_by_id.return_value = author

    service = AuthorService(repository, validator)

    result = service.find_by_id(1)

    assert result == author
    repository.find_by_id.assert_called_once_with(1)

def test_find_by_id_author_not_found():
    repository = Mock()
    validator = Mock()

    repository.find_by_id.return_value = None 

    service = AuthorService(repository, validator)

    with pytest.raises(AuthorNotFound):
        service.find_by_id(999)
    
    repository.find_by_id.assert_called_once_with(999)
    
def test_add():
    repository = Mock()
    validator = Mock()

    author = Mock()

    service = AuthorService(repository, validator)

    service.add(author)

    validator.validate.assert_called_once_with(author)
    repository.add.assert_called_once_with(author)

def test_add_validation_error():
    repository = Mock()
    validator = Mock()

    author = Mock()

    validator.validate.side_effect = ValueError("Ошибка валидации")

    service = AuthorService(repository, validator)

    with pytest.raises(ValueError):
        service.add(author)
    
    validator.validate.assert_called_once_with(author)
    repository.add.assert_not_called()

def test_update():
    repository = Mock()
    validator = Mock()

    author = Mock()
    author.id = 1

    repository.find_by_id.return_value = author

    service = AuthorService(repository, validator)

    service.update(author)

    repository.find_by_id.assert_called_once_with(1)
    validator.validate.assert_called_once_with(author)
    repository.update.assert_called_once_with(author)

def test_update_author_not_found():
    repository = Mock()
    validator = Mock()

    author = Mock()
    author.id = 999

    repository.find_by_id.return_value = None
    
    service = AuthorService(repository, validator)

    with pytest.raises(AuthorNotFound):
        service.update(author)
    
    repository.find_by_id.assert_called_once_with(999)
    validator.validate.assert_not_called()
    repository.update.assert_not_called()

def test_update_validation_error():
    repository = Mock()
    validator = Mock()

    author = Mock()
    author.id = 1

    repository.find_by_id.return_value = author 
    validator.validate.side_effect = ValueError("Ошибка валидации")

    service = AuthorService(repository, validator)

    with pytest.raises(ValueError):
        service.update(author)
    
    repository.find_by_id.assert_called_once_with(1)
    validator.validate.assert_called_once_with(author)
    repository.update.assert_not_called()

def test_detele():
    repository = Mock()
    validator = Mock()

    author = Mock()
    author.id = 1

    repository.find_by_id.return_value = author

    service = AuthorService(repository, validator)

    service.delete(1)

    repository.find_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(1)

def test_delete_author_not_found():
    repository = Mock()
    validator = Mock()

    repository.find_by_id.return_value = None

    service = AuthorService(repository, validator)

    with pytest.raises(AuthorNotFound):
        service.delete(999)

    repository.find_by_id.assert_called_once_with(999)
    repository.delete.assert_not_called()
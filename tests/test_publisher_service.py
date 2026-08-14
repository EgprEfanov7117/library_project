import pytest
from unittest.mock import Mock

from services.publisher_service import PublisherService
from exception_library import PublisherNotFound, EmptyNameError

def test_get_all():
    repository = Mock()

    publishers = [
        Mock(),
        Mock(),
        Mock()
    ]

    repository.get_all.return_value = publishers

    service = PublisherService(repository)

    result = service.get_all()

    assert result == publishers
    repository.get_all.assert_called_once()

def test_find_by_id():
    repository = Mock()

    publisher = Mock()

    repository.find_by_id.return_value = publisher

    service = PublisherService(repository)

    result = service.find_by_id(1)

    assert result == publisher
    repository.find_by_id.assert_called_once_with(1)

def test_find_by_id_publisher_not_found():
    repository = Mock()

    repository.find_by_id.return_value = None 

    service = PublisherService(repository)

    with pytest.raises(PublisherNotFound):
        service.find_by_id(999)
    
    repository.find_by_id.assert_called_once_with(999)

def test_add():
    repository = Mock()

    publisher = Mock()
    publisher.name = "Егор"

    service = PublisherService(repository)

    service.add(publisher)

    repository.add.assert_called_once_with(publisher)

@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "   ",
        "\t",
    ]
)
def test_add_empty_name(name):
    repository = Mock()

    publisher = Mock()
    publisher.name = name
    
    service = PublisherService(repository)

    with pytest.raises(EmptyNameError):
        service.add(publisher)

    repository.add.assert_not_called()

def test_update():
    repository = Mock()

    publisher = Mock()
    publisher.id = 1
    publisher.name = "Егор"

    repository.find_by_id.return_value = publisher

    service = PublisherService(repository)

    service.update(publisher)

    repository.find_by_id.assert_called_once_with(1)
    repository.update.assert_called_once_with(publisher)

def test_update_publisher_not_found():
    repository = Mock()

    publisher = Mock()
    publisher.id = 999

    repository.find_by_id.return_value = None 

    service = PublisherService(repository)

    with pytest.raises(PublisherNotFound):
        service.update(publisher)
    
    repository.find_by_id.assert_called_once_with(999)
    repository.update.assert_not_called()

def test_update_empty_name():
    repository = Mock()

    publisher = Mock()
    publisher.name = ""
    publisher.id = 1

    repository.find_by_id.return_value = publisher

    service = PublisherService(repository)

    with pytest.raises(EmptyNameError):
        service.update(publisher)
    
    repository.find_by_id.assert_called_once_with(1)
    repository.update.assert_not_called()

def test_delete():
    repository = Mock()

    publisher = Mock()

    repository.find_by_id.return_value = publisher

    service = PublisherService(repository)

    service.delete(1)

    repository.find_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(1)

def test_delete_publisher_not_found():
    repository = Mock()

    repository.find_by_id.return_value = None

    service = PublisherService(repository)

    with pytest.raises(PublisherNotFound):
        service.delete(999)
    
    repository.find_by_id.assert_called_once_with(999)
    repository.delete.assert_not_called()



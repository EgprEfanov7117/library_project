from repositories.publisher_repository import PublisherRepository
from models.publisher import Publisher

from tests.conftest import get_test_connection

def test_get_all(clean_publisher):
    repository = PublisherRepository(get_test_connection)

    publishers = repository.get_all()

    assert publishers == []

def test_find_by_id(test_publisher):
    repository = PublisherRepository(get_test_connection)

    publisher = repository.find_by_id(test_publisher)

    assert publisher is not None
    assert publisher.id == test_publisher
    assert publisher.name == "Тестовое издательство"

def test_find_by_id_not_found(clean_publisher):
    repository = PublisherRepository(get_test_connection)

    publisher = repository.find_by_id(999999)

    assert publisher is None 

def test_add(clean_publisher):
    repository = PublisherRepository(get_test_connection)

    publisher = Publisher(
        id=None,
        name="Тестовое издательство"
    )

    repository.add(publisher)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name
            FROM publishers
            WHERE name = %s;
        """, (publisher.name,))

        row = cursor.fetchone()

    connection.close()

    assert row == (
        "Тестовое издательство",
    )

def test_update(test_publisher):
    repository = PublisherRepository(get_test_connection)

    publisher = repository.find_by_id(test_publisher)
    publisher.name = "Новое издательство"
    repository.update(publisher)

    update_publisher = repository.find_by_id(test_publisher)

    assert update_publisher.id == test_publisher
    assert update_publisher.name == "Новое издательство"

def test_delete(test_publisher):
    repository = PublisherRepository(get_test_connection)

    repository.delete(test_publisher)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id
            FROM publishers
            WHERE id = %s;
        """, (test_publisher,))
    
        row = cursor.fetchone()
    
    connection.close()

    assert row is None 
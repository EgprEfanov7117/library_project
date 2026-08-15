from repositories.author_repository import AuthorRepository
from models.author import Author
from tests.conftest import get_test_connection


def test_get_all(clean_authors):
    repository = AuthorRepository(get_test_connection)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO authors (name, birth_year, country)
            VALUES
                ('Лев Толстой', 1828, 'Россия'),
                ('Фёдор Достоевский', 1821, 'Россия');
        """)
    
    connection.commit()
    connection.close()

    authors = repository.get_all()

    assert len(authors) == 2
    assert authors[0].name == "Лев Толстой"
    assert authors[1].name == "Фёдор Достоевский"

def test_find_by_id(test_author):
    repository = AuthorRepository(get_test_connection)

    author = repository.find_by_id(test_author)

    assert author is not None
    assert author.id == test_author
    assert author.name == "Лев Толстой"
    assert author.birth_year == 1828
    assert author.country == "Россия"

def test_find_by_id_not_found(clean_authors):
    repository = AuthorRepository(get_test_connection)

    author = repository.find_by_id(999999)

    assert author is None

def test_add(clean_authors):
    repository = AuthorRepository(get_test_connection)

    author = Author(
        id=None,
        name="А.С. Пушкин",
        birth_year=1799,
        country="Россия"
    )

    repository.add(author)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name, birth_year, country
            FROM authors
            WHERE name = %s;
        """, (author.name,))

        row = cursor.fetchone()

    connection.close()

    assert row == (
        "А.С. Пушкин",
        1799,
        "Россия"
    )

def test_update(test_author):
    repository = AuthorRepository(get_test_connection)

    author = repository.find_by_id(test_author)

    author.name = "Лев Николаевич Толстой"
    author.birth_year = 1828
    author.country = "Россия"

    repository.update(author)

    updated_author = repository.find_by_id(test_author)

    assert updated_author.id == test_author
    assert updated_author.name == "Лев Николаевич Толстой"
    assert updated_author.birth_year == 1828
    assert updated_author.country == "Россия"

def test_delete(test_author):
    repository = AuthorRepository(get_test_connection)

    repository.delete(test_author)

    connection = get_test_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id
            FROM authors
            WHERE id = %s;
        """, (test_author,))

        row = cursor.fetchone()

    connection.close()

    assert row is None

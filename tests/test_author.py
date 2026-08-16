from models.author import Author


def test_author_str():
    author = Author(
        id=1,
        name="Лев Толстой",
        birth_year=1828,
        country="Россия"
    )

    result = str(author)

    assert result == (
        "ID: 1\n"
        "Имя: Лев Толстой\n"
        "Дата рождения: 1828\n"
        "Страна:Россия\n"
    )
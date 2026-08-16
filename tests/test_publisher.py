from models.publisher import Publisher


def test_publisher_str():
    publisher = Publisher(
        id=1,
        name="Тестовое издательство"
    )

    result = str(publisher)

    assert result == "ID: 1 | Имя: Тестовое издательство"
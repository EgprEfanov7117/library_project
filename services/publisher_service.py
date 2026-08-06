from models.publisher import Publisher
from repositories.publisher_repository import PublisherRepository
from database import get_connection
from exception_library import EmptyNameError

class PublisherService:
    
    def __init__(self):

        self.publisher_repository = PublisherRepository()
    
    def _validate_name(self, name: str) -> None:
        if not name.strip():
            raise EmptyNameError("Ошибка: Имя не может быть пустым")

    def get_all(self) -> list[Publisher]:

        return self.publisher_repository.get_all()

    def find_by_id(self, publisher_id: int) -> Publisher | None:

        publisher = self.publisher_repository.find_by_id(publisher_id)
        if publisher is None:
            raise ValueError()
        return publisher

    def add(self, publisher: Publisher) -> None:

        self._validate_name(publisher.name)
        self.publisher_repository.add(publisher)

    def update(self, publisher: Publisher) -> None:

        self._validate_name(publisher.name)
        self.publisher_repository.update(publisher)

    def delete(self, publisher_id: int) -> None:

        self.find_by_id(publisher_id)
        self.publisher_repository.delete(publisher_id)


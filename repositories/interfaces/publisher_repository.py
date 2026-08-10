from abc import ABC, abstractmethod
from models.publisher import Publisher

class PublisherRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Publisher]:
        pass

    @abstractmethod
    def find_by_id(self, publisher_id: int) -> Publisher | None:
        pass

    @abstractmethod
    def add(self, publisher: Publisher) -> None:
        pass

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        pass

    @abstractmethod
    def delete(self, publisher_id: int) -> None:
        pass
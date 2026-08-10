from abc import ABC, abstractmethod
from models.author import Author

class AuthorRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Author]:
        pass

    @abstractmethod
    def find_by_id(self, author_id: int) -> Author | None:
        pass

    @abstractmethod
    def add(self, author: Author) -> None:
        pass

    @abstractmethod
    def update(self, author: Author) -> None:
        pass

    @abstractmethod
    def delete(self, author_id: int) -> None:
        pass
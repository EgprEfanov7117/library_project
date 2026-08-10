from abc import ABC, abstractmethod
from models.book import Book

class BookRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Book]:
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Book | None:
        pass

    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass
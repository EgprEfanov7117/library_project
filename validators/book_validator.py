from models.book import Book
from repositories.author_repository import AuthorRepository
from repositories.publisher_repository import PublisherRepository
from datetime import date, datetime
from exception_library import (
    EmptyBookTitleError,
    AuthorNotFound,
    PublisherNotFound
)

class BookValidator:

    def __init__(self):
        self.author_repository = AuthorRepository
        self.publisher_repository = PublisherRepository()

    def _validate_title(self, title: str) -> None:
        if not title.strip():
            raise EmptyBookTitleError("Ошибка: Название книги не может быть пустым или состоять из пробелов")
    
    def _validate_isbn(self, isbn: str) -> None:
        if len(isbn) not in (13, 17):
            raise ValueError("Ошибка: Неверный формат ISBN")
        
    def _validate_pages(self, pages: int) -> None:
        if pages <= 0:
            raise ValueError("Ошибка: Количество страниц должно быть целым положительным числом")
    
    def _validate_price(self, price: float) -> None:
        if price <= 0:
            raise ValueError("Ошибка: Цена должна быть положительным числом")
    
    def _validate_date(self, published_date: date) -> None:
        if published_date > date.today():
            raise ValueError("Ошибка: Дата публикации не может быть в будущем")
    
    def _validate_author_by_id(self, author_id: int) -> None:
        if author_id is not None and self.author_repository.get_by_id(author_id) is None:
            raise AuthorNotFound("Ошибка: Автора с таким ID не существует")
    
    def _validate_publisher_by_id(self, publisher_id: int) -> None:
        if publisher_id is not None and self.publisher_repository.get_by_id(publisher_id) is None:
            raise PublisherNotFound("Ошибка: Издания с таким ID не существует")

    def validate(self, book: Book) -> None:
        
        self._validate_title(book.title)
        self._validate_isbn(book.isbn)
        self._validate_pages(book.pages)
        self._validate_price(book.price)
        self._validate_date(book.published_at)
        self._validate_author_by_id(book.author_id)
        self._validate_publisher_by_id(book.publisher_id)
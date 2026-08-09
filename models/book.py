from dataclasses import dataclass
from datetime import date
from services.author_service import AuthorService
from services.publisher_service import PublisherService

# id, title, isbn, pages, price, published_at, is_available, author_id, publisher_id
@dataclass
class Book:
    id: int
    title: str
    isbn: str
    pages: int
    price: float
    published_at: date
    is_available: bool
    author_id: int
    publisher_id:int
    author_name: str | None = None
    publisher_name: str | None = None


    def __str__(self):
        return f"ID: {self.id}\nНазвание: {self.title}\nISBN: {self.isbn}\nСтраниц: {self.pages}\nСтоимость: {self.price} руб.\nДата публикации: {self.published_at}\nСтатус: {self.is_available}\nАвтор: {self.author_name}\nИздание: {self.publisher_name}"
    

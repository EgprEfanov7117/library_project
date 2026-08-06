from dataclasses import dataclass
from datetime import date

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

    def __str__(self):
        return f"ID={self.id}, {self.title} ISBN:{self.isbn}, ({self.pages} стр.). Стоимость: {self.price} руб., Дата публикации: {self.published_at}, Статус: {self.is_available}, {self.author_id} {self.publisher_id}"
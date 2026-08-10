from repositories.book_repository import BookRepository
from models.book import Book
from validators.book_validator import BookValidator
from exception_library import BookNotFound
from repositories.interfaces.book_repository import BookRepositoryInterface

class BookService:

    def __init__(
            self,
            repository: BookRepositoryInterface,
            validator: BookValidator
    ):
        
        self.book_repository = repository
        self.book_validator = validator
        
    
    def get_all(self) -> list[Book]:
       return self.book_repository.get_all()
        
    def find_by_id(self, book_id: int) -> Book:
        book = self.book_repository.find_by_id(book_id)
        
        if book is None:
            raise BookNotFound("Ошибка: Книга не найдена")
        return book
    
    def add(self, book: Book) -> None:
        
        self.book_validator.validate(book)
        self.book_repository.add(book)
    
    def update(self, book: Book) -> None:
        
        self.find_by_id(book.id)
        self.book_validator.validate(book)
        self.book_repository.update(book)

    def delete(self, book_id: int) -> None:
        
        self.find_by_id(book_id)
        self.book_repository.delete(book_id)
    

        

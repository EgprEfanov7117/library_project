from models.author import Author
from repositories.author_repository import AuthorRepository
from validators.author_validator import AuthorValidator
from exception_library import AuthorNotFound

class AuthorService:
    
    def __init__(self):
        
        self.author_repository = AuthorRepository()
        self.author_validator = AuthorValidator()

    
    def get_all(self) -> list[Author]:
        return self.author_repository.get_all()

    def find_by_id(self, author_id: int) -> Author | None:
        
        author = self.author_repository.find_by_id(author_id)

        if author is None:
            raise AuthorNotFound("Ошибка: Автора с таким ID не существует")
        return author

    def add(self, author: Author) -> None:
        
        self.author_validator.validate(author)
        self.author_repository.add(author)

    def update(self, author: Author) -> None:
        
        self.author_validator.validate(author)
        self.author_repository.update(author)

    def delete(self, author_id: int) -> None:
        
        self.find_by_id(author_id)
        self.author_repository.delete(author_id)
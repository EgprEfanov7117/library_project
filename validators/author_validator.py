from models.author import Author
from datetime import date
from exception_library import EmptyNameError, EmptyCountryError



class AuthorValidator:

    def _validate_name(self, name: str) -> None:
        if not name.strip():
            raise EmptyNameError("Ошибка: Имя не может быть пустым")
    
    def _validate_year(self, year: int) -> None:
        if year > date.today().year:
            raise ValueError("Ошибка: Рождение автора не может быть датой из будущего")
    
    def _validate_country(self, country: str) -> None:
        if not country.strip():
            raise EmptyCountryError("Ошибка: Название страны не может быть пустым")
    
    def validate(self, author: Author) -> None:
        
        self._validate_name(author.name)
        self._validate_year(author.birth_year)
        self._validate_country(author.country)
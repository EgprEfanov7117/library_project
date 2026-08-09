from dataclasses import dataclass

@dataclass
class Author():
    id: int
    name: str
    birth_year: int
    country: str

    def __str__(self):
        return f"ID: {self.id}\nИмя: {self.name}\nДата рождения: {self.birth_year}\nСтрана:{self.country}\n"
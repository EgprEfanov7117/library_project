from dataclasses import dataclass

@dataclass
class Publisher:
    id: int
    name: str

    def __str__(self):
        return f"ID: {self.id} | Имя: {self.name}"
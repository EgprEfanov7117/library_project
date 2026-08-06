from dataclasses import dataclass

@dataclass
class Publisher:
    id: int
    name: str

    def __str__(self):
        return f"{self.id} | {self.name}"
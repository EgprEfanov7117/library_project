from models.author import Author

class AuthorMenu:

    def __init__(self, author_service):
        self.author_service = author_service
    
    def show(self) -> None:
        while True:
            print("\n+" + "-" * 38 + "+")
            print("|" + " " * 16 + "АВТОРЫ" + " " * 16 + "|")
            print("\n+" + "-" * 38 + "+")
            print("|    1. Показать всех авторов" + " " * 10 + "|")
            print("|    2. Найти автора по ID" + " " * 13 + "|")
            print("|    3. Добавить автора" + " " * 16 + "|")
            print("|    4. Изменить автора" + " " * 16 + "|")
            print("|    5. Удалить автора" + " " * 17 + "|")
            print("|    0. Назад" + " " * 26 + "|")
            print("\n+" + "-" * 38 + "+")

            choice = input("| Выберите действие: ")

            if choice == "1":
                self.show_all()
            elif choice == "2":
                print("Показ автора по ID пока в разработке.")
            elif choice == "3":
                print("Добавление автора пока в разработке.")
            elif choice == "4":
                print("Изменение автора пока в разработке.")
            elif choice == "5":
                print("Удаление автора пока в разработке.")
            elif choice == "0":
                break
            else:
                print("\nОшибка: такого пункта меню нет.")

    def show_all(self) -> None:
        authors = self.author_service.get_all()

        if not authors:
            print("\n Авторов нет")
        
        sort = input("Сортировать? (y/n): ").strip().lower()

        if sort == "y":
            authors = self._sort_authors(authors)

        filter = input("Фильтровать? (y/n): ").strip().lower()

        if filter == "y":
            authors = self._filter_authors(authors)
        
        self._print_authors(authors)

    def _print_authors(self, authors: list[Author]) -> None:
        print("\n+" + "-" * 52 + "+")
        print(
            f"{'| ID':<5}"
            f"{'| Имя':<20}"
            f"{'| Страна':<25}"
        )
        print("\n+" + "-" * 52 + "+")

        for author in authors:
            print(
                f"{author.id:<5}"
                f"{author.name[:18]:<20}"
                f"{author.country[:23]:<25}"
            )
            
        print("\n+" + "-" * 52 + "+")
    
    def _sort_authors(self, authors: list[Author]) -> list[Author]:
        print("Сортировать по:")
        print(" 1. ID")
        print(" 2. Имени")
        print(" 0. Отмена")

        choice = input("Выберите поле: ").strip()

        sort_fields = {
            "1": lambda author: author.id,
            "2": lambda author: author.name.lower(),
        }

        if choice == "0":
            return authors
    
        if choice not in sort_fields:
            print("Ошибка: такого варианта сортировки нет.")
            return

        print("\nНаправление сортировки:")
        print(" 1. По возрастанию")
        print(" 2. По убыванию")

        direction = input("Выберите направление: ")

        if direction not in ("1", "2"):
            print("Ошибка: такого направления нет.")
            return authors

        reverse = direction == "2"

        return sorted(
            authors,
            key=sort_fields[choice],
            reverse=reverse
        )

    def _filter_authors(self, authors: list[Author]) -> list[Author]:
        print("Фильтровать по:")
        print(" 1. Дате рождения")
        print(" 0. Отмена")

        choice = input("Выберите поле: ").strip()

        if choice == "0":
            return authors
        
        if choice != "1":
            print("Ошибка: такого варианта фильтрации нет.")
        
        print("Сортировка по году рождения")
        try:
            min_year = int(input("От: "))
            max_year = int(input("До: "))
        except ValueError:
            print("Ошибка: год должен быть целым числом")
            return authors
        
        if min_year > max_year:
            print("Ошибка: минимальная год не может быть больше максимального")
            return authors
        
        return [
            author for author in authors
            if min_year <= author.birth_year <= max_year
        ]
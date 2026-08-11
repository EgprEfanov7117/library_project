from models.book import Book

class BookMenu:

    def __init__(self, book_service):
        self.book_service = book_service

    def show(self) -> None:
        while True:
            print("\n+" + "-" * 38 + "+")
            print("|" + " " * 17 + "КНИГИ" + " " * 16 + "|")
            print("\n+" + "-" * 38 + "+")
            print("|    1. Показать все книги" + " " * 26 + "|")
            print("|    2. Найти книгу по ID" + " " * 26 + "|")
            print("|    3. Добавить книгу" + " " * 26 + "|")
            print("|    4. Изменить книгу" + " " * 26 + "|")
            print("|    5. Удалить книгу" + " " * 26 + "|")
            print("|    0. Назад" + " " * 26 + "|")
            print("\n+" + "-" * 38 + "+")

            choice = input("| Выберите действие: ")

            if choice == "1":
                print("\nПоказ всех книг пока в разработке.")
            elif choice == "2":
                print("\nПоиск книги пока в разработке.")
            elif choice == "3":
                print("\nДобавление книги пока в разработке.")
            elif choice == "4":
                print("\nИзменение книги пока в разработке.")
            elif choice == "5":
                print("\nУдаление книги пока в разработке.")
            elif choice == "0":
                break
            else:
                print("\nОшибка: такого пункта меню нет.")

    def show_all(self) -> None:
        books = self.book_service.get_all()

        if not books:
            print("\nКниг нет.")
            return
        
        sort = input("\nСортировать? (y/n): ").lower()

        if sort == "y":
            print("Функция сортировки еще не реализвана")

        filter = input("\nФильтровать? (y/n): ").lower()

        if filter == "y":
            print("Функция фильтрации еще не реализована")

        self._print_books(books)
        
    def _print_books(self, books: list[Book]) -> None:
        print("\n+" + "-" * 103 + "+")
        print(
            f"{'| ID':<5}"
            f"{'| Название':<30}"
            f"{'| Автор':<25}"
            f"{'| Издательство':<20}"
            f"{'| Цена':<12}"
            f"{'| Доступна':<10}|"
        )
        print("\n+" + "-" * 102 + "+")

        for book in books:
            print(
                f"{book.id:<5}"
                f"{book.title[:28]:<30}"
                f"{book.author_name[:23]:<25}"
                f"{book.publisher_name[:18]:<20}"
                f"{str(book.price):<12}"
                f"{'Да' if book.is_available else 'Нет':<10}"
            )
        print("\n+" + "-" * 102 + "+")
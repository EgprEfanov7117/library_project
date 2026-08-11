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

    def _sort_books(self, books: list[Book]) -> list[Book]:
        print("Сортировать по: ")
        print(" 1. ID")
        print(" 2. Названию")
        print(" 3. Цене")
        print(" 4. Дате публикации")
        print(" 5. Количеству страниц")
        print(" 0. Отмена")

        choice = input("Выберите поле: ")

        sort_fields = {
            "1": lambda book: book.id,
            "2": lambda book: book.title.lower(),
            "3": lambda book: book.price,
            "4": lambda book: book.published_at,
            "5": lambda book: book.pages
        }

        if choice == "0":
            return books
        
        if choice not in sort_fields:
            print("Ошибка: такого варианта сортировки нет.")
            return books

        print("\nНаправление сортировки:")
        print(" 1. По возрастанию")
        print(" 2. По убыванию")

        direction = input("Выберите направление: ")

        if direction not in ("1", "2"):
            print("Ошибка: такого направления нет.")
            return books

        reverse = direction == "2"

        return sorted(
            books,
            key=sort_fields[choice],
            reverse=reverse
        )
    
    def _filte_books(self, books: list[Book]) -> list[Book]:
        print("\nФильтровать по:")
        print(" 1. Доступности")
        print(" 2. Автору")
        print(" 3. Издательству")
        print(" 4. Цене")
        print(" 5. Количеству страниц")
        print(" 0. Отмена")

        choice = input("Выберите поле: ")

        if choice == "0":
            return books
        
        if choice == "1":
            print("\n 1.Только доступные")
            print(" 2. Только не доступные")

            availability = input("Выберите вариант: ")

            if availability == "1":
                return [book for book in books if book.is_available]
            
            if availability == "2":
                return [book for book in books if not book.is_available]
            
            print("Ошибка: такого варианта нет.")
            return books

        if choice == "2":
            author_name = input("Введите имя автора: ").strip().lower()

            return [
                book for book in books 
                if author_name 
                and author_name in book.author_name.lower()
            ]
        
        if choice == "3":
            publisher_name = input("Введите название издательства: ").strip().lower()

            return [
                book for book in books
                if publisher_name
                and publisher_name in book.publisher_name.lower()
            ]
        
        if choice == "4":
            try:
                min_price = float(input("Введите минимальную цену: "))
                max_price = float(input("Введите максимальную цену: "))
            except ValueError:
                print("Ошибка: цена должна быть числом.")
                return books

            if min_price > max_price:
                print("Ошибка: минимальная цена не может быть больше максимальной.")
                return books
            
            return [
                book for book in books
                if min_price <= book.price <= max_price
            ]

        if choice == "5":
            try:
                min_pages = int(input("Введите минимальное количество страниц: "))
                max_pages = int(input("Введите максимальное количество страниц: "))
            except ValueError:
                print("Ошибка: количество страниц должно быть целым числом.")
                return books

            if min_pages > max_pages:
                print("Ошибка: минимальное количество страниц не может быть больше максимального.")
                return books
            
            return [
                book for book in books
                if min_pages <= book.pages <= max_pages
            ]
        
        print("Ошибка: такого варианта фильрации нет.")
        return books
    
    
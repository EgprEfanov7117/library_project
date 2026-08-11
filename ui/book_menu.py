
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
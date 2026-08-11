
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
                print("Показ всех авторов пока в разработке.")
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
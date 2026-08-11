
class PublisherMenu:

    def __init__(self, publisher_service):
        self.publisher_service = publisher_service

    def show():
        while True:
            print("\n+" + "-" * 38 + "+")
            print("|" + " " * 13 + "ИЗДАТЕЛЬСТВА" + " " * 13 + "|")
            print("\n+" + "-" * 38 + "+")
            print("|    1. Показать всех издательств" + " " * 6 + "|")
            print("|    2. Найти издательство по ID" + " " * 7 + "|")
            print("|    3. Добавить издательство" + " " * 10 + "|")
            print("|    4. Изменить издательство" + " " * 10 + "|")
            print("|    5. Удалить издательство" + " " * 11 + "|")
            print("|    0. Назад" + " " * 26 + "|")
            print("\n+" + "-" * 38 + "+")

            choice = input("| Выберите действие: ")

            if choice == "1":
                print("Показ всех издательств пока в разработке.")
            elif choice == "2":
                print("Показ издательства по ID пока в разработке.")
            elif choice == "3":
                print("Добавление издательства пока в разработке.")
            elif choice == "4":
                print("Изменение издательства пока в разработке.")
            elif choice == "5":
                print("Удаление издательства пока в разработке.")
            elif choice == "0":
                break
            else:
                print("\nОшибка: такого пункта меню нет.")
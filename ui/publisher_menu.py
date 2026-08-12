from models.publisher import Publisher

class PublisherMenu:

    def __init__(self, publisher_service):
        self.publisher_service = publisher_service

    def show(self) -> None:
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
                self.show_all()
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
    
    def show_all(self) -> None:
        publishers = self.publisher_service.get_all()

        if not publishers:
            print("\nИздательств нет.")
            return
        
        sort = input("\nСортировать? (y/n): ").lower()

        if sort == "y":
            publishers = self._sort_publisher(publishers)
        
        self._print_publishers(publishers)

    def _print_publishers(self, publishers: list[Publisher]) -> None:
        print("\n+" + "-" * 40 + "+")
        print(
            f"{'| ID':<5}"
            f"{'| Название':<30}"
        )
        print("\n+" + "-" * 40 + "+")

        for publisher in publishers:
            print(
                f"{publisher.id:<5}"
                f"{publisher.name[:28]:<30}"
            )
        print("\n+" + "-" * 40 + "+")
    
    def _sort_publisher(self, publishers: list[Publisher]) -> list[Publisher]:
        print("Сортировать по: ")
        print(" 1. ID")
        print(" 2. Названию")
        print(" 0. Отмена")

        choice = input("Выберите поле: ")

        sort_fields = {
            "1": lambda publisher: publisher.id,
            "2": lambda publisher: publisher.title.lower()
        }

        if choice == "0":
            return publishers
        
        if choice not in sort_fields:
            print("Ошибка: такого варианта сортировки нет.")
            return publishers

        print("\nНаправление сортировки:")
        print(" 1. По возрастанию")
        print(" 2. По убыванию")

        direction = input("Выберите направление: ")

        if direction not in ("1", "2"):
            print("Ошибка: такого направления нет.")
            return publishers

        reverse = direction == "2"

        return sorted(
            publishers,
            key=sort_fields[choice],
            reverse=reverse
        )
    
    
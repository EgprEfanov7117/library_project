
class MainMenu:

    def __init__(
            self,
            book_menu,
            author_menu,
            publisher_menu
    ):
        self.book_menu = book_menu
        self.author_menu = author_menu
        self.publisher_menu = publisher_menu
    
    def show(self) -> None:
        while True:
            print("\n+" + "-" * 38 + "+")
            print("|" + " " * 14 + "БИБЛИОТЕКА" + " " * 14 + "|")
            print("\n+" + "-" * 38 + "+")
            print("|    1. Книги" + " " * 26 + "|")
            print("|    2. Авторы" + " " * 25 + "|")
            print("|    3. Издательства" + " " * 19 + "|")
            print("|    0. Выход" + " " * 26 + "|")
            print("\n+" + "-" * 38 + "+")

            choice = input("| Выберите действие: ")

            if choice == "1":
                self.book_menu.show()
            elif choice == "2":
                self.author_menu.show()
            elif choice == "3":
                self.publisher_menu.show()
            elif choice == "0":
                print("\nДо свидания!")
                break
            else:
                print("\nОшибка: такого пункта меню нет.")
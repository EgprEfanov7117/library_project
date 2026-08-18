from ui.ui_helpers import (
    console,
    show_screen,
    show_error,
    ask_choice,
    wait_for_enter,
    PRIMARY_COLOR
)

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
            console.clear()

            show_screen(
                title="📚 LIBRARY SYSTEM",
                subtitle="Система управления библиотекой",
                options=[
                    ("1", "Книги"),
                    ("2", "Авторы"),
                    ("3", "Издательства"),
                    ("0", "Выход"),
                ],
            )

            choice = ask_choice("Выберите раздел")

            if choice == "1":
                self.book_menu.show()

            elif choice == "2":
                self.author_menu.show()

            elif choice == "3":
                self.publisher_menu.show()

            elif choice == "0":
                console.print(
                    f"\n[bold {PRIMARY_COLOR}]До свидания! 👋[/bold {PRIMARY_COLOR}]"
                )
                break

            else:
                show_error("Некорректный выбор.")
                wait_for_enter()
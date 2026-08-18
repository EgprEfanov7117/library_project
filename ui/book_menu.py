from datetime import date

from models.book import Book
from exception_library import LibraryError, BookNotFound
from ui.ui_helpers import (
    console,
    show_screen,
    show_options,
    show_success,
    show_error,
    show_warning,
    show_info,
    ask_choice,
    ask_text,
    ask_int,
    ask_float,
    ask_date,
    ask_confirmation,
    wait_for_enter,
    create_table,
)


class BookMenu:

    def __init__(self, book_service):
        self.book_service = book_service

    def show(self) -> None:
        while True:
            console.clear()

            show_screen(
                title="КНИГИ",
                options=[
                    ("1", "Показать все книги"),
                    ("2", "Найти книгу по ID"),
                    ("3", "Добавить книгу"),
                    ("4", "Изменить книгу"),
                    ("5", "Удалить книгу"),
                    ("0", "Назад"),
                ],
            )

            choice = ask_choice(
                "Выберите действие",
                choices=["1", "2", "3", "4", "5", "0"],
                show_choices=False,
            )

            if choice == "1":
                self.show_all()
            elif choice == "2":
                self.find_by_id()
            elif choice == "3":
                self.add()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete()
            elif choice == "0":
                break

    def show_all(self) -> None:
        books = self.book_service.get_all()

        if not books:
            show_warning("Книг нет.")
            wait_for_enter()
            return

        sort_info = None
        filter_info = None

        if ask_confirmation("Сортировать?"):
            books, sort_info = self._sort_books(books)

        if ask_confirmation("Фильтровать?"):
            books, filter_info = self._filter_books(books)

        console.clear()

        show_screen(
            title="КНИГИ",
            options=[
                ("1", "Показать все книги"),
                ("2", "Найти книгу по ID"),
                ("3", "Добавить книгу"),
                ("4", "Изменить книгу"),
                ("5", "Удалить книгу"),
                ("0", "Назад"),
            ],
        )

        if sort_info:
            show_info(sort_info)

        if filter_info:
            show_info(filter_info)

        self._print_books(books)
        wait_for_enter()

    def find_by_id(self) -> None:
        book_id = ask_int("Введите ID книги для поиска")

        try:
            book = self.book_service.find_by_id(book_id)
        except BookNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=[
                    "ID",
                    "Название",
                    "Автор",
                    "Издательство",
                    "Цена",
                    "Доступна",
                ],
                rows=[[
                    str(book.id),
                    book.title,
                    book.author_name,
                    book.publisher_name,
                    str(book.price),
                    "Да" if book.is_available else "Нет",
                ]],
                title="Книга найдена",
            )
        )

        wait_for_enter()

    def add(self) -> None:
        title = ask_text("Введите название книги")
        isbn = ask_text("Введите ISBN книги")
        pages = ask_int("Введите количество страниц")
        price = ask_float("Введите цену книги")
        published_at = ask_date(
            "Введите дату публикации (ГГГГ-ММ-ДД)"
        )
        author_id = ask_int("Введите ID автора")
        publisher_id = ask_int("Введите ID издательства")

        is_available = ask_confirmation("Книга доступна?")

        book = Book(
            id=0,
            title=title,
            isbn=isbn,
            pages=pages,
            price=price,
            published_at=published_at,
            is_available=is_available,
            author_id=author_id,
            publisher_id=publisher_id,
        )

        try:
            self.book_service.add(book)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Книга успешно добавлена.")
        wait_for_enter()

    def update(self) -> None:
        book_id = ask_int("Введите ID книги")

        try:
            book = self.book_service.find_by_id(book_id)
        except BookNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=[
                    "ID",
                    "Название",
                    "Автор",
                    "Издательство",
                    "Цена",
                    "Доступна",
                ],
                rows=[[
                    str(book.id),
                    book.title,
                    book.author_name,
                    book.publisher_name,
                    str(book.price),
                    "Да" if book.is_available else "Нет",
                ]],
                title="Текущие данные книги",
            )
        )

        show_warning(
            "Чтобы оставить значение без изменения, нажмите Enter."
        )

        title = ask_text(
            f"Название [{book.title}]"
        )

        isbn = ask_text(
            f"ISBN [{book.isbn}]"
        )

        pages_input = ask_text(
            f"Количество страниц [{book.pages}]"
        )

        price_input = ask_text(
            f"Цена [{book.price}]"
        )

        published_at_input = ask_text(
            f"Дата публикации [{book.published_at}]"
        )

        availability_input = ask_choice(
            f"Доступна [{'y' if book.is_available else 'n'}]",
            choices=["y", "n", ""],
            show_choices=False,
        )

        author_id_input = ask_text(
            f"ID автора [{book.author_id}]"
        )

        publisher_id_input = ask_text(
            f"ID издательства [{book.publisher_id}]"
        )

        if title:
            book.title = title

        if isbn:
            book.isbn = isbn

        if pages_input:
            try:
                book.pages = int(pages_input)
            except ValueError:
                show_error(
                    "Количество страниц должно быть целым числом."
                )
                wait_for_enter()
                return

        if price_input:
            try:
                book.price = float(price_input)
            except ValueError:
                show_error("Цена должна быть числом.")
                wait_for_enter()
                return

        if published_at_input:
            try:
                book.published_at = date.fromisoformat(
                    published_at_input
                )
            except ValueError:
                show_error(
                    "Дата должна быть в формате ГГГГ-ММ-ДД."
                )
                wait_for_enter()
                return

        if availability_input:
            book.is_available = availability_input == "y"

        if author_id_input:
            try:
                book.author_id = int(author_id_input)
            except ValueError:
                show_error(
                    "ID автора должно быть целым числом."
                )
                wait_for_enter()
                return

        if publisher_id_input:
            try:
                book.publisher_id = int(publisher_id_input)
            except ValueError:
                show_error(
                    "ID издательства должно быть целым числом."
                )
                wait_for_enter()
                return

        try:
            self.book_service.update(book)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Книга успешно изменена.")
        wait_for_enter()

    def delete(self) -> None:
        book_id = ask_int(
            "Введите ID книги для удаления"
        )

        try:
            book = self.book_service.find_by_id(book_id)
        except BookNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=[
                    "ID",
                    "Название",
                    "Автор",
                    "Издательство",
                ],
                rows=[[
                    str(book.id),
                    book.title,
                    book.author_name,
                    book.publisher_name,
                ]],
                title="Книга для удаления",
            )
        )

        if not ask_confirmation(
            "Вы уверены, что хотите удалить эту книгу?"
        ):
            show_warning("Удаление отменено.")
            wait_for_enter()
            return

        try:
            self.book_service.delete(book_id)
        except BookNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Книга успешно удалена.")
        wait_for_enter()

    def _print_books(self, books: list[Book]) -> None:
        rows = [
            [
                str(book.id),
                book.title,
                book.author_name,
                book.publisher_name,
                str(book.price),
                "Да" if book.is_available else "Нет",
            ]
            for book in books
        ]

        table = create_table(
            columns=[
                "ID",
                "Название",
                "Автор",
                "Издательство",
                "Цена",
                "Доступна",
            ],
            rows=rows,
            title="Список книг",
        )

        console.print(table)

    def _sort_books(
        self,
        books: list[Book],
    ) -> tuple[list[Book], str | None]:

        show_options(
            title="СОРТИРОВКА",
            options=[
                ("1", "По ID"),
                ("2", "По названию"),
                ("3", "По цене"),
                ("4", "По дате публикации"),
                ("5", "По количеству страниц"),
                ("0", "Отмена"),
            ],
        )

        choice = ask_choice(
            "Выберите поле для сортировки",
            choices=["1", "2", "3", "4", "5", "0"],
            show_choices=False,
        )

        sort_fields = {
            "1": lambda book: book.id,
            "2": lambda book: book.title.lower(),
            "3": lambda book: book.price,
            "4": lambda book: book.published_at,
            "5": lambda book: book.pages,
        }

        if choice == "0":
            return books, None

        show_options(
            title="НАПРАВЛЕНИЕ СОРТИРОВКИ",
            options=[
                ("1", "По возрастанию"),
                ("2", "По убыванию"),
            ],
        )

        direction = ask_choice(
            "Выберите направление",
            choices=["1", "2"],
            show_choices=False,
        )

        sorted_books = sorted(
            books,
            key=sort_fields[choice],
            reverse=direction == "2",
        )

        field_name = {
            "1": "ID",
            "2": "названию",
            "3": "цене",
            "4": "дате публикации",
            "5": "количеству страниц",
        }

        direction_name = {
            "1": "по возрастанию",
            "2": "по убыванию",
        }

        sort_info = (
            f'Сортировка по "{field_name[choice]}" | '
            f"Направление: {direction_name[direction]}"
        )

        return sorted_books, sort_info

    def _filter_books(
        self,
        books: list[Book],
    ) -> tuple[list[Book], str | None]:

        show_options(
            title="ФИЛЬТРАЦИЯ",
            options=[
                ("1", "По доступности"),
                ("2", "По автору"),
                ("3", "По издательству"),
                ("4", "По цене"),
                ("5", "По количеству страниц"),
                ("0", "Отмена"),
            ],
        )

        choice = ask_choice(
            "Выберите поле для фильтрации",
            choices=["1", "2", "3", "4", "5", "0"],
            show_choices=False,
        )

        if choice == "0":
            return books, None

        if choice == "1":
            show_options(
                title="ДОСТУПНОСТЬ",
                options=[
                    ("1", "Только доступные"),
                    ("2", "Только недоступные"),
                ],
            )

            availability = ask_choice(
                "Выберите вариант",
                choices=["1", "2"],
                show_choices=False,
            )

            if availability == "1":
                filtered_books = [
                    book for book in books
                    if book.is_available
                ]
                filter_info = "Фильтр: только доступные книги"

            else:
                filtered_books = [
                    book for book in books
                    if not book.is_available
                ]
                filter_info = "Фильтр: только недоступные книги"

            return filtered_books, filter_info

        if choice == "2":
            author_name = ask_text(
                "Введите имя автора"
            ).strip().lower()

            if not author_name:
                return books, None

            filtered_books = [
                book
                for book in books
                if author_name in book.author_name.lower()
            ]

            return (
                filtered_books,
                f'Фильтр: автор содержит "{author_name}"',
            )

        if choice == "3":
            publisher_name = ask_text(
                "Введите название издательства"
            ).strip().lower()

            if not publisher_name:
                return books, None

            filtered_books = [
                book
                for book in books
                if publisher_name in book.publisher_name.lower()
            ]

            return (
                filtered_books,
                f'Фильтр: издательство содержит "{publisher_name}"',
            )

        if choice == "4":
            min_price = ask_float("Введите минимальную цену")
            max_price = ask_float("Введите максимальную цену")

            if min_price > max_price:
                show_error(
                    "Минимальная цена не может быть больше максимальной."
                )
                return books, None

            filtered_books = [
                book
                for book in books
                if min_price <= book.price <= max_price
            ]

            return (
                filtered_books,
                f"Фильтр: цена от {min_price} до {max_price}",
            )

        min_pages = ask_int(
            "Введите минимальное количество страниц"
        )
        max_pages = ask_int(
            "Введите максимальное количество страниц"
        )

        if min_pages > max_pages:
            show_error(
                "Минимальное количество страниц "
                "не может быть больше максимального."
            )
            return books, None

        filtered_books = [
            book
            for book in books
            if min_pages <= book.pages <= max_pages
        ]

        return (
            filtered_books,
            f"Фильтр: страниц от {min_pages} до {max_pages}",
        )
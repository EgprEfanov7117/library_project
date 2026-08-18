from models.author import Author
from exception_library import LibraryError, AuthorNotFound
from ui.ui_helpers import (
    console,
    show_screen,
    show_success,
    show_error,
    show_warning,
    show_options,
    show_info,
    ask_choice,
    ask_text,
    ask_int,
    ask_confirmation,
    wait_for_enter,
    create_table,
)


class AuthorMenu:

    def __init__(self, author_service):
        self.author_service = author_service

    def show(self) -> None:
        while True:
            console.clear()

            show_screen(
                title="АВТОРЫ",
                options=[
                    ("1", "Показать всех авторов"),
                    ("2", "Найти автора по ID"),
                    ("3", "Добавить автора"),
                    ("4", "Изменить автора"),
                    ("5", "Удалить автора"),
                    ("0", "Назад"),
                ]
            )

            choice = ask_choice("Выберите действие")

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
            else:
                show_error("Некорректный выбор.")
                wait_for_enter()

    def show_all(self) -> None:
        authors = self.author_service.get_all()

        if not authors:
            show_warning("Авторов нет.")
            wait_for_enter()
            return

        sort_info = None
        filter_info = None

        if ask_confirmation("Сортировать?"):
            authors, sort_info = self._sort_authors(authors)

        if ask_confirmation("Фильтровать?"):
            authors, filter_info = self._filter_authors(authors)

        console.clear()

        show_screen(
            title="АВТОРЫ",
            options=[
                ("1", "Показать всех авторов"),
                ("2", "Найти автора по ID"),
                ("3", "Добавить автора"),
                ("4", "Изменить автора"),
                ("5", "Удалить автора"),
                ("0", "Выход"),
            ],
        )

        if sort_info:
            show_info(sort_info)

        if filter_info:
            show_info(filter_info)

        self._print_authors(authors)
        wait_for_enter()

    def find_by_id(self) -> None:
        author_id = ask_int("Введите ID автора для поиска")

        try:
            author = self.author_service.find_by_id(author_id)
        except AuthorNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        table = create_table(
            columns=["ID", "Имя", "Год рождения", "Страна"],
            rows=[[
                str(author.id),
                author.name,
                str(author.birth_year),
                author.country,
            ]],
            title="Автор найден",
        )

        console.print(table)
        wait_for_enter()

    def add(self) -> None:
        name = ask_text("Введите имя автора")
        birth_year = ask_int("Введите год рождения")
        country = ask_text("Введите страну")

        author = Author(
            id=0,
            name=name,
            birth_year=birth_year,
            country=country,
        )

        try:
            self.author_service.add(author)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Автор успешно добавлен.")
        wait_for_enter()

    def update(self) -> None:
        author_id = ask_int("Введите ID автора")

        try:
            author = self.author_service.find_by_id(author_id)
        except AuthorNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=["ID", "Имя", "Год рождения", "Страна"],
                rows=[[
                    str(author.id),
                    author.name,
                    str(author.birth_year),
                    author.country,
                ]],
                title="Текущие данные",
            )
        )

        show_warning("Чтобы оставить значение без изменения, нажмите Enter.")

        name = ask_text(
            f"Имя [{author.name}]"
        )

        birth_year_input = ask_text(
            f"Год рождения [{author.birth_year}]"
        )

        country = ask_text(
            f"Страна [{author.country}]"
        )

        if name:
            author.name = name

        if birth_year_input:
            try:
                author.birth_year = int(birth_year_input)
            except ValueError:
                show_error("Год рождения должен быть целым числом.")
                wait_for_enter()
                return

        if country:
            author.country = country

        try:
            self.author_service.update(author)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Данные об авторе успешно изменены.")
        wait_for_enter()

    def delete(self) -> None:
        author_id = ask_int("Введите ID автора для удаления")

        try:
            author = self.author_service.find_by_id(author_id)
        except AuthorNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=["ID", "Имя", "Год рождения", "Страна"],
                rows=[[
                    str(author.id),
                    author.name,
                    str(author.birth_year),
                    author.country,
                ]],
                title="Автор для удаления",
            )
        )

        if not ask_confirmation(
            "Вы уверены, что хотите удалить этого автора?"
        ):
            show_warning("Удаление отменено.")
            wait_for_enter()
            return

        try:
            self.author_service.delete(author_id)
        except AuthorNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Автор успешно удалён.")
        wait_for_enter()

    def _print_authors(self, authors: list[Author]) -> None:
        rows = [
            [
                str(author.id),
                author.name,
                str(author.birth_year),
                author.country,
            ]
            for author in authors
        ]

        table = create_table(
            columns=["ID", "Имя", "Год рождения", "Страна"],
            rows=rows,
            title="Список авторов",
        )

        console.print(table)

    def _sort_authors(
        self,
        authors: list[Author],
    ) -> tuple[list[Author], str | None]:

        show_options(
            title="СОРТИРОВКА",
            options=[
                ("1", "По ID"),
                ("2", "По имени"),
                ("0", "Отмена"),
            ],
        )

        choice = ask_choice(
            "Выберите поле для сортировки",
            choices=["1", "2", "0"],
            show_choices=False,
        )

        sort_fields = {
            "1": lambda author: author.id,
            "2": lambda author: author.name.lower(),
        }

        if choice == "0":
            return authors, None

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

        field_name = {
            "1": "ID",
            "2": "имени",
        }

        direction_name = {
            "1": "по возрастанию",
            "2": "по убыванию",
        }

        sorted_authors = sorted(
            authors,
            key=sort_fields[choice],
            reverse=direction == "2",
        )

        info = (
            f'Сортировка по "{field_name[choice]}" | '
            f"Направление: {direction_name[direction]}"
        )

        return sorted_authors, info

    def _filter_authors(
        self,
        authors: list[Author],
    ) -> tuple[list[Author], str | None]:

        show_options(
            title="ФИЛЬТРАЦИЯ",
            options=[
                ("1", "По году рождения"),
                ("0", "Отмена"),
            ],
        )

        choice = ask_choice(
            "Выберите поле для фильтрации",
            choices=["1", "0"],
            show_choices=False,
        )

        if choice == "0":
            return authors, None

        min_year = ask_int("Введите минимальный год рождения")
        max_year = ask_int("Введите максимальный год рождения")

        if min_year > max_year:
            show_error(
                "Минимальный год не может быть больше максимального."
            )
            return authors, None

        filtered_authors = [
            author
            for author in authors
            if min_year <= author.birth_year <= max_year
        ]

        info = (
            f"Фильтр: год рождения от {min_year} до {max_year}"
        )

        return filtered_authors, info
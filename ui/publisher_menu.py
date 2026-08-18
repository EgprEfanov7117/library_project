from models.publisher import Publisher
from exception_library import LibraryError, PublisherNotFound
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
    ask_confirmation,
    wait_for_enter,
    create_table,
)


class PublisherMenu:

    def __init__(self, publisher_service):
        self.publisher_service = publisher_service

    def show(self) -> None:
        while True:
            console.clear()

            show_screen(
                title="ИЗДАТЕЛЬСТВА",
                options=[
                    ("1", "Показать всех издательств"),
                    ("2", "Найти издательство по ID"),
                    ("3", "Добавить издательство"),
                    ("4", "Изменить издательство"),
                    ("5", "Удалить издательство"),
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
        publishers = self.publisher_service.get_all()

        if not publishers:
            show_warning("Издательств нет.")
            wait_for_enter()
            return

        sort_info = None

        if ask_confirmation("Сортировать?"):
            publishers, sort_info = self._sort_publishers(publishers)

        console.clear()

        show_screen(
            title="ИЗДАТЕЛЬСТВА",
            options=[
                ("1", "Показать всех издательств"),
                ("2", "Найти издательство по ID"),
                ("3", "Добавить издательство"),
                ("4", "Изменить издательство"),
                ("5", "Удалить издательство"),
                ("0", "Назад"),
            ],
        )

        if sort_info:
            show_info(sort_info)

        self._print_publishers(publishers)
        wait_for_enter()

    def find_by_id(self) -> None:
        publisher_id = ask_int(
            "Введите ID издательства для поиска"
        )

        try:
            publisher = self.publisher_service.find_by_id(publisher_id)
        except PublisherNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        table = create_table(
            columns=["ID", "Название"],
            rows=[[
                str(publisher.id),
                publisher.name,
            ]],
            title="Издательство найдено",
        )

        console.print(table)
        wait_for_enter()

    def add(self) -> None:
        name = ask_text("Введите название издательства")

        publisher = Publisher(
            id=0,
            name=name,
        )

        try:
            self.publisher_service.add(publisher)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Издательство успешно добавлено.")
        wait_for_enter()

    def update(self) -> None:
        publisher_id = ask_int(
            "Введите ID издательства"
        )

        try:
            publisher = self.publisher_service.find_by_id(
                publisher_id
            )
        except PublisherNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=["ID", "Название"],
                rows=[[
                    str(publisher.id),
                    publisher.name,
                ]],
                title="Текущие данные",
            )
        )

        show_warning(
            "Чтобы оставить значение без изменения, нажмите Enter."
        )

        name = ask_text(
            f"Название [{publisher.name}]"
        )

        if name:
            publisher.name = name

        try:
            self.publisher_service.update(publisher)
        except LibraryError as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Издательство успешно изменено.")
        wait_for_enter()

    def delete(self) -> None:
        publisher_id = ask_int(
            "Введите ID издательства для удаления"
        )

        try:
            publisher = self.publisher_service.find_by_id(
                publisher_id
            )
        except PublisherNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        console.print(
            create_table(
                columns=["ID", "Название"],
                rows=[[
                    str(publisher.id),
                    publisher.name,
                ]],
                title="Издательство для удаления",
            )
        )

        if not ask_confirmation(
            "Вы уверены, что хотите удалить это издательство?"
        ):
            show_warning("Удаление отменено.")
            wait_for_enter()
            return

        try:
            self.publisher_service.delete(publisher_id)
        except PublisherNotFound as e:
            show_error(str(e))
            wait_for_enter()
            return

        show_success("Издательство успешно удалено.")
        wait_for_enter()

    def _print_publishers(
        self,
        publishers: list[Publisher],
    ) -> None:
        rows = [
            [
                str(publisher.id),
                publisher.name,
            ]
            for publisher in publishers
        ]

        table = create_table(
            columns=["ID", "Название"],
            rows=rows,
            title="Список издательств",
        )

        console.print(table)

    def _sort_publishers(
        self,
        publishers: list[Publisher],
    ) -> tuple[list[Publisher], str | None]:

        show_options(
            title="СОРТИРОВКА",
            options=[
                ("1", "По ID"),
                ("2", "По названию"),
                ("0", "Отмена"),
            ],
        )

        choice = ask_choice(
            "Выберите поле для сортировки",
            choices=["1", "2", "0"],
            show_choices=False,
        )

        sort_fields = {
            "1": lambda publisher: publisher.id,
            "2": lambda publisher: publisher.name.lower(),
        }

        if choice == "0":
            return publishers, None

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

        sorted_publishers = sorted(
            publishers,
            key=sort_fields[choice],
            reverse=direction == "2",
        )

        field_name = {
            "1": "ID",
            "2": "названию",
        }

        direction_name = {
            "1": "по возрастанию",
            "2": "по убыванию",
        }

        sort_info = (
            f'Сортировка по "{field_name[choice]}" | '
            f"Направление: {direction_name[direction]}"
        )

        return sorted_publishers, sort_info
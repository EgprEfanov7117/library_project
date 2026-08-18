from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.align import Align
from rich.prompt import IntPrompt
from rich.prompt import FloatPrompt
from rich.box import ROUNDED
from datetime import date


console = Console()


PRIMARY_COLOR = "#8B4513"
SUCCESS_COLOR = "green"
WARNING_COLOR = "yellow"
ERROR_COLOR = "red"

def show_screen(
    title: str,
    options: list[tuple[str, str]],
    subtitle: str | None = None,
) -> None:
    table = create_menu_table(options)

    elements = []

    if subtitle:
        elements.append(
            Align.center(f"[dim]{subtitle}[/dim]\n") 
        )

    elements.append(table)

    panel = Panel(
        Group(*elements),
        title=f"[bold {PRIMARY_COLOR}]{title}[/bold {PRIMARY_COLOR}]",
        border_style=PRIMARY_COLOR,
        box=ROUNDED,
        padding=(1, 2),
        width=70,
    )

    console.print(panel)

def show_success(message: str) -> None:
    console.print(
        f"[bold {SUCCESS_COLOR}]✓[/bold {SUCCESS_COLOR}] {message}"
    )


def show_error(message: str) -> None:
    console.print(
        f"[bold {ERROR_COLOR}]✗[/bold {ERROR_COLOR}] {message}"
    )

def show_warning(message: str) -> None:
    console.print(
        f"[bold {WARNING_COLOR}]![/bold {WARNING_COLOR}] {message}"
    )

def show_options(
    title: str,
    options: list[tuple[str, str]],
) -> None:
    table = create_menu_table(options)

    panel = Panel(
        table,
        title=f"[bold {PRIMARY_COLOR}]{title}[/bold {PRIMARY_COLOR}]",
        border_style=PRIMARY_COLOR,
        box=ROUNDED,
        padding=(1, 2),
        width=70,
    )

    console.print(panel)

def show_info(message: str) -> None:
    console.print(
        Panel(
            message,
            border_style=PRIMARY_COLOR,
            box=ROUNDED,
            padding=(0, 1),
            width=70,
        )
    )

def ask_choice(
    message: str = "Выберите действие",
    choices: list[str] | None = None,
    show_choices: bool = True,
) -> str:
    return Prompt.ask(
        f"[bold {PRIMARY_COLOR}]›[/bold {PRIMARY_COLOR}] {message}",
        choices=choices,
        show_choices=show_choices,
    )

def ask_int(message: str) -> int:
    return IntPrompt.ask(
        f"[bold {PRIMARY_COLOR}]›[/bold {PRIMARY_COLOR}] {message}"
    )

def ask_confirmation(message: str) -> bool:
    return Confirm.ask(
        f"[bold {WARNING_COLOR}]›[/bold {WARNING_COLOR}] {message}"
    )

def ask_text(message: str) -> str:
    return Prompt.ask(
        f"[bold {PRIMARY_COLOR}]›[/bold {PRIMARY_COLOR}] {message}"
    ).strip()

def ask_float(message: str) -> float:
    return FloatPrompt.ask(
        f"[bold {PRIMARY_COLOR}]›[/bold {PRIMARY_COLOR}] {message}"
    )

def ask_date(message: str) -> date:
    while True:
        value = Prompt.ask(
            f"[bold {PRIMARY_COLOR}]›[/bold {PRIMARY_COLOR}] {message}"
        )

        try:
            return date.fromisoformat(value)
        except ValueError:
            show_error(
                "Дата должна быть в формате ГГГГ-ММ-ДД."
            )

def wait_for_enter() -> None:
    Prompt.ask(
        "[dim]Нажмите Enter, чтобы продолжить[/dim]",
        default="",
        show_default=False,
    )

def create_menu_table(
    options: list[tuple[str, str]],
) -> Table:
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        expand=True,
    )

    table.add_column(
        width=5,
        justify="center",
        style=f"bold {PRIMARY_COLOR}",
    )

    table.add_column(
        width=25,
        style="white",
    )

    for number, description in options:
        table.add_row(
            number,
            description,
        )

    return table

def create_table(
    columns: list[str],
    rows: list[list[str]],
    title: str | None = None,
) -> Table:
    table = Table(
        title=title,
        box=ROUNDED,
        header_style=f"bold {PRIMARY_COLOR}",
        show_lines=False,
    )

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row)

    return table


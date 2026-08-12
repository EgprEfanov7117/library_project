from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from repositories.publisher_repository import PublisherRepository

from services.author_service import AuthorService
from services.book_service import BookService
from services.publisher_service import PublisherService

from validators.author_validator import AuthorValidator
from validators.book_validator import BookValidator

from ui.main_menu import MainMenu
from ui.author_menu import AuthorMenu
from ui.book_menu import BookMenu
from ui.publisher_menu import PublisherMenu

def main():
    # =========================
    # Repositories
    # =========================

    author_repository = AuthorRepository()
    book_repository = BookRepository()
    publisher_repository = PublisherRepository()

    # =========================
    # Validators
    # =========================

    author_validator = AuthorValidator()
    book_validator = BookValidator()

    # =========================
    # Services
    # =========================

    author_service = AuthorService(
        repository=author_repository,
        validator=author_validator
    )
    book_service = BookService(
        repository=book_repository,
        validator=book_validator
    )
    publisher_service = PublisherService(
        repository=publisher_repository,
    )

    # =========================
    # Menus
    # =========================

    author_menu = AuthorMenu(
        author_service=author_service
    )
    book_menu = BookMenu(
        book_service=book_service
    )
    publisher_menu = PublisherMenu(
        publisher_service=publisher_service
    )

    # =========================
    # Main menu
    # =========================

    main_menu = MainMenu(
        book_menu=book_menu,
        author_menu=author_menu,
        publisher_menu=publisher_menu
    )

    main_menu.show()

if __name__ == "__main__":
    main()
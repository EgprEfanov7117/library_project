from database import get_connection
from repositories.book_repository import BookRepository
from repositories.author_repository import AuthorRepository
from services.book_service import BookService
from models.book import Book

from datetime import date, datetime

def main():
    
    d1 = date.today()
    d2 = date.fromisoformat("2027-01-01")

    if d1 < d2:
        print("123")

if __name__ == "__main__":
    main()
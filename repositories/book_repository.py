from database import get_connection
from models.book import Book

class BookRepository:

    def _map_to_book(self, row: tuple) -> Book:
        return Book(
                id=row[0],
                title=row[1],
                isbn=row[2],
                pages=row[3],
                price=row[4],
                published_at=row[5],
                is_available=row[6],
                author_id=row[7],
                publisher_id=row[8]
        )

    def get_all(self) -> list[Book]:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                    SELECT
                        id,
                        title,
                        isbn,
                        pages,
                        price,
                        published_at,
                        is_available,
                        author_id,
                        publisher_id
                    FROM books_join;
                """)

                rows = cursor.fetchall()

        return [self._map_to_book(row) for row in rows]

    def find_by_id(self, book_id: int) -> Book | None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                    SELECT
                        id,
                        title,
                        isbn,
                        pages,
                        price,
                        published_at,
                        is_available,
                        author_id,
                        publisher_id
                    FROM books_join
                    WHERE id = %s;
                """, (book_id,))

                row = cursor.fetchone()
        
        if row is None:
            return None
        return self._map_to_book(row)

    def add(self, book: Book) -> None:
        
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO books_join (
                               title, 
                               isbn, 
                               pages, 
                               price, 
                               published_at, 
                               is_available, 
                               author_id, 
                               publisher_id
                               )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (book.title, 
                      book.isbn, 
                      book.pages, 
                      book.price, 
                      book.published_at, 
                      book.is_available, 
                      book.author_id, 
                      book.publisher_id,))

    def update(self, book: Book) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                cursor.execute("""
                            UPDATE books_join
                            SET
                                title = %s,
                                isbn = %s,
                                pages = %s,
                                price = %s,
                                published_at = %s,
                                is_available = %s,
                                author_id = %s,
                                publisher_id = %s
                            WHERE id = %s;
                            """, (book.title, 
                                  book.isbn, 
                                  book.pages, 
                                  book.price, 
                                  book.published_at, 
                                  book.is_available, 
                                  book.author_id, 
                                  book.publisher_id,
                                  book.id))

    def delete(self, book_id: int) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            DELETE FROM books_join
                            WHERE id = %s;
                            """, (book_id,))
        
from database import get_connection
from models.author import Author
from repositories.interfaces.author_repository import AuthorRepositoryInterface

class AuthorRepository(AuthorRepositoryInterface):

    def _map_to_author(self, row: tuple) -> Author:
        return Author(
            id=row[0],
            name=row[1],
            birth_year=row[2],
            country=row[3]
        )

    def get_all(self) -> list[Author]:
        
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            SELECT 
                               id,
                               name,
                               birth_year,
                               country
                            FROM authors;
                            """)
                
                rows = cursor.fetchall()
        
        return [self._map_to_author(row) for row in rows]

    def find_by_id(self, author_id: int) -> Author | None:
        
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            SELECT
                               id,
                               name,
                               birth_year,
                               country
                            FROM authors
                            WHERE id = %s;
                            """, (author_id,))

                row = cursor.fetchone()
        
        if row is None:
            return None
        return self._map_to_author(row)

    def add(self, author: Author) -> None:
        
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            INSERT INTO authors(
                                            name,
                                            birth_year,
                                            country
                                            )
                            VALUES (%s, %s, %s);
                            """, (author.name, 
                                  author.birth_year, 
                                  author.country,))

    def update(self, author: Author) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                cursor.execute("""
                            UPDATE authors
                            SET 
                                name = %s,
                                birth_year = %s,
                                country = %s
                            WHERE id = %s;
                            """, (
                                author.name,
                                author.birth_year,
                                author.country,
                                author.id,
                            ))
    
    def delete(self, author_id: int) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                cursor.execute("""
                            DELETE FROM authors
                            WHERE id = %s;
                            """, (author_id,))



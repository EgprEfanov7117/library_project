from models.publisher import Publisher
from database import get_connection

#publishers
class PublisherRepository:

    def _map_to_publisher(self, row: tuple) -> Publisher:
        return Publisher(
            id=row[0],
            name=row[1],
        )

    def get_all(self) -> list[Publisher]:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            SELECT 
                               id,
                               name
                            FROM publishers;
                            """)
                
                rows = cursor.fetchall()
        
        return [self._map_to_publisher(row) for row in rows]

    def find_by_id(self, publisher_id: int) -> Publisher | None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            SELECT 
                               id,
                               name
                            FROM publishers
                            WHERE id = %s;
                            """, (publisher_id,))
                
                row = cursor.fetchall()
        if row is None:
            return None
        return self._map_to_publisher(row)

    def add(self, publisher: Publisher) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            INSERT INTO publishers (name)
                            VALUES (%s);
                            """, (publisher.name,))

    def update(self, publisher: Publisher) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                               UPDATE publishers
                               SET name = %s
                               WHERE id = %s;
                               """, (publisher.name, publisher.id))

    def delete(self, publisher_id: int) -> None:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                               DELETE FROM publishers
                               WHERE id = %s;
                               """, (publisher_id))

    
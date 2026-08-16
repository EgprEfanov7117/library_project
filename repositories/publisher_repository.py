from models.publisher import Publisher
from database import get_connection
from repositories.interfaces.publisher_repository import PublisherRepositoryInterface

#publishers
class PublisherRepository(PublisherRepositoryInterface):

    def __init__(self, connection_factory=get_connection):
        self.connection_factory = connection_factory


    def _map_to_publisher(self, row: tuple) -> Publisher:
        return Publisher(
            id=row[0],
            name=row[1],
        )

    def get_all(self) -> list[Publisher]:
        with self.connection_factory() as conn:
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
        with self.connection_factory() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            SELECT 
                               id,
                               name
                            FROM publishers
                            WHERE id = %s;
                            """, (publisher_id,))
                
                row = cursor.fetchone()
        if row is None:
            return None
        return self._map_to_publisher(row)

    def add(self, publisher: Publisher) -> None:
        with self.connection_factory() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                            INSERT INTO publishers (name)
                            VALUES (%s);
                            """, (publisher.name,))

    def update(self, publisher: Publisher) -> None:
        with self.connection_factory() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                               UPDATE publishers
                               SET name = %s
                               WHERE id = %s;
                               """, (publisher.name, publisher.id))

    def delete(self, publisher_id: int) -> None:
        with self.connection_factory() as conn:
            with conn.cursor() as cursor:

                cursor.execute("""
                               DELETE FROM publishers
                               WHERE id = %s;
                               """, (publisher_id,))

    
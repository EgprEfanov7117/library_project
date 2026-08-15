def test_database_connection(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT 1")

        result = cursor.fetchone()

    assert result == (1,)
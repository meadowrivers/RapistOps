from rapistops.database import get_connection


def test_database_connection():
    connection = get_connection()

    try:
        assert connection is not None
    finally:
        connection.close()

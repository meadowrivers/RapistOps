from rapistops.database import get_connection
from rapistops.person import Person
from rapistops.person_storage import save_person


def test_save_person():
    person = Person(
        id=1,
        name="Test Person",
        identifiers="test-identifier",
        description="Test Person Description",
        created_at="2026-09-30",
        updated_at="2026-09-30",
    )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM person WHERE id = %s",
                (person.id,),
            )

        connection.commit()
    finally:
        connection.close()

    save_person(person)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM person WHERE id = %s",
                (person.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 1
            assert row[1] == "Test Person"
            assert row[2] == "test-identifier"
            assert row[3] == "Test Person Description"

            cursor.execute(
                "DELETE FROM person WHERE id = %s",
                (person.id,),
            )

        connection.commit()
    finally:
        connection.close()

from rapistops.database import get_connection
from rapistops.event import Event
from rapistops.event_storage import save_event


def test_save_event():
    event = Event(
        id=1,
        type="incident",
        title="Test Event",
        occurred_at="2026-09-30",
        location="Test Location",
        description="Test Event Description",
    )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM event WHERE id = %s",
                (event.id,),
            )

        connection.commit()
    finally:
        connection.close()

    save_event(event)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM event WHERE id = %s",
                (event.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 1
            assert row[1] == "incident"
            assert row[2] == "Test Event"
            assert row[3].strftime("%Y-%m-%d") == "2026-09-30"
            assert row[4] == "Test Location"
            assert row[5] == "Test Event Description"

            cursor.execute(
                "DELETE FROM event WHERE id = %s",
                (event.id,),
            )

        connection.commit()
    finally:
        connection.close()

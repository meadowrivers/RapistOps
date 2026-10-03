from rapistops.database import transaction
from rapistops.event import Event


def save_event(event: Event) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO event (
                id,
                type,
                title,
                occurred_at,
                location,
                description
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                event.id,
                event.type,
                event.title,
                event.occurred_at,
                event.location,
                event.description,
            ),
        )

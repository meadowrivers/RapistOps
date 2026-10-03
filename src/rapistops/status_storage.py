from rapistops.database import transaction
from rapistops.status import Status


def save_status(status: Status) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO status (
                id,
                type,
                entity_id,
                effective_at,
                source_id,
                record_id,
                description
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                status.id,
                status.type,
                status.entity_id,
                status.effective_at,
                status.source_id,
                status.record_id,
                status.description,
            ),
        )

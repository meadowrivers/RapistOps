from rapistops.database import transaction
from rapistops.record import Record


def save_record(record: Record) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO record (
                id,
                source_id,
                provenance_id,
                type,
                title,
                source_reference,
                created_at,
                published_at,
                collected_at
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                record.id,
                record.source_id,
                record.provenance_id,
                record.type,
                record.title,
                record.source_reference,
                record.created_at,
                record.published_at,
                record.collected_at,
            ),
        )

from rapistops.database import transaction
from rapistops.source import Source


def save_source(source: Source) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO source (
                id,
                name,
                type,
                organization,
                location,
                access_reference
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                source.id,
                source.name,
                source.type,
                source.organization,
                source.location,
                source.access_reference,
            ),
        )

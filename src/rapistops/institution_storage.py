from rapistops.database import transaction
from rapistops.institution import Institution


def save_institution(institution: Institution) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO institution (
                id,
                name,
                type,
                jurisdiction,
                location,
                description,
                created_at,
                updated_at
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                institution.id,
                institution.name,
                institution.type,
                institution.jurisdiction,
                institution.location,
                institution.description,
                institution.created_at,
                institution.updated_at,
            ),
        )

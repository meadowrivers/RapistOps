from rapistops.database import transaction
from rapistops.person import Person


def save_person(person: Person) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO person (
                id,
                name,
                identifiers,
                description,
                created_at,
                updated_at
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                person.id,
                person.name,
                person.identifiers,
                person.description,
                person.created_at,
                person.updated_at,
            ),
        )

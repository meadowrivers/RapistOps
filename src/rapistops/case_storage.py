from rapistops.case import Case
from rapistops.database import transaction


def save_case(case: Case) -> None:
    with transaction() as cursor:
        cursor.execute(
            """
            INSERT INTO cases (
                id,
                type,
                name,
                identifier,
                description,
                opened_at,
                closed_at
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                case.id,
                case.type,
                case.name,
                case.identifier,
                case.description,
                case.opened_at,
                case.closed_at,
            ),
        )

from rapistops.case import Case
from rapistops.case_storage import save_case
from rapistops.database import get_connection


def test_save_case():
    case = Case(
        id=1,
        type="criminal",
        name="Test Case",
        identifier="TEST-001",
        description="Test Case Description",
        opened_at="2026-09-30",
        closed_at="2026-09-30",
    )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM cases WHERE id = %s",
                (case.id,),
            )

        connection.commit()
    finally:
        connection.close()

    save_case(case)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM cases WHERE id = %s",
                (case.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 1
            assert row[1] == "criminal"
            assert row[2] == "Test Case"
            assert row[3] == "TEST-001"
            assert row[4] == "Test Case Description"
            assert row[5].strftime("%Y-%m-%d") == "2026-09-30"
            assert row[6].strftime("%Y-%m-%d") == "2026-09-30"

            cursor.execute(
                "DELETE FROM cases WHERE id = %s",
                (case.id,),
            )

        connection.commit()
    finally:
        connection.close()

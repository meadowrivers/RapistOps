from rapistops.database import get_connection
from rapistops.institution import Institution
from rapistops.institution_storage import save_institution


def test_save_institution():
    institution = Institution(
        id=1,
        name="Test Institution",
        type="government",
        jurisdiction="Test Jurisdiction",
        location="Test Location",
        description="Test Institution Description",
        created_at="2026-09-30",
        updated_at="2026-09-30",
    )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM institution WHERE id = %s",
                (institution.id,),
            )

        connection.commit()
    finally:
        connection.close()

    save_institution(institution)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM institution WHERE id = %s",
                (institution.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 1
            assert row[1] == "Test Institution"
            assert row[2] == "government"
            assert row[3] == "Test Jurisdiction"
            assert row[4] == "Test Location"
            assert row[5] == "Test Institution Description"

            cursor.execute(
                "DELETE FROM institution WHERE id = %s",
                (institution.id,),
            )

        connection.commit()
    finally:
        connection.close()

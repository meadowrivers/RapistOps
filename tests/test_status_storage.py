from rapistops.database import get_connection
from rapistops.status import Status
from rapistops.status_storage import save_status


def test_save_status():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM status WHERE id = %s",
                (2,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (4,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (5,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (5,),
            )

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
                    5,
                    "Status Test Source",
                    "public_record",
                    "Test Organization",
                    "Test Location",
                    "status-test-reference",
                ),
            )

            cursor.execute(
                """
                INSERT INTO provenance (
                    id,
                    source_id,
                    collected_at,
                    collection_method,
                    source_reference,
                    collection_context
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    5,
                    5,
                    "2026-09-30",
                    "manual",
                    "status-test-reference",
                    "Status Test Context",
                ),
            )

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
                    4,
                    5,
                    5,
                    "report",
                    "Status Test Record",
                    "status-test-reference",
                    "2026-09-30",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

        connection.commit()
    finally:
        connection.close()

    status = Status(
        id=2,
        type="Reported",
        entity_id=1,
        effective_at="2026-09-30",
        source_id=5,
        record_id=4,
        description="Test Status",
    )

    save_status(status)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM status WHERE id = %s",
                (status.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 2
            assert row[1] == "Reported"
            assert row[2] == 1
            assert row[3].strftime("%Y-%m-%d") == "2026-09-30"
            assert row[4] == 5
            assert row[5] == 4
            assert row[6] == "Test Status"

            cursor.execute(
                "DELETE FROM status WHERE id = %s",
                (status.id,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (4,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (5,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (5,),
            )

        connection.commit()
    finally:
        connection.close()

from rapistops.database import get_connection
from rapistops.provenance import Provenance
from rapistops.provenance_storage import save_provenance


def test_save_provenance():
    provenance = Provenance(
        id=2,
        source_id=2,
        collected_at="2026-09-30",
        collection_method="manual",
        source_reference="provenance-test-reference",
        collection_context="Provenance Test Context",
    )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (provenance.id,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (provenance.source_id,),
            )
            cursor.execute(
                """
                INSERT INTO source (id, name, type)
                VALUES (%s, %s, %s)
                """,
                (provenance.source_id, "Provenance Test Source", "public_record"),
            )

        connection.commit()
    finally:
        connection.close()

    save_provenance(provenance)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM provenance WHERE id = %s",
                (provenance.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 2
            assert row[1] == 2
            assert row[2].strftime("%Y-%m-%d") == "2026-09-30"
            assert row[3] == "manual"
            assert row[4] == "provenance-test-reference"
            assert row[5] == "Provenance Test Context"

            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (provenance.id,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (provenance.source_id,),
            )

        connection.commit()
    finally:
        connection.close()

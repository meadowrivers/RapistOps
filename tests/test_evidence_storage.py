from rapistops.database import get_connection
from rapistops.evidence import Evidence
from rapistops.evidence_storage import save_evidence


def test_save_evidence():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM evidence WHERE id = %s",
                (2,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (2,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (3,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (3,),
            )

            cursor.execute(
                """
                INSERT INTO source (
                    id, name, type, organization, location, access_reference
                )
                VALUES (3, 'Evidence Test Source', 'public_record',
                        'Test Organization', 'Test Location',
                        'evidence-test-reference')
                """
            )

            cursor.execute(
                """
                INSERT INTO provenance (
                    id, source_id, collected_at, collection_method,
                    source_reference, collection_context
                )
                VALUES (3, 3, '2026-09-30', 'manual',
                        'evidence-test-reference',
                        'Evidence Test Context')
                """
            )

            cursor.execute(
                """
                INSERT INTO record (
                    id, source_id, provenance_id, type, title,
                    source_reference, created_at, published_at, collected_at
                )
                VALUES (2, 3, 3, 'report', 'Evidence Test Record',
                        'evidence-test-reference',
                        '2026-09-30', '2026-09-30', '2026-09-30')
                """
            )

        connection.commit()
    finally:
        connection.close()

    evidence = Evidence(
        id=2,
        type="document",
        source_id=3,
        provenance_id=3,
        record_id=2,
        reference="evidence-test-reference",
        description="Test Evidence",
    )

    save_evidence(evidence)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM evidence WHERE id = %s",
                (evidence.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 2
            assert row[1] == "document"
            assert row[2] == 3
            assert row[3] == 3
            assert row[4] == 2
            assert row[5] == "evidence-test-reference"
            assert row[6] == "Test Evidence"

            cursor.execute(
                "DELETE FROM evidence WHERE id = %s",
                (evidence.id,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (2,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (3,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (3,),
            )

        connection.commit()
    finally:
        connection.close()

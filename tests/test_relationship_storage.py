from rapistops.database import get_connection
from rapistops.relationship import Relationship
from rapistops.relationship_storage import save_relationship


def test_save_relationship():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM relationship WHERE id = %s",
                (2,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (3,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (4,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (4,),
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
                    4,
                    "Relationship Test Source",
                    "public_record",
                    "Test Organization",
                    "Test Location",
                    "relationship-test-reference",
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
                    4,
                    4,
                    "2026-09-30",
                    "manual",
                    "relationship-test-reference",
                    "Relationship Test Context",
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
                    3,
                    4,
                    4,
                    "report",
                    "Relationship Test Record",
                    "relationship-test-reference",
                    "2026-09-30",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

        connection.commit()
    finally:
        connection.close()

    relationship = Relationship(
        id=2,
        source_entity_id=1,
        target_entity_id=2,
        type="associated_with",
        source_id=4,
        record_id=3,
        effective_at="2026-09-30",
        description="Test Relationship",
    )

    save_relationship(relationship)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM relationship WHERE id = %s",
                (relationship.id,),
            )

            row = cursor.fetchone()

            assert row is not None
            assert row[0] == 2
            assert row[1] == 1
            assert row[2] == 2
            assert row[3] == "associated_with"
            assert row[4] == 4
            assert row[5] == 3
            assert row[6].strftime("%Y-%m-%d") == "2026-09-30"
            assert row[7] == "Test Relationship"

            cursor.execute(
                "DELETE FROM relationship WHERE id = %s",
                (relationship.id,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (3,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (4,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (4,),
            )

        connection.commit()
    finally:
        connection.close()

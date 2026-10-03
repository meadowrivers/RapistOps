from rapistops.database import get_connection


def test_database_integration():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            # Clean up any previous integration-test data.
            cursor.execute("DELETE FROM relationship WHERE id = %s", (100,))
            cursor.execute("DELETE FROM status WHERE id = %s", (100,))
            cursor.execute("DELETE FROM evidence WHERE id = %s", (100,))
            cursor.execute("DELETE FROM cases WHERE id = %s", (100,))
            cursor.execute("DELETE FROM event WHERE id = %s", (100,))
            cursor.execute("DELETE FROM institution WHERE id = %s", (100,))
            cursor.execute("DELETE FROM person WHERE id = %s", (100,))
            cursor.execute("DELETE FROM record WHERE id = %s", (100,))
            cursor.execute("DELETE FROM provenance WHERE id = %s", (100,))
            cursor.execute("DELETE FROM source WHERE id = %s", (100,))

            # Create the source.
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
                    100,
                    "Integration Test Source",
                    "public_record",
                    "Test Organization",
                    "Test Location",
                    "integration-test-reference",
                ),
            )

            # Create provenance connected to the source.
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
                    100,
                    100,
                    "2026-09-30",
                    "manual",
                    "integration-test-reference",
                    "Integration Test Context",
                ),
            )

            # Create a record connected to the source and provenance.
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
                    100,
                    100,
                    100,
                    "report",
                    "Integration Test Record",
                    "integration-test-reference",
                    "2026-09-30",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

            # Create evidence connected to the record.
            cursor.execute(
                """
                INSERT INTO evidence (
                    id,
                    type,
                    source_id,
                    provenance_id,
                    record_id,
                    reference,
                    description
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    100,
                    "document",
                    100,
                    100,
                    100,
                    "integration-evidence-reference",
                    "Integration Test Evidence",
                ),
            )

            # Create a person.
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
                    100,
                    "Integration Test Person",
                    "integration-test-identifier",
                    "Integration Test Person Description",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

            # Create an institution.
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
                    100,
                    "Integration Test Institution",
                    "government",
                    "Test Jurisdiction",
                    "Test Location",
                    "Integration Test Institution Description",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

            # Create an event.
            cursor.execute(
                """
                INSERT INTO event (
                    id,
                    type,
                    title,
                    occurred_at,
                    location,
                    description
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    100,
                    "incident",
                    "Integration Test Event",
                    "2026-09-30",
                    "Test Location",
                    "Integration Test Event Description",
                ),
            )

            # Create a case.
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
                    100,
                    "criminal",
                    "Integration Test Case",
                    "INTEGRATION-001",
                    "Integration Test Case Description",
                    "2026-09-30",
                    "2026-09-30",
                ),
            )

            # Create a status connected to the record.
            cursor.execute(
                """
                INSERT INTO status (
                    id,
                    type,
                    entity_id,
                    effective_at,
                    source_id,
                    record_id,
                    description
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    100,
                    "Reported",
                    100,
                    "2026-09-30",
                    100,
                    100,
                    "Integration Test Status",
                ),
            )

            # Create a relationship connected to the record.
            cursor.execute(
                """
                INSERT INTO relationship (
                    id,
                    source_entity_id,
                    target_entity_id,
                    type,
                    source_id,
                    record_id,
                    effective_at,
                    description
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    100,
                    100,
                    100,
                    "associated_with",
                    100,
                    100,
                    "2026-09-30",
                    "Integration Test Relationship",
                ),
            )

        connection.commit()

        # Verify the complete set of connected data exists.
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    source.id,
                    provenance.id,
                    record.id,
                    evidence.id,
                    person.id,
                    institution.id,
                    event.id,
                    cases.id,
                    status.id,
                    relationship.id
                FROM source
                JOIN provenance
                    ON provenance.source_id = source.id
                JOIN record
                    ON record.source_id = source.id
                    AND record.provenance_id = provenance.id
                JOIN evidence
                    ON evidence.record_id = record.id
                CROSS JOIN person
                CROSS JOIN institution
                CROSS JOIN event
                CROSS JOIN cases
                JOIN status
                    ON status.record_id = record.id
                JOIN relationship
                    ON relationship.record_id = record.id
                WHERE source.id = 100
                    AND provenance.id = 100
                    AND record.id = 100
                    AND evidence.id = 100
                    AND person.id = 100
                    AND institution.id = 100
                    AND event.id = 100
                    AND cases.id = 100
                    AND status.id = 100
                    AND relationship.id = 100
                """
            )

            row = cursor.fetchone()

            assert row == (
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
            )

            # Clean up in reverse dependency order.
            cursor.execute(
                "DELETE FROM relationship WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM status WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM evidence WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM cases WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM event WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM institution WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM person WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM record WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM provenance WHERE id = %s",
                (100,),
            )
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (100,),
            )

        connection.commit()

    finally:
        connection.close()

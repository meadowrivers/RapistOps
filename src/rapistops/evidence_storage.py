from rapistops.database import transaction
from rapistops.evidence import Evidence


def save_evidence(evidence: Evidence) -> None:
    with transaction() as cursor:
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
                evidence.id,
                evidence.type,
                evidence.source_id,
                evidence.provenance_id,
                evidence.record_id,
                evidence.reference,
                evidence.description,
            ),
        )

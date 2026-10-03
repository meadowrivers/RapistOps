from rapistops.database import transaction
from rapistops.relationship import Relationship


def save_relationship(relationship: Relationship) -> None:
    with transaction() as cursor:
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
                relationship.id,
                relationship.source_entity_id,
                relationship.target_entity_id,
                relationship.type,
                relationship.source_id,
                relationship.record_id,
                relationship.effective_at,
                relationship.description,
            ),
        )

from rapistops.relationship import Relationship


def test_class_relationship():
    relationship = Relationship(
        id=1,
        source_entity_id=1,
        target_entity_id=2,
        type="associated_with",
        source_id=1,
        record_id=1,
        effective_at="2024-06-01",
        description="Test Relationship",
    )

    assert relationship.id == 1
    assert relationship.source_entity_id == 1
    assert relationship.target_entity_id == 2
    assert relationship.type == "associated_with"
    assert relationship.source_id == 1
    assert relationship.record_id == 1
    assert relationship.effective_at == "2024-06-01"
    assert relationship.description == "Test Relationship"

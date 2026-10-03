from rapistops.status import Status


def test_class_status():
    status = Status(
        id=1,
        type="Reported",
        entity_id=1,
        effective_at="2024-06-01",
        source_id=1,
        record_id=1,
        description="Test Status",
    )

    assert status.id == 1
    assert status.type == "Reported"
    assert status.entity_id == 1
    assert status.effective_at == "2024-06-01"
    assert status.source_id == 1
    assert status.record_id == 1
    assert status.description == "Test Status"

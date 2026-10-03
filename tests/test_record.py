from rapistops.record import Record


def test_class_record():
    record = Record(
        id=1,
        source_id=1,
        provenance_id=1,
        type="Test Record",
        title="Test Title",
        source_reference="Test Reference",
        created_at="2024-06-01",
        published_at="2024-06-02",
        collected_at="2024-06-03",
    )

    assert record.id == 1
    assert record.source_id == 1
    assert record.provenance_id == 1
    assert record.type == "Test Record"
    assert record.title == "Test Title"
    assert record.source_reference == "Test Reference"
    assert record.created_at == "2024-06-01"
    assert record.published_at == "2024-06-02"
    assert record.collected_at == "2024-06-03"

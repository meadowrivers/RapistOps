from rapistops.evidence import Evidence


def test_class_evidence():
    evidence = Evidence(
        id=1,
        type="Test Evidence",
        source_id=1,
        provenance_id=1,
        record_id=1,
        reference="Test Reference",
        description="Test Description",
    )

    assert evidence.id == 1
    assert evidence.type == "Test Evidence"
    assert evidence.source_id == 1
    assert evidence.provenance_id == 1
    assert evidence.record_id == 1
    assert evidence.reference == "Test Reference"
    assert evidence.description == "Test Description"

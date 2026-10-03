from rapistops.provenance import Provenance


def test_class_provenance():
    provenance = Provenance(
        id=1,
        source_id=1,
        collected_at="2026-09-30",
        collection_method="manual",
        source_reference="test-reference",
        collection_context="Test Context",
    )

    assert provenance.source_id == 1
    assert provenance.collected_at == "2026-09-30"
    assert provenance.collection_method == "manual"
    assert provenance.source_reference == "test-reference"
    assert provenance.collection_context == "Test Context"

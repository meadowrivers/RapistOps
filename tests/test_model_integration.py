from rapistops.case import Case
from rapistops.event import Event
from rapistops.evidence import Evidence
from rapistops.institution import Institution
from rapistops.person import Person
from rapistops.provenance import Provenance
from rapistops.record import Record
from rapistops.relationship import Relationship
from rapistops.source import Source
from rapistops.status import Status


def test_core_model_integration():
    source = Source(
        id=1,
        name="Test Source",
        type="public_record",
        organization="Test Organization",
        location="Test Location",
        access_reference="source-1",
    )

    provenance = Provenance(
        id=1,
        source_id=source.id,
        collected_at="2024-06-01",
        collection_method="Test Method",
        source_reference="record-1",
        collection_context="Test Context",
    )

    record = Record(
        id=1,
        source_id=source.id,
        provenance_id=1,
        type="Test Record",
        title="Test Record",
        source_reference="record-1",
        created_at="2024-05-01",
        published_at="2024-05-02",
        collected_at="2024-06-01",
    )

    evidence = Evidence(
        id=1,
        type="Test Evidence",
        source_id=source.id,
        provenance_id=1,
        record_id=record.id,
        reference="evidence-1",
        description="Test Evidence",
    )

    person = Person(
        id=1,
        name="Test Person",
        identifiers="person-1",
        description="Test Person",
        created_at="2024-06-01",
        updated_at="2024-06-01",
    )

    institution = Institution(
        id=1,
        name="Test Institution",
        type="agency",
        jurisdiction="Test Jurisdiction",
        location="Test Location",
        description="Test Institution",
        created_at="2024-06-01",
        updated_at="2024-06-01",
    )

    event = Event(
        id=1,
        type="incident",
        title="Test Event",
        occurred_at="2024-05-01",
        location="Test Location",
        description="Test Event",
    )

    case = Case(
        id=1,
        type="investigation",
        name="Test Case",
        identifier="CASE-001",
        description="Test Case",
        opened_at="2024-05-01",
        closed_at="2024-06-01",
    )

    status = Status(
        id=1,
        type="Reported",
        entity_id=case.id,
        effective_at="2024-05-01",
        source_id=source.id,
        record_id=record.id,
        description="Test Status",
    )

    relationship = Relationship(
        id=1,
        source_entity_id=person.id,
        target_entity_id=case.id,
        type="associated_with",
        source_id=source.id,
        record_id=record.id,
        effective_at="2024-05-01",
        description="Test Relationship",
    )

    assert provenance.source_id == source.id
    assert record.source_id == source.id
    assert record.provenance_id == 1
    assert evidence.source_id == source.id
    assert evidence.provenance_id == provenance.source_id
    assert evidence.record_id == record.id
    assert status.entity_id == case.id
    assert status.source_id == source.id
    assert status.record_id == record.id
    assert relationship.source_entity_id == person.id
    assert relationship.target_entity_id == case.id
    assert relationship.source_id == source.id
    assert relationship.record_id == record.id
    assert institution.type == "agency"
    assert event.type == "incident"

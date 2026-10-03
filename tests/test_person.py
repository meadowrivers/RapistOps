from rapistops.person import Person


def test_class_person():
    person = Person(
        id=1,
        name="Test Person",
        identifiers="Test Identifier",
        description="Test Description",
        created_at="2024-06-01",
        updated_at="2024-06-02",
    )

    assert person.id == 1
    assert person.name == "Test Person"
    assert person.identifiers == "Test Identifier"
    assert person.description == "Test Description"
    assert person.created_at == "2024-06-01"
    assert person.updated_at == "2024-06-02"

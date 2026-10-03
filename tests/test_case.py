from rapistops.case import Case


def test_class_case():
    case = Case(
        id=1,
        type="Test Case",
        name="Test Case Name",
        identifier="TEST-001",
        description="Test Description",
        opened_at="2024-06-01",
        closed_at="2024-06-02",
    )

    assert case.id == 1
    assert case.type == "Test Case"
    assert case.name == "Test Case Name"
    assert case.identifier == "TEST-001"
    assert case.description == "Test Description"
    assert case.opened_at == "2024-06-01"
    assert case.closed_at == "2024-06-02"

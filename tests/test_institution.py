from rapistops.institution import Institution


def test_class_institution():
    institution = Institution(
        id=1,
        name="Test Institution",
        type="Test Type",
        jurisdiction="Test Jurisdiction",
        location="Test Location",
        description="Test Description",
        created_at="2024-06-01",
        updated_at="2024-06-02",
    )

    assert institution.id == 1
    assert institution.name == "Test Institution"
    assert institution.type == "Test Type"
    assert institution.jurisdiction == "Test Jurisdiction"
    assert institution.location == "Test Location"
    assert institution.description == "Test Description"
    assert institution.created_at == "2024-06-01"
    assert institution.updated_at == "2024-06-02"

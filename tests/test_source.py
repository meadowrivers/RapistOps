from rapistops.source import Source


def test_class_source():
    source = Source(
        id=1,
        name="Test Source",
        type="Test Type",
        organization="Test Organization",
        location="Test Location",
        access_reference="Test Reference",
    )

    assert source.id == 1
    assert source.name == "Test Source"
    assert source.type == "Test Type"
    assert source.organization == "Test Organization"
    assert source.location == "Test Location"
    assert source.access_reference == "Test Reference"

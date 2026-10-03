from rapistops.source import Source
from rapistops.source_storage import save_source


def test_save_source():
    source = Source(
        id=1,
        name="Test Source",
        type="public_record",
        organization="Test Organization",
        location="Test Location",
        access_reference="test-reference",
    )

    save_source(source)

from rapistops.event import Event


def test_class_event():
    event = Event(
        id=1,
        type="Test Event",
        title="Test Event Title",
        occurred_at="2024-06-01",
        location="Test Location",
        description="Test Description",
    )

    assert event.id == 1
    assert event.type == "Test Event"
    assert event.title == "Test Event Title"
    assert event.occurred_at == "2024-06-01"
    assert event.location == "Test Location"
    assert event.description == "Test Description"

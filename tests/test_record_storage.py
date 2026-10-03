from rapistops.database import get_connection
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

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (source.id,),
            )

        connection.commit()
    finally:
        connection.close()

    save_source(source)

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM source WHERE id = %s",
                (source.id,),
            )

        connection.commit()
    finally:
        connection.close()

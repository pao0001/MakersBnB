from lib.property_repository import PropertyRepository
from lib.property import Property

"""
Call all from property repo we get all property objects
"""

def test_get_all_property_objects(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    properties = repository.all()

    assert properties == [
        Property(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
        Property(2, 'Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, 'available', 2),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3)
    ]

"""
When we call PropertyRepository find we get a single property
"""
def test_get_single_property(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    book = repository.find(3)
    assert book == Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3)

"""
When we call PropertyRepository create, we create a single property
"""
def test_create_property(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    create_property = repository.create(Property(4, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 4))

    assert create_property == Property(4, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 4)

    result = repository.all()
    assert result == [
        Property(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
        Property(2, 'Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, 'available', 2),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3),
        Property(4, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 4)
    ]

"""
When we call PropertyRepository delete, the id of property will be removed from list
"""

def test_delete_property(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)
    repository.delete(2)

    result = repository.all()

    assert result == [
        Property(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3)
    ]

"""
When update it called by PropertyRepository, all details from the row can be updated based of its id
"""

def test_update(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    updated_property = repository.update(Property(2, 'Alice Jones', 'alicejones@example.com', '0987743217', '50 River Road, Lakeside', 'Peaceful lake house with forest views.', 200.00, 'available', 2))
    assert updated_property == Property(2, 'Alice Jones', 'alicejones@example.com', '0987743217', '50 River Road, Lakeside', 'Peaceful lake house with forest views.', 200.00, 'available', 2)

    result = repository.all()
    assert result == [
        Property(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3),
        Property(2, 'Alice Jones', 'alicejones@example.com', '0987743217', '50 River Road, Lakeside', 'Peaceful lake house with forest views.', 200.00, 'available', 2)
    ]
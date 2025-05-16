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
        Property(1, 'John Doe', 'johndoe@bing.com', '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, '2025-05-15,2025-05-20', 1),
        Property(2, 'Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, '2025-06-01 - 2025-06-10', 2),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, '2025-07-05 - 2025-07-12', 3),
        Property(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', '101 Oak Street, Midtown', 'Modern apartment close to downtown.', 120.00, '2025-08-15 - 2025-08-22', 4),
        Property(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', '202 Pine Lane, Suburbia', 'Cozy suburban home with backyard.', 90.00, '2025-09-10 - 2025-09-17', 5),
        Property(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', '303 Birch Blvd, Riverside', 'Riverside cabin with great views.', 130.00, '2025-10-01 - 2025-10-07', 6),
        Property(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', '404 Cedar Court, Hillside', 'Spacious villa on a hill.', 200.00, '2025-11-01 - 2025-11-10', 7),
        Property(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', '505 Elm Street, Downtown', 'Stylish loft in city center.', 140.00, '2025-12-01 - 2025-12-08', 8),
        Property(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', '606 Spruce Drive, Seaside', 'Beachfront property with ocean views.', 220.00, '2025-05-25 - 2025-06-01', 9),
        Property(10, 'Karen Young', 'karen.young@mail.com', '07789012345', '707 Maple Avenue, Oldtown', 'Historic home with modern amenities.', 110.00, '2025-06-15 - 2025-06-20', 10),
        Property(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', '808 Walnut Street, Uptown', 'Elegant townhouse near park.', 125.00, '2025-07-10 - 2025-07-17', 11),
        Property(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', '909 Chestnut Blvd, Midtown', 'Contemporary apartment with gym access.', 135.00, '2025-08-01 - 2025-08-07', 12),
        Property(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', '1001 Aspen Way, Countryside', 'Quiet retreat surrounded by nature.', 95.00, '2025-09-01 - 2025-09-10', 13),
        Property(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', '1102 Willow Road, Lakeside', 'Cozy cottage near the lake.', 105.00, '2025-10-10 - 2025-10-15', 14),
        Property(15, 'Paul Green', 'paul.green@domain.com', '07234567801', '1203 Poplar Street, Suburbia', 'Family home with large garden.', 115.00, '2025-11-05 - 2025-11-12', 15),
        Property(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', '1304 Fir Lane, Hillside', 'Charming bungalow with views.', 125.00, '2025-12-10 - 2025-12-17', 16),
        Property(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', '1405 Pine Street, Downtown', 'Modern condo with balcony.', 130.00, '2026-01-01 - 2026-01-08', 17),
        Property(18, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18),
        Property(19, 'Tina King', 'tina.king@domain.com', '07678012345', '1607 Birch Avenue, Oldtown', 'Classic home with fireplace.', 115.00, '2026-03-01 - 2026-03-08', 19),
        Property(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', '1708 Oak Court, Riverside', 'Cozy riverside cabin.', 125.00, '2026-04-01 - 2026-04-07', 20),

    ]

"""
When we call PropertyRepository find we get a single property
"""
def test_get_single_property(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    book = repository.find(3)
    assert book == Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, '2025-07-05 - 2025-07-12', 3)

"""
When we call PropertyRepository create, we create a single property
"""
def test_create_property(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = PropertyRepository(db_connection)

    create_property = repository.create(Property(21, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18))

    assert create_property == Property(21, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18)

    result = repository.all()
    assert result == [
        Property(1, 'John Doe', 'johndoe@bing.com', '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, '2025-05-15,2025-05-20', 1),
        Property(2, 'Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, '2025-06-01 - 2025-06-10', 2),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, '2025-07-05 - 2025-07-12', 3),
        Property(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', '101 Oak Street, Midtown', 'Modern apartment close to downtown.', 120.00, '2025-08-15 - 2025-08-22', 4),
        Property(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', '202 Pine Lane, Suburbia', 'Cozy suburban home with backyard.', 90.00, '2025-09-10 - 2025-09-17', 5),
        Property(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', '303 Birch Blvd, Riverside', 'Riverside cabin with great views.', 130.00, '2025-10-01 - 2025-10-07', 6),
        Property(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', '404 Cedar Court, Hillside', 'Spacious villa on a hill.', 200.00, '2025-11-01 - 2025-11-10', 7),
        Property(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', '505 Elm Street, Downtown', 'Stylish loft in city center.', 140.00, '2025-12-01 - 2025-12-08', 8),
        Property(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', '606 Spruce Drive, Seaside', 'Beachfront property with ocean views.', 220.00, '2025-05-25 - 2025-06-01', 9),
        Property(10, 'Karen Young', 'karen.young@mail.com', '07789012345', '707 Maple Avenue, Oldtown', 'Historic home with modern amenities.', 110.00, '2025-06-15 - 2025-06-20', 10),
        Property(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', '808 Walnut Street, Uptown', 'Elegant townhouse near park.', 125.00, '2025-07-10 - 2025-07-17', 11),
        Property(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', '909 Chestnut Blvd, Midtown', 'Contemporary apartment with gym access.', 135.00, '2025-08-01 - 2025-08-07', 12),
        Property(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', '1001 Aspen Way, Countryside', 'Quiet retreat surrounded by nature.', 95.00, '2025-09-01 - 2025-09-10', 13),
        Property(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', '1102 Willow Road, Lakeside', 'Cozy cottage near the lake.', 105.00, '2025-10-10 - 2025-10-15', 14),
        Property(15, 'Paul Green', 'paul.green@domain.com', '07234567801', '1203 Poplar Street, Suburbia', 'Family home with large garden.', 115.00, '2025-11-05 - 2025-11-12', 15),
        Property(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', '1304 Fir Lane, Hillside', 'Charming bungalow with views.', 125.00, '2025-12-10 - 2025-12-17', 16),
        Property(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', '1405 Pine Street, Downtown', 'Modern condo with balcony.', 130.00, '2026-01-01 - 2026-01-08', 17),
        Property(18, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18),
        Property(19, 'Tina King', 'tina.king@domain.com', '07678012345', '1607 Birch Avenue, Oldtown', 'Classic home with fireplace.', 115.00, '2026-03-01 - 2026-03-08', 19),
        Property(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', '1708 Oak Court, Riverside', 'Cozy riverside cabin.', 125.00, '2026-04-01 - 2026-04-07', 20),
        Property(21, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18)

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
        Property(1, 'John Doe', 'johndoe@bing.com', '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, '2025-05-15,2025-05-20', 1),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, '2025-07-05 - 2025-07-12', 3),
        Property(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', '101 Oak Street, Midtown', 'Modern apartment close to downtown.', 120.00, '2025-08-15 - 2025-08-22', 4),
        Property(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', '202 Pine Lane, Suburbia', 'Cozy suburban home with backyard.', 90.00, '2025-09-10 - 2025-09-17', 5),
        Property(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', '303 Birch Blvd, Riverside', 'Riverside cabin with great views.', 130.00, '2025-10-01 - 2025-10-07', 6),
        Property(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', '404 Cedar Court, Hillside', 'Spacious villa on a hill.', 200.00, '2025-11-01 - 2025-11-10', 7),
        Property(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', '505 Elm Street, Downtown', 'Stylish loft in city center.', 140.00, '2025-12-01 - 2025-12-08', 8),
        Property(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', '606 Spruce Drive, Seaside', 'Beachfront property with ocean views.', 220.00, '2025-05-25 - 2025-06-01', 9),
        Property(10, 'Karen Young', 'karen.young@mail.com', '07789012345', '707 Maple Avenue, Oldtown', 'Historic home with modern amenities.', 110.00, '2025-06-15 - 2025-06-20', 10),
        Property(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', '808 Walnut Street, Uptown', 'Elegant townhouse near park.', 125.00, '2025-07-10 - 2025-07-17', 11),
        Property(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', '909 Chestnut Blvd, Midtown', 'Contemporary apartment with gym access.', 135.00, '2025-08-01 - 2025-08-07', 12),
        Property(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', '1001 Aspen Way, Countryside', 'Quiet retreat surrounded by nature.', 95.00, '2025-09-01 - 2025-09-10', 13),
        Property(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', '1102 Willow Road, Lakeside', 'Cozy cottage near the lake.', 105.00, '2025-10-10 - 2025-10-15', 14),
        Property(15, 'Paul Green', 'paul.green@domain.com', '07234567801', '1203 Poplar Street, Suburbia', 'Family home with large garden.', 115.00, '2025-11-05 - 2025-11-12', 15),
        Property(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', '1304 Fir Lane, Hillside', 'Charming bungalow with views.', 125.00, '2025-12-10 - 2025-12-17', 16),
        Property(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', '1405 Pine Street, Downtown', 'Modern condo with balcony.', 130.00, '2026-01-01 - 2026-01-08', 17),
        Property(18, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18),
        Property(19, 'Tina King', 'tina.king@domain.com', '07678012345', '1607 Birch Avenue, Oldtown', 'Classic home with fireplace.', 115.00, '2026-03-01 - 2026-03-08', 19),
        Property(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', '1708 Oak Court, Riverside', 'Cozy riverside cabin.', 125.00, '2026-04-01 - 2026-04-07', 20),

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
        Property(1, 'John Doe', 'johndoe@bing.com', '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, '2025-05-15,2025-05-20', 1),
        Property(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, '2025-07-05 - 2025-07-12', 3),
        Property(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', '101 Oak Street, Midtown', 'Modern apartment close to downtown.', 120.00, '2025-08-15 - 2025-08-22', 4),
        Property(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', '202 Pine Lane, Suburbia', 'Cozy suburban home with backyard.', 90.00, '2025-09-10 - 2025-09-17', 5),
        Property(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', '303 Birch Blvd, Riverside', 'Riverside cabin with great views.', 130.00, '2025-10-01 - 2025-10-07', 6),
        Property(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', '404 Cedar Court, Hillside', 'Spacious villa on a hill.', 200.00, '2025-11-01 - 2025-11-10', 7),
        Property(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', '505 Elm Street, Downtown', 'Stylish loft in city center.', 140.00, '2025-12-01 - 2025-12-08', 8),
        Property(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', '606 Spruce Drive, Seaside', 'Beachfront property with ocean views.', 220.00, '2025-05-25 - 2025-06-01', 9),
        Property(10, 'Karen Young', 'karen.young@mail.com', '07789012345', '707 Maple Avenue, Oldtown', 'Historic home with modern amenities.', 110.00, '2025-06-15 - 2025-06-20', 10),
        Property(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', '808 Walnut Street, Uptown', 'Elegant townhouse near park.', 125.00, '2025-07-10 - 2025-07-17', 11),
        Property(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', '909 Chestnut Blvd, Midtown', 'Contemporary apartment with gym access.', 135.00, '2025-08-01 - 2025-08-07', 12),
        Property(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', '1001 Aspen Way, Countryside', 'Quiet retreat surrounded by nature.', 95.00, '2025-09-01 - 2025-09-10', 13),
        Property(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', '1102 Willow Road, Lakeside', 'Cozy cottage near the lake.', 105.00, '2025-10-10 - 2025-10-15', 14),
        Property(15, 'Paul Green', 'paul.green@domain.com', '07234567801', '1203 Poplar Street, Suburbia', 'Family home with large garden.', 115.00, '2025-11-05 - 2025-11-12', 15),
        Property(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', '1304 Fir Lane, Hillside', 'Charming bungalow with views.', 125.00, '2025-12-10 - 2025-12-17', 16),
        Property(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', '1405 Pine Street, Downtown', 'Modern condo with balcony.', 130.00, '2026-01-01 - 2026-01-08', 17),
        Property(18, 'Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, '2026-02-01 - 2026-02-07', 18),
        Property(19, 'Tina King', 'tina.king@domain.com', '07678012345', '1607 Birch Avenue, Oldtown', 'Classic home with fireplace.', 115.00, '2026-03-01 - 2026-03-08', 19),
        Property(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', '1708 Oak Court, Riverside', 'Cozy riverside cabin.', 125.00, '2026-04-01 - 2026-04-07', 20),
        Property(2, 'Alice Jones', 'alicejones@example.com', '0987743217', '50 River Road, Lakeside', 'Peaceful lake house with forest views.', 200.00, 'available', 2)

    ]
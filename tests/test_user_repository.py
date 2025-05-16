from lib.user_repository import UserRepository
from lib.user import User


def test_all(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()

    assert users == [
        User(1, 'John Doe', 'johndoe@bing.com', '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'),
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'),
        User(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', 'password_hash_placeholder'),
        User(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', 'password_hash_placeholder'),
        User(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', 'password_hash_placeholder'),
        User(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', 'password_hash_placeholder'),
        User(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', 'password_hash_placeholder'),
        User(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', 'password_hash_placeholder'),
        User(10, 'Karen Young', 'karen.young@mail.com', '07789012345', 'password_hash_placeholder'),
        User(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', 'password_hash_placeholder'),
        User(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', 'password_hash_placeholder'),
        User(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', 'password_hash_placeholder'),
        User(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', 'password_hash_placeholder'),
        User(15, 'Paul Green', 'paul.green@domain.com', '07234567801', 'password_hash_placeholder'),
        User(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', 'password_hash_placeholder'),
        User(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', 'password_hash_placeholder'),
        User(18, 'Steve Young', 'steve.young@mail.com', '07567801234', 'password_hash_placeholder'),
        User(19, 'Tina King', 'tina.king@domain.com', '07678012345', 'password_hash_placeholder'),
        User(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', 'password_hash_placeholder')
        ]

def test_find(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user == User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu')

def test_create(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    created_user = repository.create(User(21, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4'))
    assert created_user == User(21, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4')

    result = repository.all()
    assert result == [
        User(1, 'John Doe', 'johndoe@bing.com', '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'),
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'),
        User(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', 'password_hash_placeholder'),
        User(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', 'password_hash_placeholder'),
        User(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', 'password_hash_placeholder'),
        User(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', 'password_hash_placeholder'),
        User(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', 'password_hash_placeholder'),
        User(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', 'password_hash_placeholder'),
        User(10, 'Karen Young', 'karen.young@mail.com', '07789012345', 'password_hash_placeholder'),
        User(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', 'password_hash_placeholder'),
        User(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', 'password_hash_placeholder'),
        User(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', 'password_hash_placeholder'),
        User(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', 'password_hash_placeholder'),
        User(15, 'Paul Green', 'paul.green@domain.com', '07234567801', 'password_hash_placeholder'),
        User(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', 'password_hash_placeholder'),
        User(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', 'password_hash_placeholder'),
        User(18, 'Steve Young', 'steve.young@mail.com', '07567801234', 'password_hash_placeholder'),
        User(19, 'Tina King', 'tina.king@domain.com', '07678012345', 'password_hash_placeholder'),
        User(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', 'password_hash_placeholder'),
        User(21, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4')
        ]

def test_delete(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'),
        User(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', 'password_hash_placeholder'),
        User(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', 'password_hash_placeholder'),
        User(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', 'password_hash_placeholder'),
        User(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', 'password_hash_placeholder'),
        User(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', 'password_hash_placeholder'),
        User(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', 'password_hash_placeholder'),
        User(10, 'Karen Young', 'karen.young@mail.com', '07789012345', 'password_hash_placeholder'),
        User(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', 'password_hash_placeholder'),
        User(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', 'password_hash_placeholder'),
        User(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', 'password_hash_placeholder'),
        User(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', 'password_hash_placeholder'),
        User(15, 'Paul Green', 'paul.green@domain.com', '07234567801', 'password_hash_placeholder'),
        User(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', 'password_hash_placeholder'),
        User(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', 'password_hash_placeholder'),
        User(18, 'Steve Young', 'steve.young@mail.com', '07567801234', 'password_hash_placeholder'),
        User(19, 'Tina King', 'tina.king@domain.com', '07678012345', 'password_hash_placeholder'),
        User(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', 'password_hash_placeholder')
        ]


def test_update(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    updated_user = repository.update(User(1, 'Bob Doe', 'bobdoe@bing.com' , '987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'))
    assert updated_user == (User(1, 'Bob Doe', 'bobdoe@bing.com' , '987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'))

    result = repository.all()
    print(result)
    assert result == [
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'),
        User(4, 'Eve Carter', 'eve.carter@mail.com', '07123456789', 'password_hash_placeholder'),
        User(5, 'Frank Lee', 'frank.lee@example.com', '07234567890', 'password_hash_placeholder'),
        User(6, 'Grace Kim', 'grace.kim@mail.com', '07345678901', 'password_hash_placeholder'),
        User(7, 'Henry Adams', 'henry.adams@domain.com', '07456789012', 'password_hash_placeholder'),
        User(8, 'Ivy Clark', 'ivy.clark@mail.com', '07567890123', 'password_hash_placeholder'),
        User(9, 'Jack Wright', 'jack.wright@example.com', '07678901234', 'password_hash_placeholder'),
        User(10, 'Karen Young', 'karen.young@mail.com', '07789012345', 'password_hash_placeholder'),
        User(11, 'Leo Martin', 'leo.martin@domain.com', '07890123456', 'password_hash_placeholder'),
        User(12, 'Mia Turner', 'mia.turner@mail.com', '07901234567', 'password_hash_placeholder'),
        User(13, 'Noah Scott', 'noah.scott@example.com', '07012345678', 'password_hash_placeholder'),
        User(14, 'Olivia Evans', 'olivia.evans@mail.com', '07123456780', 'password_hash_placeholder'),
        User(15, 'Paul Green', 'paul.green@domain.com', '07234567801', 'password_hash_placeholder'),
        User(16, 'Quinn Hall', 'quinn.hall@mail.com', '07345678012', 'password_hash_placeholder'),
        User(17, 'Rachel Baker', 'rachel.baker@example.com', '07456780123', 'password_hash_placeholder'),
        User(18, 'Steve Young', 'steve.young@mail.com', '07567801234', 'password_hash_placeholder'),
        User(19, 'Tina King', 'tina.king@domain.com', '07678012345', 'password_hash_placeholder'),
        User(20, 'Uma Collins', 'uma.collins@mail.com', '07780123456', 'password_hash_placeholder'),
        User(1, 'Bob Doe', 'bobdoe@bing.com' , '987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G')
        ]
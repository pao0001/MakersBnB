from lib.user_repository import UserRepository
from lib.user import User


def test_all(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()

    assert users == [
    User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'),
    User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
    User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user == User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu')

def test_create(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    created_user = repository.create(User(4, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4'))
    assert created_user == User(4, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4')

    result = repository.all()
    assert result == [
        User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'),
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'),
        User(4, 'Jane Doe', 'janedoe@bing.com' , '987654321', 'hashed_password_4')
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        User(2, 'Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'),
        User(3, 'Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q')
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
        User(1, 'Bob Doe', 'bobdoe@bing.com' , '987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G')
        ]
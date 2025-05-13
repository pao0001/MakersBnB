from lib.user import *

def test_init():
    user = User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', 'hashed_password_1')
    assert user.name == 'John Doe'
    assert user.id == 1
    assert user.email == 'johndoe@bing.com'
    assert user.phone_number == '1234567890'
    assert user.password_hash == 'hashed_password_1'


def test_user_format():
    user = User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', 'hashed_password_1')
    assert str(user) == "User(1, John Doe, johndoe@bing.com, 1234567890, hashed_password_1)"

def test_eq():
    user1 = User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', 'hashed_password_1')
    user2 = User(1, 'John Doe', 'johndoe@bing.com' , '1234567890', 'hashed_password_1')
    assert user1 == user2
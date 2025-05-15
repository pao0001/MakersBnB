from lib.user_repository import UserRepository
import bcrypt

class PasswordAuthenticator:
    def __init__(self, email, password, connection):
        self.email = email
        self.password = password
        self.connection = connection
        self.users = UserRepository(connection).all()

    def authenticate(self):
        for user in self.users:
            if user.email == self.email and user.password_hash == self.password:
                print('True')
                return True

class PasswordHasher:
    def __init__(self, password):
        self.password = password
        self.hashed_password = None
    
    def hash_password(self):
        self.hashed_password =bcrypt.hashpw(self.password)
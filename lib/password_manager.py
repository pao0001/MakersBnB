import bcrypt
from lib.user_repository import UserRepository

class PasswordManager:
    def __init__(self, email, password, connection):
        self.email = email
        self.password = password
        self.connection = connection
        self.users = UserRepository(connection).all()

    def authenticate(self):
        for user in self.users:
            if user.email == self.email:
                # Check hashed password
                if bcrypt.checkpw(self.password.encode('utf-8'), user.password_hash.encode('utf-8')):
                    print('Authenticated')
                    return True
        print('Authentication failed')
        return False

    def hash_password(self):
        return bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

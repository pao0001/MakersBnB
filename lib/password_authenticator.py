from lib.user_repository import UserRepository

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

# Def Class

class User:

    def __init__(self, id, name, email, phone_number, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password_hash = password_hash

    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.phone_number}, {self.password_hash})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return (
            self.id == other.id and
            self.name == other.name and
            self.email == other.email and
            self.phone_number == other.phone_number and
            self.password_hash == other.password_hash
        )

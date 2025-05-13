from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users') 
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"], row["phone_number"], row["password_hash"])
            users.append(item)
        return users
    
    def find(self, user_id):
        rows = self._connection.execute(
        'SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["phone_number"], row["password_hash"])
    
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users(name, email, phone_number, password_hash) VALUES (%s, %s, %s, %s) RETURNING id', (
            user.name, user.email, user.phone_number, user.password_hash
        ))
        row = rows[0]
        user.id = row["id"]
        print(f"{user} has been successfully created.")
        return user

    def delete(self, user_id):
        self._connection.execute('DELETE FROM properties WHERE user_id = %s', [user_id])
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        print("USER AND ALL ASSOCIATED PROPERTIES HAVE BEEN DELETED!!")
        return None


    def update(self, user):
        self._connection.execute('UPDATE users SET name = %s, email = %s, phone_number = %s, password_hash = %s WHERE id = %s RETURNING id',
        (user.name, user.email, user.phone_number, user.password_hash, user.id)
    )
        print(f"{user} has been successfully updated.")
        return user
from lib.property import *

class PropertyRepository:
    def __init__(self, connection):
        self._connection = connection

    # Get all available properties
    def all(self):
        rows = self._connection.execute('SELECT * FROM properties')
        properties = []
        for row in rows:
            item = Property(row["id"], row["name"], row["email"], row["phone_number"], row["address"], row["description"], row["price_per_night"], row["availability"], row["user_id"])
            properties.append(item)
        return properties
    
    # Find a single property by its id
    def find(self, property_id):
        rows = self._connection.execute(
            'SELECT * from properties WHERE id = %s', [property_id])
        row = rows[0]
        return Property(row["id"], row["name"], row["email"], row["phone_number"], row["address"], row["description"], row["price_per_night"], row["availability"], row["user_id"])

    # Create a new property
    def create(self, property):
        rows = self._connection.execute('INSERT INTO properties (name, email, phone_number, address, description, price_per_night, availability, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id', [property.name, property.email, property.phone_number, property.address, property.description, property.price_per_night, property.availability, property.user_id])

        row = rows[0]
        property.id = row["id"]
        print(property)
        return property

    # Delete a property by its id
    def delete(self, property_id):
        self._connection.execute(
            'DELETE FROM properties WHERE id = %s', [property_id])
        return None
    
    # Update a full property by its id
    def update(self, property):
        self._connection.execute('UPDATE properties SET name = %s, email = %s, phone_number = %s, address = %s, description = %s, price_per_night = %s, availability = %s, user_id = %s WHERE id = %s RETURNING id',
        (property.name, property.email, property.phone_number, property.address, property.description, property.price_per_night, property.availability, property.user_id, property.id)
    )
        return property
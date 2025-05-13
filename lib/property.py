

class Property:
    def __init__(self, 
                 id, 
                 name, 
                 availability, 
                 price_per_night, 
                 email, 
                 phone_number, 
                 address, 
                 description, 
                 user_id):
        self.id = id
        self.name = name
        self.availability = availability
        self.price_per_night = price_per_night
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.description = description
        self.user_id = user_id


    def __eq__(self, value):
        return self.__dict__ == value.__dict__
        
    def __repr__(self):
        return f"Property({self.id}, {self.name}, {self.availability}, {self.price_per_night}, {self.email}, {self.phone_number}, {self.address}, {self.description}, {self.user_id})"
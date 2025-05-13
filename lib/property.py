

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


    def __eq__(self, other):
        if not isinstance(other, Property):
            return NotImplemented
        return (
            self.id == other.id and
            self.name == other.name and
            self.availability == other.availability and
            self.price_per_night == other.price_per_night and
            self.email == other.email  and
            self.phone_number == other.phone_number  and
            self.address == other.address  and
            self.description == other.description  and
            self.user_id == other.user_id
            )
        
    def __repr__(self):
        return f"Property({self.id}, {self.name}, {self.availability}, {self.price_per_night}, {self.email}, {self.phone_number}, {self.address}, {self.description}, {self.user_id})"
    


    # def __eq__(self, other):
    # if not isinstance(other, User):
    #     return NotImplemented
    # return (
    #     self.id == other.id and
    #     self.name == other.name and
    #     self.email == other.email and
    #     self.phone_number == other.phone_number and
    #     self.password_hash == other.password_hash
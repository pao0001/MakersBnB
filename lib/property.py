

class Property:
    def __init__(self, 
                 id, 
                 name, 
                 email, 
                 phone_number, 
                 address, 
                 description, 
                 price_per_night, 
                 availability, 
                 user_id):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.description = description
        self.price_per_night = price_per_night
        self.availability = availability
        self.user_id = user_id



    
    def __eq__(self, other):
        if not isinstance(other, Property):
            return NotImplemented
        return (
            self.id == other.id and
            self.name == other.name and
            self.email == other.email and
            self.phone_number == other.phone_number and
            self.address == other.address and
            self.description == other.description and
            self.price_per_night == other.price_per_night and
            self.availability == other.availability and
            self.user_id == other.user_id
        )
        

    
    def __repr__(self):
        return (
            f"Property({self.id}, {self.name}, {self.email}, {self.phone_number}, "
            f"{self.address}, {self.description}, {self.price_per_night}, "
            f"{self.availability}, {self.user_id})"
        )

    
class Pet:
    def __init__(self):
        # Private data attributes
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    # Setter method for name attribute
    def set_name(self, name):
        self.__name = name
    
    # Setter method for animal_type attribute
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    # Setter method for age attribute
    def set_age(self, age):
        self.__age = age
    
    # Getter method for name attribute
    def get_name(self):
        return self.__name
    
    # Getter method for animal_type attribute
    def get_animal_type(self):
        return self.__animal_type
    
    # Getter method for age attribute
    def get_age(self):
        return self.__age

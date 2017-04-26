# Author: Jorge Rodriguez
# Date: April 16, 2017
# Pet Class Lab


class Pet:
    # init method to initialize the attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # set methods sets the pet name, animal_type, and age
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # get methods return the pet's name, animal_type and age
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

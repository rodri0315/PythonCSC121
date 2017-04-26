
# get the pets name, type and age from user
from chapter10 import PetClass

name = input("What is your pet's name? ")
animal_type = input("What type of animal is that? ")
age = input("How old is your pet? ")

# Create and instance of the Pet Class
my_pet = PetClass.Pet(name, animal_type, age)

print("Here is the information you entered: ")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())



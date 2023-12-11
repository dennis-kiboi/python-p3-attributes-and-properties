#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # Constructor
    def __init__(self, name="Fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    # getting name
    def get_name(self):
        print("Retrieving name.")
        return self._name
    
    # setting name
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # getting breed
    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    
    # setting breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
from Person import Person
from Bike import Bike

class Drive(Person, Bike):

    def __init__(self):
        super().__init__()

person = Person()
bike = Bike()
person.turnOnBike()
while(True):
    gear = input("Press 'u' to gear up and 'd' to gear down: ")
    if gear == 'u' or gear == 'd':                      
        person.changeGear(gear)
    if gear != 'u' and gear != 'd':
        break
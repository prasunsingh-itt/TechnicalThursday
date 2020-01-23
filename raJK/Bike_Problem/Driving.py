from Person import Person
from Bike import Bike

class Driving(Person, Bike):
    def __init__(self):
        print('This is Driving Class')
    
person = Person()
bike = Bike()

person.personName()
person.IsPersonReady()
person.turnOnBike()
bike.EngineON()
while True:
    g = input('Enter U for Gear UP or and D for Down \n')
    person.changeGear(g)
    print('Current Gear is ', person.bike.Gear)



    

    
    
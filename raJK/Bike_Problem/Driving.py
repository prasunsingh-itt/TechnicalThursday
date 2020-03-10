from Person import Person
from Bike import Bike

class Driving(): # Need not to Inherit
    def __init__(self):
        print('This is Driving Class')
    
person = Person()
bike = Bike()



person.personName() 
person.IsPersonReady()
person.turnOnBike()
bike.EngineON()

## you can still change it but it's not adviced
person.bike.__gear = 50

#You can't access it though
print(person.bike.__Gear)
while True:
    g = input('Enter U for Gear UP or and D for Down \n')
    person.changeGear(g)
    print('Current Gear is ', person.bike.__Gear)



    

    
    
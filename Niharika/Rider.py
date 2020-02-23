from Person import Person
from Bike import Bike

class Rider(Person, Bike):
    def __init__(self):
        print('Riding Class')
    
person = Person()
bike = Bike()

while (True):
    Action = input('U:Gear UP and D:Down \n')
    #person.Speedup(Action)
    if Action == "U":
        bike.SpeedUp()
        print('Current Gear is ', bike.Gear)
    else: 
        bike.SpeedDown()
        print('Current Gear is ', bike.Gear)
        

       
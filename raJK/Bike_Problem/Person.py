from Bike import Bike
class Person:
    def __init__(self):
        print('This is Person Class')
        self.bike = Bike()
        
    def IsPersonReady(self):
        print('Person is ready')

    def personName(self):
        print('My Name is Rajk')
    
    def turnOnBike(self):
        print('Turn on Bike')

    def turnOFFBike(self):
        print('Turn OFF Bike')

    def changeGear(self, UpdateGear):
        if UpdateGear == 'U':
            self.bike.GearUp()
        elif UpdateGear == 'D':
            self.bike.GearDown()
        else: 
            print('Invalid option')


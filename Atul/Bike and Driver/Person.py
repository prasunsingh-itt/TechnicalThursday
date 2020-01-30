from Bike import Bike

class Person():

    def __init__(self):
        super().__init__()
        self.bike=Bike()

    def turnOnBike(self):
        print("Bike has been started. Put the bike in first gear and start driving.")
        print("Have a safe journey!!")

    def changeGear(self, gear):
        if gear == 'u':
            self.bike.GearUp()
        if gear == 'd':
            self.bike.GearDown()
        


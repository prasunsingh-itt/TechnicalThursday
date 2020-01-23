class Bike():

    def __init__(self):
        self.Gear = 0

    def GearUp(self):
        if self.Gear < 5:
            self.Gear += 1
            print("You are in gear",self.Gear)
        else:
            print("Gear box todega kya!!!")

    def GearDown(self):
        if self.Gear > 0:
            self.Gear -= 1
            print("You are in gear",self.Gear)
        else:
            print("Ab kya neutral se neeche jaega!!!")



        
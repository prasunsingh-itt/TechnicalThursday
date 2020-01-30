class Bike:
    def __init__(self):
        self.Gear = 0
        print('This is Bike Class')

    def GearUp(self):
        if self.Gear + 1 < 6 :
            self.Gear = self.Gear + 1
        else:
            print('Already in TOP GEAR')

    def EngineON(self):
        print('Bike is ON')

    def EngineOFF(self):
        print('Bike is OFF')

    def GearDown(self):
        if self.Gear > 0:
            self.Gear = self.Gear - 1
        else:
            print('Already in BOTTOM GEAR')

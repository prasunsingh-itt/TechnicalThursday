class Bike():

    def __init__(self):
        self.Gear = 0
        print('Bike Class')


    def StartBike(self):
        print('Bike Started')

    def SpeedUp(self):
        if self.Gear <= 6 :
            self.Gear = self.Gear + 1
        else:
            print('Max speed obtained')

    def SpeedDown(self):    
        if self.Gear > 0:
            self.Gear = self.Gear - 1
        else:
            print('Min speed obtained')

    def StopBike(self):
        print('Bike Stopped')
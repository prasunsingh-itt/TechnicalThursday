from parentbike import Bike

class Aprilla(Bike):

    def __init__(self):
        self.Type = "Bike"
        print ("Bike is Aprilla")
        print("Aprilla is ready to go for a ride")

    def bike_start(self):
        self.speed = 10
        print('Speed = '+ str(self.speed) + '\n')

    def speedup(self):
        print ('Speed Increased')
        self.speed = self.speed+20
        print('Speed = '+ str(self.speed) + '\n')

    def speeddown(self):
        print ('Speed Decreased')
        self.speed = self.speed-20
        print('Speed = '+ str(self.speed) + '\n')

if __name__ == "__main__":
    a = Aprilla()
    a.bike_start()
    a.speedup()
    a.speeddown()
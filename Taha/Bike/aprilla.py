from bike import Bike

class Aprilla(Bike):

    def __init__(self):
        self.__Type = "Bike"
        self.__gear = 0
        self.__speed = 0
        print ("Bike is Aprilla")
        print("Aprilla is ready to go for a ride")

    def bike_start(self):
        self.__speed = 10
        print('Speed = '+ str(self.__speed) + '\n')

    def speedup(self):
        print ('Speed Increased')
        self.__speed = self.__speed+20
        print('Speed = '+ str(self.__speed) + '\n')

    def speeddown(self):
        print ('Speed Decreased')
        self.__speed = self.__speed-20
        print('Speed = '+ str(self.__speed) + '\n')

if __name__ == "__main__":
    a = Aprilla()
    a.bike_start()
    a.speedup()
    a.speeddown()
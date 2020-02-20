class Bike():
    def __init__(self):
        self.__gear = 0
        # print("This is Bike Class")

    def start(self):
        print("Bike Started")
        self.__speed = 20
        self.__gear = 1
        print('Speed = '+ str(self.__speed) + '\nGear = '+str(self.__gear)+'\n')
    
    def speedup(self):
        if (self.__gear < 6 or self.__speed < 140):
            print ('Speed Increased')
            self.__speed = self.__speed + 20
            self.__gear = self.__gear + 1
            print('Speed = '+ str(self.__speed) + '\nGear = '+str(self.__gear)+'\n')
        else:
            print("Max Gear!!!!!!!!!!!!!!!! \nCannot change gear")

    def speeddown(self):
        if (self.__gear > 1 or self.__speed < 0):
            print ('Speed Decreased')
            self.__speed = self.__speed - 20
            self.__gear = self.__gear - 1
            print('Speed = '+ str(self.__speed) + '\nGear = '+str(self.__gear)+'\n')
        else:
            print("Already on Neutral!!!!!!!!!!!!!\nCannot Gear Down")
    def stop(self):
        print("Bike Stopped")

if __name__ == "__main__":
    bike=Bike()
    bike.start()
    bike.speedup()
    bike.speeddown()
    bike.stop()



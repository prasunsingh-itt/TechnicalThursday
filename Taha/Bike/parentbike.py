class Bike():
    def __init__(self):
        self.Type = "Bike"
        print("Bike is started")


    def bike_start(self):
        self.speed = 10
        self.gear = 1
        print('Speed = '+ str(self.speed) + '\nGear = '+str(self.gear)+'\n')
    
    def speedup(self):
        print ('Speed Increased')
        self.speed = self.speed+20
        self.gear = self.gear+1
        print('Speed = '+ str(self.speed) + '\nGear = '+str(self.gear)+'\n')

    def speeddown(self):
        print ('Speed Decreased')
        self.speed = self.speed-20
        self.gear = self.gear-1
        print('Speed = '+ str(self.speed) + '\nGear = '+str(self.gear)+'\n')

    # bikename = input('Enter the bike to ride \n 1.Duke \n 2.Avenger : ')
    # if bikename == '1':
    #     bikename = 'duke'

    # elif bikename == '2':
    #     bikename = 'avenger'
if __name__ == "__main__":
    b=Bike()
    b.bike_start()
    b.speedup()
    b.speeddown()

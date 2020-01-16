from bike import Bike
#note the format for import

class Avenger(Bike):
    

    def __init__(self):
        #super(Avenger, self).__init__()
        self.gearbox = 1

    def print_gear(self):
        print(self.gearbox)


a = Avenger()
a.print_gear()
print(a)
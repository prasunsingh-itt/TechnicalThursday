from bike import Bike

class Person:
    def __init__(self, name):
        self.__name = name
        self.ready = name + " is ready to ride the bike"
        print(self.ready)
        self.bike = Bike()
    
    def start_bike(self):
        self.bike.start()
    
    def change_gear(self,gear):
        if (gear == 'U'):
            self.bike.speedup()
        elif (gear == 'D'):
            self.bike.speeddown()

if __name__ == "__main__":
    a = person('Taha')
    a.start_bike()
    a.change_gear('U')
    a.change_gear('D')
    a.change_gear('D')
    a.change_gear('D')
    # a.change_gear('U')
    # a.change_gear('U')
    # a.change_gear('U')
    # a.change_gear('U')

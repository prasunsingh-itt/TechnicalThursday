class Vehicles():
    bike = ""
    def __init__(self, bike):
        self.bike = bike

    def display(self):
        print(self.bike + " is ready to ride")

class Rider():
    rider = ""

    def __init__(self, ridername):
        self.rider = ridername

    def displayRider(self):
        print("Rider Name is : " + self.rider)

    def display(self):  #overriden method.
        print(self.rider + " is riding the "+ b.bike + " bike")

class Bike(Vehicles):
    total_gears = 0
    engine_status =False
    current_gear = 0
    def __init__(self,gear,engine_status):
        self.total_gears = gear
        self.engine_status = engine_status

    def instruction(self):
        print("Bike has " ,self.engine_status)
        print("Bike has ", self.total_gears, " gears")
        print("Bike can be ", self.engine_status, " at any time by turning the key")

    
    def speedUp(self):
        self.current_gear = self.current_gear+1
        print("Bike is in  ", self.current_gear, " gear")
        print("speedup")

    def speeddown(self):
        self.current_gear = self.current_gear-1
        print("Bike is in  ", self.current_gear, " gear")
        print("speeddown")


b = Vehicles("Unicorn")
b.display()

c = Rider("Manjunath")
c.displayRider()
c.display()

r = Bike(5,True)
r.instruction()
ch = 'U'
while ch != None:
    print(ch,ch != None)
    print("if You want to ride the bike then press U to speedUp and  D to Speeddown and Press any to quit")
    ch = input()
    if ch == 'U':
        r.speedUp()
    elif ch == 'D':
        r.speeddown()
    else:
        print(ch,ch != None)
        ch = None



class Motorcycle: 

    maxspeed = 0
    minspeed = 0
    gear = ""

    def __init__(self, maxspeed, minspeed, gear):
        self.maxspeed = maxspeed
        self.minspeed = minspeed
        self.gear = gear
    def gear(self):
        self.get_gear = True
        return self.get_gear
    def speed(self, speed):
        self.speed = self.minspeed + self.accelerate
        return self.speed

    def accelerate(self, accelerate):
        self.accelerate = accelerate
        if (self.accelerate + self.minspeed) > self.maxspeed:
            print("This motorcycle cannot go that fast")
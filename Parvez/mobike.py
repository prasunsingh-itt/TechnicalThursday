class Motorcycle:

    def __init__(self, maxspeed, minspeed, gear):
        self.maxspeed = maxspeed
        self.minspeed = minspeed
        self.speed = minspeed # Initial speed is equal to minspeed
        self.gear = gear

    # Printing methods
    # Print gear status
    def has_gear(self):
        if self.gear:
            print("This motorcycle has a gear")
        else:
            print("This motorcycle does not have a gear")
    # Print speed
    def how_fast(self):
        print ("The current speed of this motorcycle is {}".format(self.speed))

    # Methods to change your gear status:
    def add_gear(self):
        self.gear = True
    def remove_gear(self):
        self.gear = False
    # Method to accelerate
    def accelerate(self, accelerate):
        if (self.speed + accelerate) > self.maxspeed:
            print("This motorcycle cannot go that fast")
        else:
            self.speed += accelerate

motorcycleOne = Motorcycle(90.0, 65.0, True)
motorcycleTwo = Motorcycle(85.0, 60.0, False)

motorcycleOne.accelerate(30.0)
motorcycleTwo.accelerate(20.0)

motorcycleOne.how_fast()
motorcycleTwo.how_fast()

motorcycleOne.has_gear()
motorcycleTwo.has_gear()
#from Bike import Bike
class Scooty:
    def __init__(self):
        print("Scooty Started")

    def stop(self):
        print("Scooty stops")

    def Speed_Up(self , current_speed , gear):
        self.gear = gear + 1
        self.current_speed = current_speed + 10
        print("Scooty is at Gear: %s" % (self.gear))
        print("Scooty's Speed after gear up: %s" % (self.current_speed))
        
    def Speed_down(self , current_speed , gear):
        self.gear = gear - 1
        self.current_speed = current_speed - 10
        print("Scooty is at Gear: %s" % (self.gear))
        print("Scooty Speed after gear down: %s" % (self.current_speed))


Object = Scooty()
Object.Speed_Up(30 , 1)
Object.Speed_down(30 , 2)
Object.stop()


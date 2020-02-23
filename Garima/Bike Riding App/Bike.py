class Bike:

    def __init__(self):
        print("Bike Started")

    def stop(self):
        print("Bike stop")

    def Speed_Up(self , current_speed , gear):
        self.gear = gear + 1
        self.current_speed = current_speed + 10
        print("bike is at Gear: %s" % (self.gear))
        print("Bike's Speed after gear up: %s" % (self.current_speed))
        
    def Speed_down(self , current_speed , gear):
        self.gear = gear - 1
        self.current_speed = current_speed - 10
        print("bike is at Gear: %s" % (self.gear))
        print("Bike's Speed after gear down: %s" % (self.current_speed))
      

#if __name__ == "__main__":
Object = Bike()
Object.Speed_Up(30 , 1)
Object.Speed_down(30 , 2)
Object.stop()


class Vehicle():
    def __init__(Type):
        type="Bike"
  
class Bike(Vehicle):
    def __init__(self, name, max_speed):
        max_speed = min(max_speed, 30)
        super().__init__(name, max_speed)

class Yamaha(Vehicle):
    def __init__(self):
        self.colour= 'blue'
        self.gears= 5
        self.engine_type= 'air-cooled'
        print("Specification are:\nColour: " +self.colour +"\nGear: "+str(self.gears) + "\nEngine: "+ self.engine_type)

a = Yamaha()

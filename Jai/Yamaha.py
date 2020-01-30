class Yamaha():
    def __init__(self, bike):
        self.bike = bike

    def display(self):
        print(self.bike + " is ready to ride")

class Bike(Yamaha):
    total_gears = 0
    engine_status =False
    current_gear = 0
    def __init__(self,gear,engine_status):
        self.total_gears = gear
        self.engine_status = engine_status
   
    def speedUp(self):
        self.current_gear = self.current_gear+1
        print("Bike is in  ", self.current_gear, " gear")
        print("Speed Up")

    def speeddown(self):
        self.current_gear = self.current_gear-1
        print("Bike is in  ", self.current_gear, " gear")
        print("Speed Down")


bike = Bike("Yamaha")
bike.display()

range = Bike(5,True)
range.instruction()
choice = 'UP'
while choice!= None:
     print(choice,choice != None)
     print("if You want to ride the bike then press UP to speedUp and  DOWN to Speed down and Press any to quit")
     choice = input()
      if choice == 'UP':
         range.speedUp()
      elif choice == 'DOWN':
        range.speeddown()
      else:
        print(ch,ch != None)
        choice = None
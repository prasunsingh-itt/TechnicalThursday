class Bike:
    def __init__(self,current_speed):
        self.current_speed=current_speed
    def vehicle_type(self):
      return 'Bike'
    def no_of_wheels(self):
      print("Bike has 2 wheels")
    def gear_up(self,current_speed):
      self.current_speed=self.current_speed+10
      print("speed after gear_up is :", self.current_speed)
    def gear_down(self,current_speed):
      self.current_speed=self.current_speed-10
      print("speed after gear_down is :", self.current_speed)
class Pulsar(Bike):
    def __init__(self,modelName):
        self.modelName=modelName
    def PulsarModel(self):
        return self.modelName

bikeobj=Bike(30)
pulsarobj=Pulsar('Bazaz Pulsar')
print("Model = %s" % (pulsarobj.PulsarModel()))
bikeobj.gear_up(30)
bikeobj.gear_down(30)

       


       

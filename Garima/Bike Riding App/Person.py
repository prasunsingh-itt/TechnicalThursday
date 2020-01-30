from Bike import Bike

class Person(Bike):
    def __init__(self , Model , Color ,argument):
        self.Color = Color
        self.Model = Model

    def Call_VehicleType(self):
        if(self.argument == 0):
            super().__init__(30)
        else :
            print("djhc")
            
    def show(self):
        print("Color = %s" % (self.Color))
        print("Model = %s" % (self.Model))
    
    def get_class_name(self):
        return self.__class__.__bases__[0].__name__

Object = Person("Pulser" , "Red" , 0)
Object.Call_VehicleType()
#Object = Scooty("Red" , "Pep")
#Object.show()
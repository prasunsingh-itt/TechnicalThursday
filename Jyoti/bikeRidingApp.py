class Rider(): 
    def __init__(self,personname):
        self.personname=personname
        print(self.personname," is riding the bike")

class Bike():

    def __init__(self,bikename):
        self.bikename = bikename
        print("Bike:",self.bikename)

    def gearUp(self,currentSpeed):
        print("Current speed is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(10)," kmph")

    def gearDown(self,currentSpeed,super):
        print("Current speed is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(10)," kmph")

class Yamaha(Bike,Rider):
    
    def __init__(self,bikename,personname):
        super().__init__(bikename)
        super().__init__(personname)
    
    def gearUp(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(20)," kmph")

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(20)," kmph")

class Honda(Bike,Rider):

    def __init__(self,bikename,personname):
        super().__init__(bikename)
        super().__init__(personname)

    def gearUp(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(30))

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(30)," kmph")


yamahaobj=Yamaha("Yamaha","Neel")

yamahaobj.gearUp(10)
yamahaobj.gearDown(50)

hondaobj=Honda("Honda","Rahul")
hondaobj.gearUp(10)
hondaobj.gearDown(10)

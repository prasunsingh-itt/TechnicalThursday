class Rider(object): 
    def __init__(self,personname):
        self.personname=personname

class Bike():

    def gearUp(self,currentSpeed):
        print("Current speed is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(10)," kmph")

    def gearDown(self,currentSpeed):
        print("Current speed is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(10)," kmph")

class Yamaha(Bike,Rider):
    
    def __init__(self,personname,bikename):
        print("Bike :",super().__init__(bikename=bikename)) 
        print(super().__init__(personname=personname)," is riding the bike")
    
    def gearUp(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(20)," kmph")

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(20)," kmph")

class Honda(Bike,Rider):

    def __init__(self,personname,bikename):
        print("Bike :",super().__init__(bikename=bikename)) 
        print(super().__init__(personname=personname)," is riding the bike")

    def gearUp(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(30))

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(30)," kmph")


riderobj=Rider("Sadaan")
yamahaobj=Yamaha("Neel","Yamaha")
hondaobj=Honda("Rahul","Honda")

yamahaobj.getName()
yamahaobj.gearUp(10)
yamahaobj.gearDown(50)

hondaobj.getName()
hondaobj.gearUp(10)
hondaobj.gearDown(10)

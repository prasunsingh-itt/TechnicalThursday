class Person: 
        def personName(self,personname):
            self.personname=personname

class Bike(Person):
    def getName(self):
        print("Bike:")

    def gearUp(self,currentSpeed,personname):
        print("Current speed is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(10)," kmph")

    def gearDown(self,currentSpeed,personname):
        print("Current speed is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(10)," kmph")

class Yamaha(Bike):
    
    def getName(self):
        print("Bike: Yamaha")

    def getRiderName(self,personname):
        print(personname," is riding the bike")
    
    def gearUp(self,currentSpeed):
        print()
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(20)," kmph")

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(20)," kmph")

class Honda(Bike):
    
    def getName(self):
        print("Bike: Honda")

    def getRiderName(self,personname):
        print(personname," is riding the bike")

    def gearUp(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after gearup : ",int(currentSpeed)+int(30))

    def gearDown(self,currentSpeed):
        print("Current speed of bike is :",int(currentSpeed))
        print("Speed after geardown : ",int(currentSpeed)-int(30)," kmph")


bikeobj=Bike()
yamahaobj=Yamaha()
hondaobj=Honda()
personobj=Person()

yamahaobj.getName()
yamahaobj.getRiderName("Shubham")
yamahaobj.gearUp(10)
yamahaobj.gearDown(50)

hondaobj.getName()
yamahaobj.getRiderName("Neel")
hondaobj.gearUp(10)
hondaobj.gearDown(10)

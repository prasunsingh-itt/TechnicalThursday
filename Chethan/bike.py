class Bike:
    def __init__(self,Name,speed):
        self.name=Name
        self.speed=speed
    def description(self):
        return "{} is running in {} speed".format(self.name,self.speed)

class RoyalEnfield(Bike):
    def speedup(self):
        self.speed=self.speed+10
        print("speed is increased")
        return self.speed
        #self.gear=self.gear+1
    def speeddown(self):
        self.speed=self.speed-10
        print("speed is decreased")
        return self.speed
        #self.gear=self.gear-1

a=RoyalEnfield("Royal Enfield",20)
b=a.speedup()
c=a.speedup()
print(a.description())
d=a.speeddown()
print(a.description())


#Speed can go negative or Postive infinity
#Divide it into proper files.
#Rider is missing
#Gear should be there.
#Object name could be more clear

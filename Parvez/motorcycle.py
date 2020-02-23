class motorcycle:


    def __init__(self,total):
        self.gears = 0
        self.total=total
        
   
    def Upshift(self):
        if self.gears + 1 < 6 :
            self.gears = self.gears + 1
        else:
            print('Already in TOP GEAR')



    def has_gear(self,total):
        if self.total>0:
            print("This motorcycle has a gear")
        else:
            print("This motorcycle does not have a gear")



    def EngineOFF(self):
        print('Bike is OFF')



    def Downshift(self):
        if self.gears > 0:
            self.gears = self.gears - 1
        else:
            print('Already in BOTTOM GEAR')
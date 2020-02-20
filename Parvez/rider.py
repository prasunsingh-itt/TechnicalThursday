from motorcycle import motorcycle

class rider:
    def __init__(self):
        print('This is rider Class')
        self.motorcycle = motorcycle(6)

    def riderName(self):
        print('Rossi')
    
    def gearshift(self, UpdateGear):
        if UpdateGear == 'U':
            self.bike.Upshift()

        elif UpdateGear == 'D':
            self.bike.Downshift()
        else: 
            print('Invalid option')

r = rider()
r.riderName()
motorcycle=motorcycle(6)
while True:
    #t = input('ENter the number of gears \n')
    #motorcycle.has_gear(t)
    g = input('Enter U for Gear UP or and D for Down \n')
    if g=="U":
        motorcycle.Upshift()
        print('Current Gear is ', motorcycle.gears)
    else:
        motorcycle.Downshift()
        print('Current Gear is ', motorcycle.gears)

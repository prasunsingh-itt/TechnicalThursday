from parentbike import Bike

class person:
    def __init__(self, name):
        self.name = name
        self.ready = name + " is ready to ride the bike"
        print(self.ready)
        self.bike = Bike()

    def speedup(self):
        self.bike.speedup()

    def speeddown(self):
        self.bike.speeddown()



a = person('Taha')
# a.speedup()
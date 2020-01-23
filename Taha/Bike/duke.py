from parentbike import Bike

class Duke(Bike):

    def __init__(self):
        self.Type = "Bike"
        print ("Bike is Duke")
        print("Duke is ready to go for a ride")

    def bike_start(self):
        super().bike_start()

    def speedup(self):
        super().speedup()

    def speeddown(self):
        super().speeddown()

if __name__ == "__main__":
    a = Duke()
    a.bike_start()
    a.speedup()
    a.speeddown()
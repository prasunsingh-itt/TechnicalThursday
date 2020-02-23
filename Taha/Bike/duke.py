from bike import Bike

class Duke(Bike):

    def __init__(self):
        self.__Type = "Bike"
        print ("Bike is Duke")
        print("Duke is ready to go for a ride")
        self.bike = Bike()
        self.__gear = 0
        self.__speed = 0

    def start(self):
        super().start()

    def speedup(self):
        super().speedup()

    def speeddown(self):
        super().speeddown()

    def stop(self):
        super().stop()

if __name__ == "__main__":
    duke = Duke()
    duke.start()
    duke.speedup()
    duke.speeddown()
    duke.stop()
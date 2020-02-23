from bike import Bike


class Kawasaki(Bike):
    def __init__(self, topSpeed, noOfGears):
        super().__init__(topSpeed, noOfGears)

    def gearUp(self):
        if self._gearPosition is self._noOfGears:
            print("You are riding bike in top gear")
        else:
            self._gearPosition = self._gearPosition+1
            self._currentSpeed = (self._topSpeed//4)*self._gearPosition
            print("Gear changed to ", self._gearPosition,
                  " Current speed is", self._currentSpeed)

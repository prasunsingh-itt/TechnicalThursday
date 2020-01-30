
from engine_status import EngineStatus


class Bike:

    def __init__(self, topSpeed, noOfGears):
        super().__init__()
        self._gearPosition = 0
        self._topSpeed = topSpeed
        self._noOfGears = noOfGears
        self._currentSpeed = 0
        self._status = EngineStatus.STOPPED

    def getGearPosition(self):
        return self._gearPosition

    def getNoOfGears(self):
        return self._noOfGears

    def getCurrentSpeed(self):
        return self._currentSpeed

    def getEngineStatus(self):
        return self._status

    def start(self):
        if EngineStatus.STARTED is self._status:
            print("Engine is already started..!!")
        else:
            self._status = EngineStatus.STARTED
            print("Engine started..!!")

    def stop(self):
        if EngineStatus.STOPPED is self._status:
            print("Engine is already stopped..!!")
        else:
            self._status = EngineStatus.STOPPED
            print("Engine stopped..!!")

    def gearUp(self):
        if self._gearPosition is self._noOfGears:
            print("You are riding bike in top gear")
        else:
            self._gearPosition = self._gearPosition+1
            self._currentSpeed = (self._topSpeed//6)*self._gearPosition
            print("Gear changed to ", self._gearPosition,
                  " Current speed is", self._currentSpeed)

    def gearDown(self):
        if self._gearPosition is 0:
            print("Bike is in newtrol position")
        else:
            self._gearPosition = self._gearPosition-1
            self._currentSpeed = (self._topSpeed//7)*self._gearPosition
            print("Gear changed to ", self._gearPosition,
                  " Current speed is", self._currentSpeed)

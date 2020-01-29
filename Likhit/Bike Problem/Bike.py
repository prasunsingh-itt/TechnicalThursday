class Bike:

    def __init__(self, maxSpeed, totalGears):
        super().__init__()
        self._gearPos = 0
        self._maxSpeed = maxSpeed
        self._totalGears = totalGears
        self._curSpeed = 0
        self._bikeStatus = 0

    def start(self):
        if self._bikeStatus is 0:
            print("Bike started..!!")
        else:
            self._status = 0
            print("Bike alreay in started state")

    def stop(self):
        if self._bikeStatus is 1:
            print("Bike Already stopped")
        else:
            self._status = 1
            print("Bike stopped")

    def totalGears(self):
        return self.totalGears

    def getCurrSpeed(self):
        return self._curSpeed

    def gearPosition(self):
        return self._gearPos

    def gearUpShift(self):
        if self._gearPos is self._totalGears:
            print("Bike in Max Gear")
        else:
            self._gearPos = self._gearPos+1
            self._curSpeed = self._maxSpeed + 10
            print("gear shifted to position ", self._gearPos,
                  " Bike is running at", self._curSpeed)

    def gearDownShift(self):
        if self._gearPos is 0:
            print("Gear in Default value")
        else:
            self._gearPos = self._gearPos-1
            self._curSpeed = self._maxSpeed - 10
            print("gear shifted to position ", self._gearPos,
                  " Bike is running at", self._curSpeed)

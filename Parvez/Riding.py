from rider import rider
from motorcycle import motorcycle

class riding(rider, motorcycle):

    def __init__(self):
        self.rider = rider()

a = riding()

motorcycle = motorcycle(6)



rider.riderName()




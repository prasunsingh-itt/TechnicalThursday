from abc import abstractmethod, ABC

class Bike(ABC):

    def __init__(self):
        self.Type = "Bike"
        self.gear = 0

    def bike_start(self):
        print("Bike is started")


    def free_to_implement(self):
        pass


    # @abstractmethod
    # def implement_this(self):
    #     pass

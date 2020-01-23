class Person:
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def getName(self):
        return self.__name

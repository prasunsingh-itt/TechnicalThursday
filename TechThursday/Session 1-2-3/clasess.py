import tkinter
from swampy.Lumpy import Lumpy

class Dog:
#
    # create a Lumpy object
    lumpy = Lumpy()
    # capture reference state
    lumpy.make_reference()

    a = 10
    b = 20
    def __init__(self, name, color):
        self.name = name
        self.color= color
    


    def speak_identity(self, name):
        print(self.name)
        print(self.color)
        print(self)
        print(name)

    # draw the current state (relative to the reference state)
    lumpy.object_diagram()




dogObject = Dog("Ob1", "Color1")
dogObject2 = Dog("Ob2", "Color2")

dogObject.speak_identity("OB1")
dogObject2.speak_identity("OB2")





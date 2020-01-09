class Dog:
    

    def __init__(self,name,color):
        self.name="Harry"
        self.color="white"


    def speak_identity(self,name):
        print(self.name)
        print(self.color)
        print(self)
        print(name)
        pass

dogObject=Dog("obj","color")

dogObject2=Dog("obj1","color1")
dogObject.speak_identity("ram")
dogObject2.speak_identity("ob2")
   
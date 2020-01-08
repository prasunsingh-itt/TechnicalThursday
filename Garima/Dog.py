
class Dog:
    name = "Brun"
    breed = "German stepherd"
#self - instance / reference of that object
    def speak_identity(self , name) :
        print(self.name)
        print(self.breed)
        print(self)
        print(type(name))
    
    def _init_(self , name , breed):
        self.name = name
        self.breed = breed

dogobject = Dog("a", "1")
#dogobject2 = Dog("b" , "2")
#dogobject.speak_identity("one")
#dogobject2.speak_identity(10)
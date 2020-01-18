class Dog:
   
    def __init__(self):   #initializing the constructor #__ builtin function
       self.name=name      #self is equivalent to this in java
       self.color=color
    
    def speak_identity(self):
        print(self.name)
        print(self.color)
        print(self)
        print(name)
        pass

dogObject=Dog("Bruno","Brown")   
dogObject2=Dog("Rocky","Black")

dogObject.speak_identity("Bruno") 
dogObject2.speak_identity("Rocky")
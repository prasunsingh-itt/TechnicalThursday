from ParentBirdClass import Bird
from Parrot import Parrot


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    # def whoisThis(self):
    #     print("Penguin")

    def run(self):
        print("Run faster")

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

peggy = Penguin()
# peggy.whoisThis()
# print(peggy.a)
# # peggy.swim()
# # peggy.run()


#Validating the instances
# print("#Validating the instances")
# print(isinstance(peggy,Bird))
# print(isinstance(peggy,object))
# print(isinstance(peggy,Penguin))

# #Validating the subclass
# print("#Validating the subclass")
# print(issubclass(Penguin,Bird))
# print(issubclass(Penguin,Parrot))
# print(issubclass(Bird,Parrot))
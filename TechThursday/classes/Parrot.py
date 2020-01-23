from ParentBirdClass import Bird


# child class (Inheritance)
class Parrot(Bird):

    def __init__(self):
        # call super() function
        # --super().__init__()
        print("Parrot is ready")

    
    #Overiding
    def whoisThis(self):
        print("Parrot")

    def run(self):
        print("Run faster")

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

# if __name__ == '__main__':
#     print(__name__)
#     peter = Parrot()
#     peter.whoisThis()
#     peter.swim()
#     peter.run()
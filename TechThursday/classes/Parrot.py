from ParentBirdClass import Bird


# child class
class Parrot(Bird):

    def __init__(self):
        # call super() function
        # --super().__init__()
        print("Parrot is ready")

    def whoisThis(self):
        print("Parrot")

    def run(self):
        print("Run faster")

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

peter = Parrot()
peter.whoisThis()
peter.swim()
peter.run()
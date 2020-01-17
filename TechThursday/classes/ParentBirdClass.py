# parent class

class Bird:

    a =10 
    
    def __init__(self):
        self.a = 100 
        # Bird.a = self.a
        # print(self.a)
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# b = Bird()
# # # print(b.a)

# b.whoisThis()

# +> Static 
# => Non Static => Object
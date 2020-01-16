from Polygon import Polygon

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)
    
    def findArea(self):
        a, b, c, d = self.sides

        print (4 * a)

    # def overloading(self, a, b):
    #     print(a+b)
    #     print("overloading 1")

    # def overloading (self, a,b,c):
    #     print (a+b+c)
    #     print("overloading 2")

    














    # def overloading(self, a, b):
    #     if type(a) == int and type(b) ==int:
    #         print("int")
    #         print (a+b)
    #     if type(a) == str and type(b) == str:
    #         print("string")
    #         print(a+b)

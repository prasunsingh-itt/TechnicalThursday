class Calculator:
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    #subtraction
    def subtraction(self):
        return self.num2 - self.num1

    #multiplication
    def multiplication(self):
        return self.num1 * self.num2

    #division
    def division(self):
        return self.num1 / self.num2


obj1 = Calculator(2 , 4)
print("Addition: %s" % (obj1.addition()))
print("Subtraction : %s" % (obj1.subtraction()))
print("Multiplication : %s" % (obj1.multiplication()))
print("Division : %s" % (obj1.division()))

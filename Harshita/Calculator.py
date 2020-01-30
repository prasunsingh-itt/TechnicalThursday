class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def Addition(self):
        return self.num1 + self.num2

    def Subtraction(self):
        return self.num1 - self.num2

    def Multiplication(self):
        return self.num1 * self.num2

    def Division(self):
        return self.num1 / self.num2

CalObj=calculator(5,10)
print("Addition is : %s" % (CalObj.Addition()))
print("Subtraction is: %s" % (CalObj.Subtraction()))
print("Multiplication is: %s" % (CalObj.Multiplication()))
print("Division is : %s" % (CalObj.Division()))
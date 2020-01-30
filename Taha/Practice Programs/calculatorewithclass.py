class calculator:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def addition(self):
        return int(self.num1) + int(self.num2)

    def subtraction(self):
        return int(self.num1) - int(self.num2)

    def division(self):
        return int(self.num1) // int(self.num2)

    def multiplication(self):
        return int(self.num1) * int(self.num2)

    def op(self):
        opera = int(self.operator)

        operation={
        1: self.addition(),
        2: self.subtraction(),
        3: self.division(),
        4: self.multiplication()
        }
        print (operation.get(opera, "Invalid Operator"))

 


num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
operator = input(" 1.Add \n 2.Sub \n 3.Div \n 4.Mul \n Enter the operation to be done: ")
obj = calculator(num1,num2,operator)
obj.op()


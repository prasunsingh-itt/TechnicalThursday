class Calculator:
    
     def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

     def addition(self):
       print(self.num1+self.num2)

   

     def substraction(self):
       print(self.num1-self.num2)

   

     def multiplication(self):
       print(self.num1*self.num2)

    

     def division(self):
       print(self.num1/self.num2)

     
calculatorObject=Calculator(10,20)
calculatorObject.addition()
calculatorObject.substraction()
calculatorObject.multiplication()
calculatorObject.division()

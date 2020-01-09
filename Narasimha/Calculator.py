class Calculator:
    def addition(self,value1,value2):
        return value1+value2

    def substraction(self,value1,value2):
        return value1-value2

    def multiplication(self,value1,value2):
        return value1*value2

    def division(self,value1,value2):
        return value1//value2
    
    def calculate(self,operation,value1,value2):
        result=None
        if operation == 1:
            result=self.addition(value1,value2)
        elif operation == 2:
            result=self.substraction(value1,value2)
        elif operation == 3:
            result=self.multiplication(value1,value2)
        elif operation == 4:
            result=self.division(value1,value2)
        else:
            print('Invalid operation')
        return result

print('Enter choose operation')
print('1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n')
operation=int(input(""))
value1=int(input("Enter first value\n"))
value2=int(input("Enter second value\n"))
calculator= Calculator()

print "Result is: ",calculator.calculate(operation,value1,value2)

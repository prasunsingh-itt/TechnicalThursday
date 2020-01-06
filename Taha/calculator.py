def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplication(num1,num2):
    return num1*num2

def op(num1, num2, oper):
        opera = int(oper)

        operation={
    1: addition(num1,num2),
    2: subtraction(num1,num2),
    3: division(num1,num2),
    4: multiplication(num1,num2)
    }
        print (operation.get(opera, "Invalid Operator"))

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator = input(" 1.Add \n 2.Sub \n 3.Div \n 4.Mul \n Enter the operation to be done: ")
op(num1,num2,operator)
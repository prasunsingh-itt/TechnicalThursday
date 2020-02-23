# Program make a simple calculator

def add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x/y

print("Select one option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division)")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == "2":
    print(num1, "+",num2, "=",Subtract(num1,num2))

elif choice =="3":
    print(num1,"+",num2, "=",multiply(num1,num2))

elif choice == "4":
    print(num1,"+",num2,"=",division(num1,num2))

else:
    print("Invalid option")
    



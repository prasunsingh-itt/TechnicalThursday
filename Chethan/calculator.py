a=input("Enter the first Number: ")
b=input("Enter the Second Number: ")
c=input("Enter the Operator: ")
if c=="+":
    print(int(a)+int(b))
elif c=="-":
    print(int(a)-int(b))
elif c=="*":
    print(int(a)*int(b))
elif c=="/":
    print(int(a)/int(b))
elif c=="%":
    print(int(a)%int(b))
else:
    print("Please provide proper operator")
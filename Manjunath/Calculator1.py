def readfirstnumber(c):
    print("Enter the 1st number ")
    a = input()
    return a

def readsecondnumber(c):
    print("Enter the 2nd number")
    b = input()
    return b

def sum(a,b):
    c = int(a)+int(b)
    print("Addition of "+a+" and "+b+" is "+str(c))
    
def sub(a,b):
    c = int(a)-int(b)
    print("Subtration "+a+" and "+b+" is "+str(c))

def mul(a,b):
    c = int(a)*int(b)
    print("multiplication "+a+" and "+b+"  is "+str(c))

def div(a,b):
    c = int(a)/int(b)
    print(type(c))
    print("division is "+a+" and "+b+" is " +str(c))

# taking the choice of the user1

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")

if choice =='1':
    a = readfirstnumber(choice)
    b = readsecondnumber(choice)
    sum(a,b)

if choice =='2':
    a = readfirstnumber(choice)
    b = readsecondnumber(choice)
    sub(a,b)

if choice =='3':
    a = readfirstnumber(choice)
    b = readsecondnumber(choice)
    mul(a,b)

if choice =='4':
    a = readfirstnumber(choice)
    b = readsecondnumber(choice)
    div(a,b)
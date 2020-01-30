class Calc:
    def __init__(self,Num1,Num2):
        self.a=Num1
        self.b=Num2
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
j=int(input("First Number: "))
k=int(input("second Number: "))
choice=1
print("1: add\n2: Sub\n3: Mul\n4: div\n0: exit")
choice=int(input("Enter the choice: "))
calci=Calc(j,k)
while choice!=0:
    if choice==1:
       print(calci.add())
       exit()
    elif choice==2:
       print(calci.sub())
       exit()
    elif choice==3:
       print(calci.mul())
       exit()
    elif choice==4:
       print(calci.div())
       exit()
    elif choice==0:
       exit("Exiting")
    else:
        print("Invalid Choice: TRY AGAIN")
        print("1: add\n2: Sub\n3: Mul\n4: div\n0: exit")
        choice=int(input("Enter the choice: "))

        


class Calculator:

    def choice(self):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        ch = input("Enter choice(1/2/3/4): ")

        if ch =='1':
            a = self.readfirstnumber()
            b = self.readsecondnumber()
            self.sum(a,b)

        if ch =='2':
            a = self.readfirstnumber()
            b = self.readsecondnumber()
            self.sub(a,b)

        if ch =='3':
            a = self.readfirstnumber()
            b = self.readsecondnumber()
            self.mul(a,b)

        if ch =='4':
            a = self.readfirstnumber()
            b = self.readsecondnumber()
            self.div(a,b)


    def readfirstnumber(self):
        print("Enter the 1st number ")
        a = input()
        return a

    def readsecondnumber(self):
        print("Enter the 2nd number")
        b = input()
        return b

    def sum(self,a,b):
        c = int(a)+int(b)
        print("Addition of "+a+" and "+b+" is "+str(c))
    
    def sub(self,a,b):
        c = int(a)-int(b)
        print("Subtration "+a+" and "+b+" is "+str(c))

    def mul(self, a,b):
        c = int(a)*int(b)
        print("multiplication "+a+" and "+b+"  is "+str(c))

    def div(self,a,b):
        c = int(a)/int(b)
        print("division is "+a+" and "+b+" is " +str(c))


def hello():
    print('Hello')

hello()
cal = Calculator()
cal.choice()

    









    


    

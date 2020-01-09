class Employee:
    def __init__(self,Identity,Fullname):
        self.id= Identity
        self.name=Fullname
    def display(self):
        print("Id is "+str(self.id)+"\nName is "+self.name)
    

e1=Employee(1,'chethan')
e1.display()
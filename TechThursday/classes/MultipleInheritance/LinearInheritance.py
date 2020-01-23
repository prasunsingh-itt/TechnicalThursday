class Base1:
    def printnow(self):
        print("Base1") 

class Base2:
    def printnow(self):
        print("Base2") 

class MultiDerived(Base1, Base2):
    pass





#Diamond Problem
#https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Diamond_inheritance.svg/220px-Diamond_inheritance.svg.png


m = MultiDerived()
m.printnow()





#print(MultiDerived.__mro__)


# #Super class is object 


# print(issubclass(list,object))


# print(isinstance(5.5,object))


# print(isinstance("Hello",object))
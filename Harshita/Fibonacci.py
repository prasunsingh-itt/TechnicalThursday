occurence =input()
a=input()
b=input()

for i in range(int(occurence)):
    c=int(a)+int(b)
    print(c)
    a=b
    b=c    
    

r=input("Range: ")
st="Amstrong numbers below "+r+" are:"
for Num in range(int(r)):
    a=Num
    c=0
    for i in range(len(str(Num))):
        b= int(a) % 10
        a=int(a)/10
        c=c+(b*b*b)
    if Num==c:
        st=st+" "+str(c)
print(st)
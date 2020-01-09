b=input("Enter the amount: ")
a=[2000,500,200,100]
if (int(b)%100)==0:
    for i in a:
        print(str(int(b)//i) +" Notes of "+str(i))
        b=int(b)%i
else:
    print("Enter amount in multiples of 100s,200s,500s or 2000")
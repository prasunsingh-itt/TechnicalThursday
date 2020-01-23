a=input()
b="a Palindrome"
for i in range(len(a)):
    if(a[i]!=a[(len(a)-1)-i]):
        b="not a Palindrome"
print(a+" is "+b)
__doc__
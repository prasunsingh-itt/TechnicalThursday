print("Enter the first number")
a=input();
print("Enter the second number")
b=input();
print("Enter the range")
fiborange=input()
print(a)
print(b)
for i in range(int(fiborange)):
  sum=int(a)+int(b)
  print(sum)  
  a=b
  b=sum
  

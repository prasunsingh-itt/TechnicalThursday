n=input("Enter the N value: ")
n = int(n)
total_sum = 0
odd_sum = 0
even_sum = 0
for i in range(n+1):
    total_sum = total_sum + i
    if(i % 2 == 0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print ("Total Sum : " + str(total_sum))
print ("Even Sum : " + str(even_sum))
print ("Odd Sum : " + str(odd_sum))


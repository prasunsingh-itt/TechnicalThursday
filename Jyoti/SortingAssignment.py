#SORT FIRST HALF OF THE LIST IN ASCENDING AND SECOND HALF IN DESCENDING

ListOfNumbers=input("Enter List of numbers to be sorted: ")
list(ListOfNumbers)

length=len(ListOfNumbers)
int(length)

FirstHalfList=ListOfNumbers[0:int(length/2)]
SecondHalfList=ListOfNumbers[int(length/2):int(length)]

FirstHalfList=sorted(FirstHalfList)
SecondHalfList=sorted(SecondHalfList,reverse=True)
print(FirstHalfList)
print(SecondHalfList)


for number in SecondHalfList : 
     FirstHalfList.append(number)

print("The resultant list is: ")
print(FirstHalfList)

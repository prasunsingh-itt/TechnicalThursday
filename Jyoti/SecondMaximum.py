ListOfNumbers=input("Enter the list of numbers: ")
list(ListOfNumbers)

ListOfNumbers=sorted(ListOfNumbers,reverse=True)
print("Second maximum number in the list is: ")
print(ListOfNumbers[1])
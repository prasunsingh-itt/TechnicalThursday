def fibonnaci():
    occurance= input('Enter the occurence ')
    num1=input('Enter the number 1 ')
    num2=input('Enter the number 2 ')

    for i in range (int(occurance)):
        sum= int(num1)+int(num2)
        print(sum)
        num1=num2
        num2=sum


fibonnaci()
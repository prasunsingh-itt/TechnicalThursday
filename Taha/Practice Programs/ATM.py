amount = input('Enter the amount to be withdrawn : ')

if(int(amount) % 100 != 0):
    print('Please Enter the amount in multiples 100s')
else:
    print("No of 2000 notes :" +str(int(amount)//2000))
    amount = int(amount) - int(amount)//2000*2000
    print("No of 500 notes :" +str(int(amount)//500))
    amount =int(amount) - int(amount)//500*500
    print("No of 200 notes :" +str(int(amount)//200))
    amount = int(amount) - int(amount)//200*200
    print("No of 100 notes :" +str(int(amount)//100))
    amount = int(amount) - int(amount)//100*100
    
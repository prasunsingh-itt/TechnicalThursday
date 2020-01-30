seat_number = input("Enter the Seat Number: ")
seat_number = int(seat_number)
if(seat_number>54):
    print("Invalid Seat number")
elif(seat_number%6 == 0 and seat_number%2==0):
    print("Breth is Side Upper Berth ")
elif(seat_number%6!=0 and seat_number%2==0):
    print("Berth is Upper berth")
elif(seat_number%6==5):
    print("berth is Side Lower Berth")
else:
    print("Berth is Lower Berth")
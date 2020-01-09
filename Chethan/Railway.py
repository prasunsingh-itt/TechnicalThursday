Seat=input("Enter The seat Number:")
if int(Seat)%6==0:
    print("Side Upper Berth (Dark Green)")
elif (int(Seat)+1)%6==0:
    print("Side Lower Berth (Light Green)")
elif (int(Seat)%6!=0 and int(Seat)%2==0):
    print("Upper Berth (Light Blue)")
else:
    print("Lower Berth (Yellow)")
from Duke import Duke
from Bullet import Bullet


def yourBike():
    typeOfBike = input("Select Bike: ")
    while typeOfBike != "D" and typeOfBike != "B":
        print("D. Duke B. bullet :")
        print("Wrong option seleced")
        typeOfBike = input("Select Bike: ")
    bike = None
    if typeOfBike == "D":
        bike = Duke(200, 5)
    else:
        bike = Bullet(250, 6)
    return bike

bike = yourBike()
action = {  "1": bike.start,
            "2": bike.gearUpShift,
            "3": bike.gearDownShift,
            "4": bike.stop
         }
bikeOp = ''
while bikeOp != None:
    bikeOp = input(
        """Choose you Action 1.Start Bike 2. Gear Up  3. Gear Down 4. Stop Bike:""")
    bikeAction = action.get(bikeOp, None)
    if bikeAction is None:
        bikeOp = None
    else:
        bikeAction()
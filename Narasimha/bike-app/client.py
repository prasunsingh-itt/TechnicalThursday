from yamaha import Yamaha
from kawasaki import Kawasaki
from person import Person


def selectBike():
    print("Available bikes for ride are \n 1. Yamaha 2. Kawasaki :")
    bikeType = input("Please choose bike for riding: ")
    while bikeType != "1" and bikeType != "2":
        print("Available bikes for ride are \n 1. Yamaha 2. Kawasaki :")
        print("You have selected invalid option...!!")
        bikeType = input("Please choose bike for riding: ")
    bike = None
    if bikeType == "1":
        bike = Yamaha(100, 5)
    else:
        bike = Kawasaki(150, 6)
    return bike


def readRiderName():
    name = input("Please enter rider name: ")
    person = Person(name)
    print("Hello ", person.getName(), "!!!")


readRiderName()
bike = selectBike()
switcher = {"1": bike.start, "2": bike.gearUp,
            "3": bike.gearDown, "4": bike.stop}
option = ''
while option != None:
    option = input(
        """Select operation 1. Start Engine 2. Gear Up  3. Gear Down 4. Stop Engine 5. Exit :""")
    operation = switcher.get(option, None)
    if operation is None:
        option = None
    else:
        operation()

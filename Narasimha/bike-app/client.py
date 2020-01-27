from yamaha import Yamaha
from kawasaki import Kawasaki
from person import Person

name = input("Please enter rider name: ")
person = Person(name)
print("Hello ", person.getName(), "!!!")
print("Available bikes for ride are \n 1. Yamaha 2. Kawasaki")
bikeType = input("Please choose bike for riding: ")

while int(bikeType) != 1 and int(bikeType) != 2:
    print("You have selected invalid option...!!")
    bikeType = input("Please choose bike for riding: ")

bike = None
if int(bikeType) == 1:
    bike = Yamaha(100, 5)
else:
    bike = Kawasaki(150, 6)

bike.start()
while bike.getGearPosition() < bike.getNoOfGears():
    bike.gearUp()
bike.gearUp()

while bike.getGearPosition() != 0:
    bike.gearDown()
bike.gearDown()

bike.stop()

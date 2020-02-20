from person import Person
from bike import Bike
from duke import Duke
from aprilla import Aprilla

class Rider:
    def __init__(self):
        pass

    name = input("Enter the name of the rider: ")
    a = Person(name)
    bikename = input("Enter the bike \n 1. Duke\n 2.Aprilla : ")
    if (bikename == '1'):
        bikeride = Duke()
    elif (bikename== '2'):
        bikeride = Aprilla()
    
    action = '0'
    
    while (action < '4'):
        action = input("Enter the action to be performed:\n1.Start Bike \n2.Gear Up \n3.Gear Down\n4.Stop \n")
        if (action == '1'):
            bikeride.start()
        elif(action == '2'):
            bikeride.speedup()
        elif(action == '3'):
            bikeride.speeddown()
        else:
            bikeride.stop()

rider = Rider()
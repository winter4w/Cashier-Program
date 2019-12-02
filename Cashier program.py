
import os
import time
import sys
import math

class Cashier():
    def getDollars(self, a):
        dol = int(math.floor(a))
        return dol

    def getQuarters(self, a):
        qua = int(math.floor(a / .25))
        return qua

    def getDimes(self, a):
        dim = int(math.floor(a / .10))
        return dim

    def getNickels(self, a):
        nic = int(math.floor(a / .05))
        return nic
    
    def getPennies(self, a):
        pen = int(a / .01 +.1)
        return pen

    def newChange(self, a, coin_value , numberofcoins):
        return a - coin_value * numberofcoins

myChange = Cashier()

while True:
    print("")
    
    print("Enter the amount due in dollars and cents: ")

    amountDue = float(raw_input("$"))

    print("")

    amountReceived = float(raw_input("Enter the amount received: $"))

    print("")
    
    change = amountReceived - amountDue

    if amountDue > amountReceived:
        print("The customer has payed less than the cost")

    else:
        dolSolve  = myChange.getDollars(change)
        change = myChange.newChange(change, 1, dolSolve)
        
        quaSolve = myChange.getQuarters(change)
        change = myChange.newChange(change, .25, quaSolve)
        
        dimSolve = myChange.getDimes(change)
        change = myChange.newChange(change, .10, dimSolve)
        
        nicSolve = myChange.getNickels(change)
        change = myChange.newChange(change, .05, nicSolve)
        
        penSolve = myChange.getPennies(change)
        


        print("Give the customer")
        print(str(dolSolve) + " Dollars")
        print(str(quaSolve) + " Quarters")
        print(str(dimSolve) + " Dimes")
        print(str(nicSolve) + " Nickels")
        print(str(penSolve) + " Pennies")

        print("")


    choiceQuit = raw_input ("If you will like to quit this program type 'quit' otherwise press enter:")
    os.system('cls')

    if choiceQuit == "quit":     
        break
    else:           
        True
        
os.system('cls')
print("The Program is now closeing!")
print ("5")
time.sleep(1)
os.system('cls')
print("The Program is now closeing!")
print ("4")
time.sleep(1)
os.system('cls')
print("The Program is now closeing!")
print ("3")
time.sleep(1)
os.system('cls')
print("The Program is now closeing!")
print ("2")
time.sleep(1)
os.system('cls')
print("The Program is now closeing!")
print ("1")
sys.exit()

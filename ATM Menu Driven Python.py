import random 
import sys
switchCase = 0
wish = 0
balance = 0
pin = 0
number = 0

class atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def cashWithdrawl(self):
        self.cardnumber = int(input("Enter your Card Number:  "))
        self.pin = int(input("Enter your PIN:  "))
        self.pin = pin
        self.cardnumber = number
        balance = (random.randint(100000, 150000))
        switchCase = (random.randint(1,5))
        print("The amount of balance you have in your card is: " , balance)
        print("If You want to check your purchase history enter 3")
        print("To get Free Prize enter 9 ")
        wish = int(input("Enter 3 or 9 on the basis of what you want to VISIT:  "))
        if(switchCase == 1):
            if(wish == 3):
                print("Bought BAJAJ AIR CONDITIONER ₹45,000")
                print("Bought Double-door Refrigerator ₹30,000 ")
                print("Bought PEACE ₹ ∞")
            elif(wish == 9):
                print("BRUUH, does not grow on trees.... Just for JOKE")
                print()
                print()
                print()
                sys.exit()

        if(switchCase == 2):
            if(wish == 3):
                print("Bought LV-Bag ₹63,000 ")
                print("Bought Cap ₹1500 ")
                print("Bought PEACE ₹ ∞")
            elif(wish == 9):
                print("BRUUH, does not grow on trees.... Just for JOKE")
                print()
                print()
                print()
                sys.exit()

        if(switchCase == 3):
            if(wish == 3):
                print("Bought AMD-Ryzen Processor ₹36,000")
                print("Bought Double-door Refrigerator ₹30,000 ")
                print("Bought PEACE ₹ ∞")
            elif(wish == 9):
                print("BRUUH, does not grow on trees.... Just for JOKE")
                print()
                print()
                print()
                sys.exit()
            
        if(switchCase == 4):
            if(wish == 3):
                print("Bought SAMSUNG AIR CONDITIONER ₹45,000")
                print("Bought iPhone12MaxPro ₹102,000 ")
                print("Bought PEACE ₹ ∞")
            elif(wish == 9):
                print("BRUUH, does not grow on trees.... Just for JOKE")
                print()
                print()
                print()
                sys.exit()

        if(switchCase == 5):
            if(wish == 3):
                print("Bought classic Green Screen ₹6500")
                print("Bought Gaming Router ₹24,000 ")
                print("Bought PEACE ₹ ∞")
            elif(wish == 9):
                print("BRUUH, does not grow on trees.... Just for JOKE")
                print()
                print()
                print()
                sys.exit()


                    

            
            

       


atm1 = atm(balance, pin)
print(atm1.cashWithdrawl())



        
        
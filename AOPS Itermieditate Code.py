selfbankbal = 100
otherbankbal = 200
accountlist = ("a1","a2")
y = selfbankbal
ID = "123-456"
print ("Hello, here are some things you can do at AOPS bank")
print ("What would you like to do?: ")
print ("A: Inizatilze the account")
print ("B: Return Ammount")
print ("C: Deposit The Green Dough")
print ("D: Withdraw the Monies")
print ("E: Transfer Monies to another account")
print ("str: Print balance and ID.")
choice = input("What would you like to do?: ")
def Dep(selfbankbal,y):
    c3 = (int(input("How much would you like to deposit?: ")))
    selfbankbal = c3 + y
    print (selfbankbal)
    print ("Your new bank balance is",selfbankbal)

def With(selfbankbal,y):
    c4 = (int(input("How much would you like to withdraw?: ")))
    selfbankbal = selfbankbal - c4
    print (selfbankbal)
    print ("Your new bank balance is",selfbankbal)
    
def transfer(a, b, c, selfbankbal):
    if c <= selfbankbal:
        selfbankbal = selfbankbal - c
        print ("Your account is now",selfbankbal,"dollars")
        print(c,"dollars have been transfered to",a)
    else:
        print("You don't have enough money to transfer the specifiyed account")

##while True:
if choice == "A" or choice == "a":
    c2 = input("Put in your ID number.")
    if c2 == "123-456":
        selfbankbal = 0
        print ("Your bank account balance has been set to 0.")
elif choice == "B" or choice == "b":
    selfbankbal = y
    if selfbankbal == 0:
        print ("Your bank balance has been restored.")
    else:
        print ("It doesn't need to be restored.")
elif choice == "C" or choice == "c":
    Dep(selfbankbal, y)
elif choice == "D" or choice == "d":
    With(selfbankbal, y)
elif choice == "E" or choice == "e":
    a = input("Enter the account your tranfering money too: ")
    b = input("Enter your account: ")
    c = int(input("Enter the amount your tranfering: "))
    if a in accountlist and b in accountlist:
        transfer(a, b, c, selfbankbal)
    else:
        print ("Valid account names have not been entered.")
elif choice == "str":
    print ("Your account ID is",ID,"and you have",selfbankbal,"dollars in your account")


##    func_dict = {'transfer':transfer}
##    func_dict[a]()

    
    
        


    
##        
##        
####        print ("Your account balance has been reset to 0.")
####        print ("Would you like to do anything else?")
####        print ("B: Return Ammount")
####        print ("C: Deposit The Green Dough")
####        print ("D: Withdraw the Monies")
####print ("E: Transfer Monies to another account")
####choice = input("What would you like to do?: ")



##    




    

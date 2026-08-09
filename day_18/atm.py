balance = 10000

user = input("Enter your name : ")
print(f"WELCOME {user}.")

while True :
    print("CHOOSE ONE OPTION:")
    print("1. WITHDRAW THE AMOUNT")
    print("2. DIPOSIT THE AMOUNT")
    print("3. BALANCE  AMOUNT")
    print("4. EXIT")
    choice = int(input("Enter your choice:"))


    if(choice == 1):
        amount = int(input("ENTER HOW MUCH AMOUNT TO WITHDRAW: "))
        if(amount <= balance):
            balance -= amount
            print("WITHDRAW SUCCESFUL.")
        else :
            print("THE ENTER AMOUNT IS NOT AVAILABLE.")
    elif(choice == 2):
        deposit = int(input("ENTER HOW MUCH AMOUNT TO DEPOSIT: "))
        balance += deposit
    elif(choice == 3):
        print(f"YOUR BALANCE {balance}.")
    elif(choice == 4):
        print("THANK YOU")
        break
    else:
        print("INVALID OPTION CHOOSE CORRECT ONE")
            
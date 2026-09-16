class InsufficientBalanceError(Exception):
    pass


balance = 5000

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            balance += amount
            print("Deposit Successful.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            if amount > balance:
                raise InsufficientBalanceError("Insufficient balance")

            balance -= amount
            print("Withdrawal Successful.")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            raise ValueError("Invalid menu choice")

    except ValueError as e:
        print("Input Error:", e)

    except InsufficientBalanceError as e:
        print("Transaction Error:", e)

    else:
        print("Transaction completed successfully.")

    finally:
        print("ATM operation completed.")
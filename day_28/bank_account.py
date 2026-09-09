class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdraw Successful.")
        else:
            print("Insufficient balance.")
    def chekbalance(self):
        print(f"Your Balance is {self.balance}.")


account = BankAccount("sai", 2000)
account.deposit(200)
account.withdraw(200)
account.chekbalance()

print("Name : ",account.name)
print("Balance : ",account.balance)

        

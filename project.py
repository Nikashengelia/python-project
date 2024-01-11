class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal unsuccessful.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def get_balance(self):
        print(f"Current balance for {self.owner_name}: ${self.balance}")



if __name__ == "__main__":
    account1 = BankAccount("John Doe", initial_balance=1000)

    account1.deposit(500)


    account1.withdraw(200)

    account1.withdraw(1500)


    account1.get_balance()
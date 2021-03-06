import random
class BankAccount:
    routing_number = 121042882
    balance = 0

    def __init__(self, name, balance):
        self.account = random.randint(000000000, 999999999)
        self.name = name
        self.balance = balance

    def get_balance(self):
        print(f"Balance: ${self.balance}")

    def print_receipt(self):
        hidden_account = str(self.account)
        last_char = hidden_account[-4:]
        print(f"{self.name}")
        print(f"Account No.: XXXX{last_char}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: ${self.balance}")

    def deposit(self, amount):
        new_balance = amount + self.balance
        print(f"Amount Deposited: ${amount}")
        print(f"New Balance: ${new_balance}")

    def add_interest(self, balance):
        interest = self.balance *  0.00083

    def withdrawl(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds")
            self.balance -= 10
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
            print(f"New Balance: ${self.balance}")
#Users
jordan = BankAccount("Jordan Torres", 1200)
jacob = BankAccount("Jacob Abrahams", 4000)
brittany = BankAccount("Brittany Gilmore", 10000)

jordan.withdrawl(3000)
brittany.deposit(10)
jacob.print_receipt()
jordan.print_receipt()

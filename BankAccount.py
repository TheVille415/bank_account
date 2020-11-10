class BankAccount:
    def __init__(self, name, account, routing, balance):
        self._name = name
        self._account = account
        self._routing = routing
        self._balance = balance

    def full_name(self):
        print(f"{self._name}")

    def account_number(self):
        print(f"Account No.: {self._account}")

    def routing_number(self):
        print(f"Routing No.: {self._routing}")

    def balance(self):
        print(f"Balance: ${self._balance}")

    def print_receipt(self):
        print(f"{self._name}")
        print(f"Account No.: {self._account}")
        print(f"Routing No.: {self._routing}")
        print(f"Balance: ${self._balance}")

    def deposit(self, amount):
        new_balance = amount + self._balance
        print(f"Amount Deposited: ${amount}")
        print(f"New Balance: ${new_balance}")

    def add_interest(self, balance):
        interest = self._balance *  0.00083

    def withdrawl(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds")
        elif amount <= self._balance:
            withdrawl_ammount = self._balance - amount
            print(f"Amount Withdrawn: ${amount}")
            print(f"New Balance: ${withdrawl_ammount}")

jordan = BankAccount("Jordan Torres", 12345678, 123456789, 1200)

jacob = BankAccount("Jacob Abrahams", 98765432, 192837465, 4000)

brittany = BankAccount("Brittany Gilmore", 13579246, 246809753, 10000)

jordan.deposit(100)

jacob.withdrawl(3000)

brittany.print_receipt()


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

    def deposit(self, amount):
        new_balance = amount + balance
        print(f"Amount Deposited: ${new_balance}")

    def add_interest(self, balance):
        interest = balance *  0.00083
        new_balance = interest + balance
    
    def print_receipt(self):
        print(f"{self._name}")
        print(f"Account No.: {self._account}")
        print(f"Routing No.: {self._routing}")
        print(f"Balance: ${self._balance}")




jordan = BankAccount("Jordan", 12345678, 123456789, 1200)
jordan.account_number()
jordan.deposit(100)
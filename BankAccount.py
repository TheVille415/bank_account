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
        print(f"Balance: {self._balance}")
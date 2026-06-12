# Base Class
class Account:
    def __init__(self, name, balance):
        self._name = name          # Protected attribute
        self.__balance = balance   # Private attribute

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0")

    # Helper method for subclasses
    def _update_balance(self, amount):
        self.__balance += amount


# Subclass 1
class DigitalWallet(Account):
    def __init__(self, name, balance, transaction_limit):
        super().__init__(name, balance)
        self.__transaction_limit = transaction_limit

    def set_transaction_limit(self, limit):
        self.__transaction_limit = limit

    def get_transaction_limit(self):
        return self.__transaction_limit

    def send_money(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__transaction_limit:
            print("Transaction exceeds limit")
        elif amount > self.get_balance():
            print("Insufficient balance")
        else:
            self._update_balance(-amount)
            print(f"Sent {amount} successfully")


# Subclass 2
class SavingsAccount(Account):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self._interest = interest  # Protected attribute

    def set_interest(self, interest):
        self._interest = interest

    def get_interest(self):
        return self._interest

    def get_balance(self):
        return super().get_balance()


# Testing
wallet = DigitalWallet("Collins", 5000, 2000)

print("Name:", wallet.get_name())
print("Balance:", wallet.get_balance())

wallet.deposit(1000)
wallet.send_money(1500)

print("New Balance:", wallet.get_balance())

print("-" * 30)

savings = SavingsAccount("Frank", 10000, 5)

print("Name:", savings.get_name())
print("Balance:", savings.get_balance())
print("Interest:", savings.get_interest())

savings.set_interest(8)
print("Updated Interest:", savings.get_interest())

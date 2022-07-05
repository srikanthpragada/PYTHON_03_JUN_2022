class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Available balance is {self.balance}, but withdraw amount is {self.amount}"

class Account:
    # class attribute or static variable
    minbal = 10000

    @staticmethod
    def getminbal():
        return Account.minbal

    # Method
    def __init__(self, acno, ahname):
        # Object attribute
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceError(self.balance, amount)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid Amount. It cannot be zero or negative")

        self.balance += amount

    def getbalance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno


print(Account.getminbal())
a1 = Account(1, "Roberts")  # Object
a1.deposit(10000)
a1.deposit(20000)
print(a1.getbalance())
print(a1)  # a1.__str__()

a2 = Account(2, "Larry")
a2.deposit(100000)

try:
    a2.withdraw(200000)
except InsufficientBalanceError as ex:
    print(ex)

print(a2)

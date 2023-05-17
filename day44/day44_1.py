from decimal import Decimal
class Account():
    
    def __init__(self, name: str, balance: Decimal):
        if balance < Decimal(0):
            raise ValueError('Initial balance must be positive!')
        self.name = name
        self.balance = balance
        
    def deposite(self, amount):
        if amount < Decimal(0):
            raise ValueError('Initial balance must be positive!')
        self.balance += amount
        
acc = Account("Barak", -2000)

print(acc.balance)
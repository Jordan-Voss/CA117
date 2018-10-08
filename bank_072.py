class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = float(balance)

    def __str__(self):
        return ('Your current balance is: {:.2f} euro'.format(self.balance))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds available')
        else:
            self.balance -= amount
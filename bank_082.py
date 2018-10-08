class BankAccount:
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance

        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance *= 1 + BankAccount.interest_rate

    def __iadd__(self, amount):
        self.lodge(amount)
        return self

    def __str__(self):
        return "Name: {} {}\nAccount number: {}\nBalance: {:.2f}".format(
            self.forename, self.surname, self.account_number, self.balance)

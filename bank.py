#!/usr/bin/env python3


class BankAccount:
    """
    Returns account information and allows deposites and withdrawls.
    """

    def __init__(self):
        """
        initializes the account balance to 0.
        """
        self.account_balance = 0
        self.amount = 0

    def getAmountFromConsole(self, action):
        amount = input("Please Enter a %s Amount: " % action)
        if not amount:
            raise ValueError("Amount cannot be empty.")
        if not isinstance(int(amount), int):
            raise TypeError("Please use integers only")
        self.amount = amount

    def deposite(self):
        self.account_balance += int(self.amount)

    def withdraw(self):
        self.account_balance -= int(self.amount)

    def balance(self):
        print("Current Balance: %s" % self.account_balance)

    def go_on(self):
        value = input("Would you like to make another transaction? ")
        value = value.lower().rstrip()
        if not value:
            raise ValueError("Value cannot be empty. Please use yes or no.")
        if value == "yes" or value == "y":
            return transaction(self)
        else:
            print("Transaction complete")
            return


def transaction(bank):
    action = input("What would you like to do? ")
    if not action:
        raise ValueError("Value cannot be empty. Please respond with either deposite or withdraw")
    if not isinstance(action, str):
        raise TypeError("Please respond with either deposite or withdraw")
    if action == "deposite":
        bank.getAmountFromConsole(action)
        bank.deposite()
        bank.balance()
        bank.go_on()
    if action == "withdraw":
        bank.getAmountFromConsole(action)
        bank.withdraw()
        bank.balance()
        bank.go_on()


def main():
    bank = BankAccount()
    transaction(bank)


if __name__ == '__main__':
    main()

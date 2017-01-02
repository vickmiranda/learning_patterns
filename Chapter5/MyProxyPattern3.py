from abc import ABCMeta, abstractmethod
from collections import OrderedDict


class Customer(object):
    def __init__(self, account):
        print 'init proxy server'
        self.account = account
        self.atm = Atm()

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass

    def deposit(self):
        pass


class Firewall(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print 'Start secure link\n'

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


# This is the object not seeing by customer
class Bank(Firewall):

    def __init__(self):
        self.account = None
        self.register = OrderedDict

    def add_account(self, account, initial_deposit):
        self.register[account] = initial_deposit

    def enter_account(self, account):
        self.account = account

    def withdraw(self, amount):
        balance = self.check_balance()
        if amount > balance:
            print 'not enough money! current balance {}'.format(balance)
        else:
            balance = balance - amount
            print 'New balance is {}'.format(balance)
        return balance

    def deposit(self, amount):
        balance = self.check_balance()
        balance = balance + amount
        print 'new balance is {}'.format(balance)

    def check_balance(self, account):
        if account in self.register:
            print 'valid account found'
            return self


# This is my proxy class
class Atm(Firewall):
    def __init__(self):
        print 'initializing transaction with main object'
        self.bank = Bank()
        self.account = 0

    def enter_info(self, account):
        self.account = account

    def withdraw(self, amount):
        pass

    def check_balance(self):
        return self.bank.check_balance(self.account)

    def deposit(self, amount):
        self.bank.deposit(amount)


if __name__ == '__main__':
    print 'starting'
    customer = Customer(123)

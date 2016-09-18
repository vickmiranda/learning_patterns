from abc import ABCMeta, abstractmethod


# This is the user/customer of the proxy
class Customer(object):
    def __init__(self):
        print ('Let\'s buy this beautiful bike!\n')
        self.debit_card = DebitCard()

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("You:: Wow! the cevelo bike is mine :-)")
        else:
            print("You:: I should earn more :(")


# this is the proxy abstract which is used to talk to the real object
class Payment(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print 'Starting payment transaction\n'

    @abstractmethod
    def do_pay(self):
        pass


# this is the object that has sensitive information
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def _get_account(self):
        self.account = self.card
        return self.account

    def set_card(self, card):
        self.card = card

    def _has_funds(self):
        print('Bank: checking if account {} '
              'has funds'.format(self._get_account()))
        return False

    def do_pay(self):
        if self._has_funds():
            print ('Bank: paying the merchant\n')
            return True
        else:
            print ('Bank: Sorry not enough funds\n')
            return False


# This is the proxy class that do most of the interface with the customer
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy: "Enter the card number: "')
        self.bank.set_card(card)
        return self.bank.do_pay()

# usage
if __name__ == '__main__':
    vick = Customer()
    vick.make_payment()

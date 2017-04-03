from abc import ABCMeta, abstractmethod
# Facade


class Expense(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def pay(self):
    pass

  @abstractmethod
  def use(self):
    pass

# Sub-system1
class Utility(Expense):
  def __init__(self):
    print 'init utility'

  def pay(self):
    print 'pay utility'

  def use(self):
    print 'using utility'


# Sub-system2
class Rent(Expense):
  def __init__(self):
    print 'init rent'

  def pay(self):
    print 'paying rent'

  def use(self):
    print 'using house'


# Sub-system3
class College(Expense):
  def __init__(self):
    print 'init college'

  def pay(self):
    print 'pay college'

  def use(self):
    print 'going to college'


# Client
class MrMad(object):
  def __init__(self):
    self.exp1 = Utility()
    self.exp2 = Rent()
    self.exp3 = College()

  def make_payments(self):
    self.exp1.pay()
    self.exp2.pay()
    self.exp3.pay()

  def usage(self):
    self.exp1.use()
    self.exp2.use()
    self.exp3.use()


# Usage
if __name__ == '__main__':
  person = MrMad()
  print
  person.make_payments()
  print
  person.usage()
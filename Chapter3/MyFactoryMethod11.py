from abc import ABCMeta
from abc import abstractmethod


class Breakfast(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def prepare(self):
    pass

  @abstractmethod
  def cook(self):
    pass

  @abstractmethod
  def enjoy(self):
    pass



class MakeEggs(Breakfast):
  def prepare(self):
    print 'preparing eggs'

  def cook(self):
    print 'sunny side up'

  def enjoy(self):
    print 'yummy eggs'



class Pankake(Breakfast):
  def prepare(self):
    print 'preparing pankakes'

  def cook(self):
    print 'pankakes in the pan'

  def enjoy(self):
    print 'yummy pankakes'



class Chicharrones(Breakfast):
  def prepare(self):
    print 'buy chicharron'

  def cook(self):
    print 'prepare tortillas for chicharrones'

  def enjoy(self):
    print 'yummy chicharrones'



class CreateBreakfast(object):
  def __init__(self):
    self.items = []
    self.create_breakfast()

  @abstractmethod
  def create_breakfast(self):
    pass

  def get_items(self):
    return self.items

  def prepare_all(self):
    for i in self.items:
      i().prepare()

  def cook_all(self):
    for i in self.items:
      i().cook()

  def enjoy_all(self):
    for i in self.items:
      i().enjoy()

  def put_items(self, value):
    self.items.append(value)


class Continental(CreateBreakfast):
  def create_breakfast(self):
    self.items.append(MakeEggs)
    self.items.append(Pankake)


class MexicanBreakfast(CreateBreakfast):
  def create_breakfast(self):
    self.items.append(Chicharrones)


class CompleteBreakfast(CreateBreakfast):
  def create_breakfast(self):
    self.items.append(MakeEggs)
    self.items.append(Pankake)
    self.items.append(Chicharrones)


if __name__ == '__main__':
    continental = Continental()
    continental.prepare_all()
    print
    continental.cook_all()
    print
    continental.enjoy_all()
    print
    mexican = MexicanBreakfast()
    mexican.cook_all()
    print
    mexican.enjoy_all()


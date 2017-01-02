from abc import ABCMeta, abstractmethod
import random


class MakeMeal(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def prepare(self):
    pass

  @abstractmethod
  def cook(self):
    pass

  @abstractmethod
  def eat(self):
    pass

  # this acts as a hook and is not always called
  def share_meal(self):
    print 'sharing meal with community'

  def do_all(self):
    self.prepare()
    self.cook()
    self.eat()


class MakePizza(MakeMeal):

  def prepare(self):
    print 'prep pizza'

  def cook(self):
    print 'cook pizza'

  def eat(self):
    print 'eat pizza'


class MakeMole(MakeMeal):

  def prepare(self):
    print 'prepare mole'

  def cook(self):
    print 'cook mole'

  def eat(self):
    print 'enjoy the mole'


make_pizza = MakePizza()
make_pizza.do_all()

plenty_food = random.choice(['yes', 'no'])
if plenty_food == 'yes':
  make_pizza.share_meal()



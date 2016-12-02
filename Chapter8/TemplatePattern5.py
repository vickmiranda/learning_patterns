from abc import ABCMeta, abstractmethod

class MakeCoffe(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def SelectGrain(self):
    pass

  @abstractmethod
  def PrepareLiquid(self):
    pass

  @abstractmethod
  def PrepareCoffe(self):
    pass

  @abstractmethod
  def MixIngridients(self):
    pass

  def Enjoy(self):
    self.SelectGrain()
    self.PrepareLiquid()
    self.PrepareCoffe()
    self.MixIngridients()


class MakeCappuccino(MakeCoffe):
  def SelectGrain(self):
    print 'grain for capuchino'

  def PrepareLiquid(self):
    print 'Add milk'

  def PrepareCoffe(self):
    print 'Heat milk and pour '

  def MixIngridients(self):
    print 'Now mix with cinnamon'


class MakeLatte(MakeCoffe):
  def SelectGrain(self):
    print 'grain for latte'

  def PrepareLiquid(self):
    print 'Add mild and water'

  def PrepareCoffe(self):
    print 'Heat to 150 F '

  def MixIngridients(self):
    print 'Add hazelnut liquid'


import random

caffe1 = MakeCappuccino()
caffe2 = MakeLatte()

select_coffe = random.choice([caffe1, caffe2])

select_coffe.Enjoy()



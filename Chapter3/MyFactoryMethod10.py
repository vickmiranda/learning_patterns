from abc import ABCMeta, abstractmethod


class Transportation(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def rent_transportation(self):
    pass

  @abstractmethod
  def use_transport(self):
    pass


class Car(Transportation):
  def rent_transportation(self):
    print 'renting car'

  def use_transport(self):
    print 'car transport use'


class Truck(Transportation):
  def rent_transportation(self):
    print 'renting truck'

  def use_transport(self):
    print 'muddy truck'


class Horse(Transportation):
  def rent_transportation(self):
    print 'cool horse power'

  def use_transport(self):
    print 'ahoo silver'


class Bike(Transportation):
  def rent_transportation(self):
    print 'chip transport 10 dls'

  def use_transport(self):
    print 'not bad bike is fine'


class ArrangeTransportation(object):
  __metaclass__ = ABCMeta
  def __init__(self):
    self.transports = []
    self.build_trasportation()

  def build_trasportation(self):
    pass

  def get_transport(self):
      return self.transports

  def add_transport(self, value):
    self.transports.append(value)


class SlowTransport(ArrangeTransportation):
  def build_trasportation(self):
    self.add_transport(Bike)
    self.add_transport(Horse)


class LoadTransport(ArrangeTransportation):
  def build_trasportation(self):
    self.add_transport(Truck)


class SpeedyTransport(ArrangeTransportation):
  def build_trasportation(self):
    self.add_transport(Car)



if __name__ == '__main__':
    slow = SlowTransport()
    for i in range(len(slow.transports)):
      slow.transports[i]().rent_transportation()






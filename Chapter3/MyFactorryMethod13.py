from abc import ABCMeta
from abc import abstractmethod


# Interface
class Instrument(object):
  __metaclass__ = ABCMeta
  @abstractmethod
  def configure(self):
    pass

  @abstractmethod
  def setup(self):
    pass

  @abstractmethod
  def measure(self):
    pass

  @abstractmethod
  def cleanup(self):
    pass

# Concrete interface
class Multimeter(Instrument):
  def configure(self):
    print 'configure multimeter'

  def setup(self):
    print 'setup multimeter'

  def measure(self):
    print 'measuring with multimeter'

  def cleanup(self):
    print 'exit from multimeter'


class Scope(Instrument):
  def configure(self):
    print 'configure scope'

  def setup(self):
    print 'setup scope'

  def measure(self):
    print 'measuring with scope'

  def cleanup(self):
    print 'exit from scope'


class DaqBoard(Instrument):
  def configure(self):
    print 'configure daq'

  def setup(self):
    print 'setup daq'

  def measure(self):
    print 'measuring with daq'

  def cleanup(self):
    print 'exit from daq'


# creator
class BaseStation(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.instruments = []
    self.create_station()

  @abstractmethod
  def create_station(self):
    pass

  def get_instruments(self):
    return self.instruments

  def add_instruments(self, value):
    self.instruments.append(value)

  def get_instrument(self, index):
    return self.instruments[index]


# concrete creator
class StationOne(BaseStation):
  def create_station(self):
    self.add_instruments(Multimeter)
    self.add_instruments(Scope)

  # def configure(self):
  #   lambda x: x().configure, self.instruments


class StationTwo(BaseStation):
  def create_station(self):
    self.add_instruments(Multimeter)
    self.add_instruments(DaqBoard)

# usage
if __name__ == '__main__':
    station = StationOne()
    for i in range(len(station.instruments)):
      station.instruments[i]().setup()
      station.instruments[i]().measure()

from abc import ABCMeta, abstractmethod

# Interface
class BaseInstrument(object):
  __metaclass__ = ABCMeta
  @abstractmethod
  def setup(self):
    pass

  @abstractmethod
  def configure(self):
    pass

  @abstractmethod
  def cleanup(self):
    pass

# Concrete interface
class DMM(BaseInstrument):
  def setup(self):
    print 'setup DMM'

  def configure(self):
    print 'configure DMM'

  def cleanup(self):
    print 'cleanup DMM'


class Scope(BaseInstrument):
  def setup(self):
    print 'setup Scope'

  def configure(self):
    print 'config Scope'

  def cleanup(self):
    print 'cleanup Scope'


class Daq(BaseInstrument):
  def setup(self):
    print 'setup Daq'

  def configure(self):
    print 'config Daq'

  def cleanup(self):
    print 'cleanup Daq'


# creator
class BaseClassStation(object):
  def __init__(self):
    self.instruments = []
    self.add_instrument()

  @abstractmethod
  def add_instrument(self):
    pass

  def get_instrument(self):
    return self.instruments

  def setup_all(self):
    for i in self.instruments:
      i().setup()

  def configure_all(self):
    for i in self.instruments:
      i().configure()

  def cleanup(self):
    for i in self.instruments:
      i().cleanup()

  def run_all(self):
    self.configure_all()
    self.setup_all()
    self.cleanup()


# concrete creator
class Station1(BaseClassStation):
  def add_instrument(self):
    self.instruments.append(DMM)
    self.instruments.append(Daq)


class Station2(BaseClassStation):
  def add_instrument(self):
    self.instruments.append(DMM)
    self.instruments.append(Scope)

# usage
if __name__ == '__main__':
    station1 = Station2()
    station1.run_all()
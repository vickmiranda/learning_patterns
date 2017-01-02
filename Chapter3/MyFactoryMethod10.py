from abc import ABCMeta, abstractmethod


# Product interface
class InstrumentClass(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def type_measurement(self):
    pass

  @abstractmethod
  def interface(self):
    pass


# Concrete product
class Voltmeter(InstrumentClass):
  def type_measurement(self):
    print 'analog voltmeter'

  def interface(self):
    print 'volt interface is gpib'


class Oscilloscope(InstrumentClass):
  def type_measurement(self):
    print 'digital scope'

  def interface(self):
    print 'gpib and ethernet'


class PowerSupply(InstrumentClass):
  def type_measurement(self):
    print 'power supply is analog'

  def interface(self):
    print 'no interface for power supply'


class DigitalSwitch(InstrumentClass):
  def type_measurement(self):
    print 'Switch is digital'

  def interface(self):
    print 'Usb interface for switch'


# create tester
class CreateTester(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.instruments = []
    self.create_tester()

  @abstractmethod
  def create_tester(self):
    pass

  def add_tester(self, instrument):
    self.instruments.append(instrument)

  def get_tester(self):
    return self.instruments


# create concrete testers
class HybridTester(CreateTester):
  def create_tester(self):
    self.add_tester(DigitalSwitch)
    self.add_tester(Voltmeter)
    self.add_tester(Oscilloscope)
    self.add_tester(PowerSupply)


class DigitalTester(CreateTester):
  def create_tester(self):
    self.add_tester(DigitalSwitch)
    self.add_tester(Oscilloscope)
    self.add_tester(Voltmeter)


if __name__ == '__main__':
  tester = HybridTester()
  for i in range(len(tester.instruments)):
    tester.instruments[i]().type_measurement()
    tester.instruments[i]().interface()
    print






from abc import ABCMeta, abstractmethod
device = {'PowerSupply': 0, 'Multimeter': 1, 'Oscilloscope': 2}


# Product interface
class DeviceDriver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def self_test(self):
        pass

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


# Concrete product
class PowerSupply(DeviceDriver):
    def __init__(self):
        print 'create power supply object'

    def initialize(self):
        print 'initializing power supply'

    def self_test(self):
        print 'built in self tet for power supply'

    def configure(self):
        print 'Configuring power supply'

    def cleanup(self):
        print 'cleaning up power supply'


# Concrete product
class Multimeter(DeviceDriver):
    def __init__(self):
        print 'create multimeter object'

    def initialize(self):
        print 'initializing multimeter'

    def self_test(self):
        print 'built in self test dmm'

    def configure(self):
        print 'command to configure multimeter'

    @staticmethod
    def measure_dc():
        print 'measuring dc volts'

    def cleanup(self):
        print 'cleaning up multimeter'


# Concrete product
class Oscilloscope(DeviceDriver):
    def __init__(self):
        print 'create oscilloscope object'

    def initialize(self):
        print 'initializing TDS scope'

    def self_test(self):
        print 'built in self test for TDS'

    def configure(self):
        print 'command to configure TDS'

    def cleanup(self):
        print 'cleaning up scope'

# Creator
class RackConfiguration(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.instruments = []
        self.create_layout()

    @abstractmethod
    def create_layout(self):
        pass

    def add_instruments(self, instrument):
        self.instruments.append(instrument)

    def get_instruments(self):
        return self.instruments


# Concrete creator
class BackEndRack(RackConfiguration):
    def create_layout(self):
        self.add_instruments(PowerSupply)
        self.add_instruments(Multimeter)


class FrontEndRack(RackConfiguration):
    def create_layout(self):
        self.add_instruments(PowerSupply)
        self.add_instruments(Multimeter)
        self.add_instruments(Oscilloscope)

# Usage
if __name__ == '__main__':
    print 'creating and using FrontEnd rack \n'
    rack = FrontEndRack()
    rack_ps = rack.instruments[device['PowerSupply']]()
    rack_ps.initialize()
    rack_mm = rack.instruments[device['Multimeter']]()
    rack_mm.initialize()
    print

    rack_ps.configure()
    rack_mm.configure()

    # This is the meat
    print 'main execution:\n'
    rack_ps.self_test()
    rack_mm.measure_dc()
    print

    rack_ps.cleanup()
    rack_mm.cleanup()

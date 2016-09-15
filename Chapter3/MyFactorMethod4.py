from abc import ABCMeta, abstractmethod, abstractproperty


# Interface
class Embedded(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def os(self):
        pass

    @abstractproperty
    def communication(self):
        pass

    @abstractproperty
    def memory(self):
        pass


# Concrete interfaces
class Zync(Embedded):
    def os(self):
        print 'Running linux'

    def memory(self):
        print 'memory is 64M for Zync'

    def communication(self):
        print 'Zynq comm'


class Raspberry(Embedded):
    def os(self):
        print 'Pi os Noob'

    def memory(self):
        print 'Raspberry pi mem'

    def communication(self):
        print 'Communication wifi'


# creator
class SystemConfiguration(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.instrument = None
        self.create_instrument()

    @abstractmethod
    def create_instrument(self):
        pass

    def add_instrument(self, instrument):
        self.instrument = instrument

    def get_instrument(self):
        return self.instrument


# concrete creator
class TestFixture(SystemConfiguration):
    def create_instrument(self):
        self.instrument = Zync


class WaterController(SystemConfiguration):
    def create_instrument(self):
        self.instrument = Raspberry


# usage
if __name__ == '__main__':
    print 'configure embedded device [WaterController, TestFixture]'
    embedded = WaterController()
    embedded.instrument().memory()
    embedded.instrument().os()




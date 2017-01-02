from abc import ABCMeta, abstractmethod

# Interface
class IVIPowerSuppply(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def dc_measure(self):
        pass

    @abstractmethod
    def close(self):
        pass


# Concrete interface
class Sorensen(IVIPowerSuppply):
    def open(self):
        print 'Start sorensen'

    def dc_measure(self):
        print 'Sorensen dc measure'

    def close(self):
        print 'Closing Sorensen power'


class AgilentPower(IVIPowerSuppply):
    def open(self):
        print 'Start Agilent power'

    def dc_measure(self):
        print 'Agilent dc measure'

    def close(self):
        print 'Closing Agilent power'


class Tektronics(IVIPowerSuppply):
    def open(self):
        print 'Start Tektronics power'

    def dc_measure(self):
        print 'Tektronics dc measure'

    def close(self):
        print 'Closing Tektronics power'


# creator
class Communication(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.device = None
        self.select_power()

    @abstractmethod
    def select_power(self):
        pass

    def set_type(self, value):
        self.device = value

    def get_type(self):
        return self.device


# concrete creator
class GPIBPowerSupply(Communication):

    def select_power(self):
        self.device = Sorensen


class USBPowerSupply(Communication):

    def select_power(self):
        self.device = Tektronics

# usage
if __name__ == '__main__':
    style = raw_input('What type of power supply [GPIB, USB]')
    if style[0].upper() == 'G':
        ps = GPIBPowerSupply()
        ps.device().open()
    elif style[0].upper() == 'U':
        ps = USBPowerSupply()
        ps.device().open()
    else:
        raise ValueError('Instrument not defined')
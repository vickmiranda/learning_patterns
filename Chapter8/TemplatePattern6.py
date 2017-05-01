from abc import ABCMeta, abstractmethod


class UpdateDevice(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def update_firmware(self):
    pass

  @abstractmethod
  def update_bios(self):
    pass

  @abstractmethod
  def update_fpga(self):
    pass

  @abstractmethod
  def update_cpld(self):
    pass

  def LyraUpdate(self):
    self.update_firmware()
    self.update_bios()
    self.update_fpga()
    self.update_cpld()

  def BellantrixUpdate(self):
    self.update_firmware()
    self.update_fpga()


class UpdateLyra(UpdateDevice):

  def update_firmware(self):
    print 'update lyra f/w'

  def update_bios(self):
    print 'update lyra bios'

  def update_fpga(self):
    print 'update lyra fpga'

  def update_cpld(self):
    print 'update lyra cpld'


class UpdateBellantrix(UpdateDevice):

  def update_firmware(self):
    print 'update bellantrix f/w'

  def update_bios(self):
    pass

  def update_fpga(self):
    print 'update bellantrix fpga'

  def update_cpld(self):
    pass


if __name__ == '__main__':
    import random

    part_number = random.choice(['1234', '5678'])
    if part_number == '1234':
      update_dut = UpdateLyra()
      update_dut.LyraUpdate()
    else:
      update_dut = UpdateBellantrix()
      update_dut.BellantrixUpdate()
    print part_number

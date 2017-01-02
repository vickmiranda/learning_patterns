class MySingleton(object):
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not MySingleton._instance:
      MySingleton._instance = super(
        cls, MySingleton).__new__(cls, *args, **kwargs)
    return MySingleton._instance

  def __init__(self):
    self.space = []

  def add_memory_space(self, range):
    self.space.append(range)

  def get_all_space(self):
    print 'notice how they share the same physical space'
    return self.space


class ConfigureRam(object):
  def __init__(self):
    self.ram = MySingleton()

  def add_ram(self):
    self.ram.add_memory_space('0x0-0x100')
    self.ram.add_memory_space('0x101-0x200')

  def check_memory(self):
    return self.ram.get_all_space()


class ConfigureRom(object):
  def __init__(self):
    self.rom = MySingleton()

  def add_rom(self):
    self.rom.add_memory_space('0x201-0x300')
    self.rom.add_memory_space('0x301-0x400')

  def check_memory(self):
    return self.rom.get_all_space()


class ConfigureMemory(object):
  def __init__(self):
    self.ram = ConfigureRam()
    self.rom = ConfigureRom()

  def config_memory(self):
    self.ram.add_ram()
    self.rom.add_rom()

  def check_memory(self):
    print self.ram.check_memory()
    print self.rom.check_memory()


if __name__ == '__main__':
  Mem = ConfigureMemory()
  Mem.config_memory()
  Mem.check_memory()





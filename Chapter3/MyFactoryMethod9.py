from abc import ABCMeta, abstractmethod


# product interface
class OperatingSystem(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def installing_system(self):
    pass

  @abstractmethod
  def remove_system(self):
    pass


# concrete products
class Windows(OperatingSystem):
  def installing_system(self):
    print 'installing windows 10'

  def remove_system(self):
    print 'uff removing unpleasant os'


class Linux(OperatingSystem):
  def installing_system(self):
    print 'installing linux'

  def remove_system(self):
    print 'remove linux, please come back again'


class Unix(OperatingSystem):
  def installing_system(self):
    print 'installing unix os'

  def remove_system(self):
    print 'remove unix'


class CreateInventory(object):
  __metaclass__ = ABCMeta
  def __init__(self):
    self.computers = []
    self.create_inventory()

  @abstractmethod
  def create_inventory(self):
    pass

  def add_computers(self, pc):
    self.computers.append(pc)

  def get_inventory(self):
    return self.computers


class One(CreateInventory):
  def create_inventory(self):
    self.add_computers(Linux)
    self.add_computers(Windows)


class Two(CreateInventory):
  def create_inventory(self):
    self.add_computers(Linux)
    self.add_computers(Unix)
    self.add_computers(Windows)


class Three(CreateInventory):
  def create_inventory(self):
    self.add_computers(Unix)
    self.add_computers(Unix)
    self.add_computers(Linux)


if __name__ == '__main__':
  warehouse = input("Give me the warehouse to build? [One, Two, Three]")

  build = warehouse()
  for i in range(len(build.computers)):
    build.computers[i]().installing_system()

  print

  for i in range(len(build.computers)):
    build.computers[i]().remove_system()



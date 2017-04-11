from abc import ABCMeta, abstractmethod


# common interface
class CommonInterface(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def list(self):
    pass

  @abstractmethod
  def create_dir(self):
    pass

  @abstractmethod
  def delete_dir(self):
    pass

  def execute_all(self):
    self.list()
    self.create_dir()
    self.delete_dir()


# proxy class
class ProxyClass(CommonInterface):

  def __init__(self):
    self.os = None

  def select_os(self):
    response = raw_input("Select the type of operating system [1-Windows, 2-Linux, 3-OSX]")
    if response == '1':
      self.os = Windows()
    elif response == '2':
      self.os = Linux()
    elif response == '3':
      self.os = OSX()

    else:
      print 'Invalid os'
      raise

  def list(self):
    self.os.list()

  def create_dir(self):
    self.os.create_dir()

  def delete_dir(self):
    self.os.delete_dir()


# real objects
class Windows(CommonInterface):

  def list(self):
    print 'dir on windows'

  def create_dir(self):
    print 'mkdir on windows'

  def delete_dir(self):
    print 'del on windows'


class Linux(CommonInterface):

  def list(self):
    print 'ls'

  def create_dir(self):
    print 'mkdir'

  def delete_dir(self):
    print 'rf -rf dir_name'


class OSX(CommonInterface):

  def list(self):
    print 'dir'

  def create_dir(self):
    print 'mkdir'

  def delete_dir(self):
    print 'del dir OSX'


# customer
class PlayCommands(object):
  os = ProxyClass()
  os.select_os()

  os.execute_all()


# usage
if __name__ == '__main__':
  PlayCommands()
from abc import ABCMeta, abstractmethod


class Customer(object):
  def __init__(self):
    print 'customer init'
    self.wall = Communication()

  def start_communication(self):
    self.wall.decrypt()
    print 'complete decrypting'
    self.wall.encode()
    print 'good now try'


# Abstract method
class Message(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    print ('Please start message\n')

  @abstractmethod
  def decrypt(self):
    pass

  @abstractmethod
  def encode(self):
    pass


# Object, this is not seen by the customer
class Morse(Message):
  def decrypt(self):
    print 'decrypting morse code'

  def encode(self):
    print 'create morse code'


# This is the proxy which servers as the wall
class Communication(Message):
  def __init__(self):
    super(Communication, self).__init__()
    self.morse = Morse()

  def decrypt(self):
    self.morse.decrypt()
    print 'start talk proxy'

  def encode(self):
    print 'proxy listening ..'


if __name__ == '__main__':
    com = Customer()
    com.start_communication()




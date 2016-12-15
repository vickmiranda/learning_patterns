from abc import ABCMeta, abstractmethod


class CommonInterface(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def process_data(self):
    pass


class ProxyClass(CommonInterface):
  def __init__(self):
    print 'start proxy class'
    self.video = VideoProcessing()
    self.audio = AudioProcessing()

  def process_data(self):
    print 
    print 'Heavy computation'
    self.video.process_data()
    self.audio.process_data()


class VideoProcessing(CommonInterface):
  def __init__(self):
    print 'starting video processing'

  def process_data(self):
    print 'analysis video data'


class AudioProcessing(CommonInterface):
  def __init__(self):
    print 'starting audio processing'

  def process_data(self):
    print 'analysis audio data'


class Customer(object):
  def __init__(self):
    print 'init proxy'
    self.proxy = ProxyClass()

  def start_process(self):
    self.proxy.process_data()


if __name__ == '__main__':
  customer = Customer()
  customer.start_process()


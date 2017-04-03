from abc import ABCMeta, abstractmethod


class WeatherBroadcast(object):
  def __init__(self):
    self.stations = []

  def register(self, station):
    self.stations.append(station)

  def notify_all(self, *args, **kwargs):
    for station in self.stations:
      print 'notifying all stations'
      station.notify(*args, **kwargs)


class Bandwidth(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def notify(self):
    pass


class Classical(Bandwidth):
  def __init__(self, broadcast):
    self.broadcast = broadcast
    self.broadcast.register(self)

  def notify(self, *args, **kwargs):
    print(type(self).__name__,
          'got: ', args, kwargs, 'from', type(self.broadcast).__name__)


class Oldies(Bandwidth):
  def __init__(self, broadcast):
    self.broadcast = broadcast
    self.broadcast.register(self)

  def notify(self, *args, **kwargs):
    print(type(self).__name__,
          'got: ', args, kwargs, 'from', type(self.broadcast).__name__)


class Pop(Bandwidth):
  def __init__(self, broadcast):
    self.broadcast = broadcast
    self.broadcast.register(self)

  def notify(self, *args, **kwargs):
    print(type(self).__name__,
          'got: ', args, kwargs, 'from', type(self.broadcast).__name__)


if __name__ == '__main__':
    broadcast = WeatherBroadcast()

    for ch in [Classical, Oldies, Pop]:
        ch(broadcast)

    broadcast.notify_all("Weather storm", "Please be advise bla bla", 5,
                         notify='this alert', code='yellow code')

    print
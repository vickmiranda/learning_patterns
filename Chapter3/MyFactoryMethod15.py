""" This is a factory method try."""

from abc import ABCMeta, abstractmethod


# Interface
class MusicalInstrument(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def tune(self):
    pass

  @abstractmethod
  def play(self):
    pass


# Concrete interface
class Violin(MusicalInstrument):
  def tune(self):
    print 'tuning violin'

  def play(self):
    print 'playing violin'


class Cello(MusicalInstrument):
  def tune(self):
    print 'tuning cello'

  def play(self):
    print 'playing cello'


# Concrete interface
class Clarinet(MusicalInstrument):
  def tune(self):
    print 'tuning clarinet'

  def play(self):
    print 'playing clarinet'


class Tuba(MusicalInstrument):
  def tune(self):
    print 'tuning tuba'

  def play(self):
    print 'playing tuba'


# creator
class InstrumentCreator(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.instruments = []
    self.add_instruments()

  @abstractmethod
  def add_instruments(self):
    pass

  def tune_all(self):
    for i in self.instruments:
      i().tune()

  def play_all(self):
    for i in self.instruments:
      i().play()


# concrete creator
class StringConcert(InstrumentCreator):
  def add_instruments(self):
    self.instruments.append(Cello)
    self.instruments.append(Violin)


class WindConcert(InstrumentCreator):
  def add_instruments(self):
    self.instruments.append(Tuba)
    self.instruments.append(Clarinet)

# usage
if __name__ == '__main__':
    concert = StringConcert()
    concert.tune_all()
    concert.play_all()
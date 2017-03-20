from abc import ABCMeta, abstractmethod
# Interface

class Sport(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def practice(self):
    pass

  @abstractmethod
  def train(self):
    pass

  @abstractmethod
  def participate(self):
    pass


# Concrete interface
class Football(Sport):
  def practice(self):
    print 'Start football practice'

  def train(self):
    print 'Training football'

  def participate(self):
    print 'Football tournament'


# Concrete interface
class Volleyball(Sport):
  def practice(self):
    print 'Start volleyball practice'

  def train(self):
    print 'Training volleyball'

  def participate(self):
    print 'volleyball tournament'


# Concrete interface
class Tennis(Sport):
  def practice(self):
    print 'Start tennis practice'

  def train(self):
    print 'Training tennis'

  def participate(self):
    print 'tennis tournament'


# creator
class TypeSport(object):
  __metaclass__ = ABCMeta
  def __init__(self):
    self.sport_type = []
    # Always an abstract method
    self.create_sport()

  @abstractmethod
  def create_sport(self):
    pass

  def add_sports(self, sport):
    self.sport_type.append(sport)

  def get_sports(self):
    return self.sport_type

  def get_single_spport(self, index):
    return self.sport_type[index]

# concrete creator
class EliteSports(object):
  pass

# usage
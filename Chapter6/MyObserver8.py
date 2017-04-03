from abc import ABCMeta, abstractmethod


class SportPlan(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.sport_list = []

  def add_plan(self, sport):
    self.sport_list.append(sport)

  def warmup(self):
    for test in self.sport_list:
      test.warm_up()

  def train(self):
    for test in self.sport_list:
      test.train()

  def cooloff(self):
    for test in self.sport_list:
      test.cooloff()


class Sport(object):
  __metaclass__ = ABCMeta

  def __init__(self, sport):
    self.sport = sport
    self.sport.add_plan(self)

  @abstractmethod
  def warm_up(self):
    pass

  @abstractmethod
  def train(self):
    pass

  @abstractmethod
  def cooloff(self):
    pass


class Bike(Sport):

  def warm_up(self):
    print 'run bike warm up'

  def train(self):
    print 'run bike train'

  def cooloff(self):
    print 'run bike cooloff'


class Swim(Sport):

  def warm_up(self):
    print 'run swim warm up'

  def train(self):
    print 'run swim train'

  def cooloff(self):
    print 'run swim cooloff'


class Run(Sport):

  def warm_up(self):
    print 'run warm up'

  def train(self):
    print 'run train'

  def cooloff(self):
    print 'run cooloff'


if __name__ == '__main__':

  sport = SportPlan()
  for sp in [Run, Swim, Bike]:
    sp(sport)

  sport.warmup()
  sport.train()
  sport.cooloff()





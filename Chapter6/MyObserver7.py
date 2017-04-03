from abc import ABCMeta, abstractmethod


class TestPlan(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.test_list = []

  def add_test(self, test):
    self.test_list.append(test)

  def setup(self):
    for test in self.test_list:
      test.setup()

  def execute(self):
    for test in self.test_list:
      test.execute()

  def cleanup(self):
    for test in self.test_list:
      test.cleanup()


class BaseTest(object):
  __metaclass__ = ABCMeta

  def __init__(self, plan):
    self.plan = plan
    self.plan.add_test(self)

  @abstractmethod
  def setup(self):
    pass

  @abstractmethod
  def execute(self):
    pass

  @abstractmethod
  def cleanup(self):
    pass


class Video(BaseTest):

  def setup(self):
    print 'run video setup'

  def execute(self):
    print 'run video execute'

  def cleanup(self):
    print 'run video cleanup'


class Audio(BaseTest):
  def setup(self):
    print 'run audio setup'

  def execute(self):
    print 'run audio execute'

  def cleanup(self):
    print 'run audio cleanup'


class Voltage(BaseTest):
  def setup(self):
    print 'run voltage setup'

  def execute(self):
    print 'run voltage execute'

  def cleanup(self):
    print 'run voltage cleanup'


if __name__ == '__main__':
  tp = TestPlan()
  for test in [Video, Audio, Voltage]:
    test(tp)

  tp.setup()
  print
  tp.execute()
  print
  tp.cleanup()

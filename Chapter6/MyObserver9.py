from abc import ABCMeta
from abc import abstractmethod


class HealthPlan(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.plan = []

  def add_plan(self, plan):
    self.plan.append(plan)

  def create_plan(self):
    for plan in self.plan:
      plan.create_plan()

  def change_plan(self):
    for plan in self.plan:
      plan.change_plan()


class BasePlan(object):
  __metaclass__ = ABCMeta

  def __init__(self, plan):
    self.plan = plan
    self.plan.add_plan(self)

  @abstractmethod
  def create_plan(self):
    pass

  @abstractmethod
  def change_plan(self):
    pass


class HMO(BasePlan):
  def create_plan(self):
    print 'creating HMO plan'

  def change_plan(self):
    print 'changing HMO plan'


class PPO(BasePlan):
  def create_plan(self):
    print 'creating PPO plan'

  def change_plan(self):
    print 'changing PPO plan'


class HDPC(BasePlan):
  def create_plan(self):
    print 'creating HDPC plan'

  def change_plan(self):
    print 'changing HDPC plan'


if __name__ == '__main__':
    health_plan = HealthPlan()
    for hp in [HMO, PPO, HDPC]:
      hp(health_plan)

    health_plan.create_plan()
    health_plan.change_plan()

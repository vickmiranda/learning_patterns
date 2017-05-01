# Facade
class PlanLife(object):
  def __init__(self):
    self.prayer = Prayer()
    self.actions = Actions()
  def start_day(self):
    self.prayer.morning_prayer()
    self.actions.go_mass()

  def mid_day(self):
    self.actions.help_someone()
    self.prayer.angelus()

  def end_day(self):
    self.actions.visit_sick()
    self.prayer.rosary()


# Sub-system1
class Prayer(object):
  def morning_prayer(self):
    print 'start the day with morning prayer'

  def angelus(self):
    print 'Noon time for angelus'

  def rosary(self):
    print 'Hail Mary..'


# Sub-system2
class Actions(object):
  def help_someone(self):
    print 'Help the needy'

  def go_mass(self):
    print 'Go to daily mass'

  def visit_sick(self):
    print 'go to the hospital'

# Sub-system3


# Client
class GoodBoy(object):
  def __init__(self):
    self.plan = PlanLife()

  def run(self):
    self.plan.start_day()
    self.plan.mid_day()
    self.plan.end_day()

# Usage
if __name__ == '__main__':
  boy = GoodBoy()
  boy.run()
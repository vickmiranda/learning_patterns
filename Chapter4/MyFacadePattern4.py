#TODO the type of actions follow more the command pattern, do this using it


# Facade
class Triathlon(object):
  def __init__(self):
    print 'starting event'

  def leg_one(self):

    swim = Swimming()
    swim.action()
    swim.complete()

  def leg_two(self):

    bike = Biking()
    bike.get_gear()
    bike.action()
    bike.complete()

  def leg_three(self):

    run = Running()
    run.get_gear()
    run.action()
    run.complete()


class Swimming(object):
  def get_gear(self):
    print 'preparing gear'

  def action(self):
    print 'swimming'

  def complete(self):
    print 'go to transition area'


class Biking(object):
  def get_gear(self):
    print 'take bike'

  def action(self):
    print 'start the bike route'

  def complete(self):
    print 'go to transition area'


class Running(object):
  def get_gear(self):
    print 'take your shoes'

  def action(self):
    print 'start the last leg'

  def complete(self):
    print 'finish strong'


class Triathlete(object):
  tri = Triathlon()
  tri.leg_one()
  tri.leg_two()
  tri.leg_three()


if __name__ == '__main__':
  triathlon = Triathlon()

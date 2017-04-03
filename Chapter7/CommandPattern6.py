from abc import ABCMeta, abstractmethod

# command interface
class Command(object):
  __metaclass__ = ABCMeta

  def __init__(self, cmd, action):
    self.command = cmd
    self.action = action

  @abstractmethod
  def execute(self):
    pass

# This is something I added to keep the invoker cleaner
class Invoke(object):
  __metaclass__ = ABCMeta
  def __init__(self):
    self.queue = []

  def add_cmd(self, action):
    self.queue.append(action)

  @abstractmethod
  def perform(self):
    pass


# concrete commands below
class ShiftGear(Command):
  def execute(self):
    if self.action == 'forward':

      self.command.forward()
    elif self.action == 'reverse':
      self.command.reverse()

    else:
      self.command.invalid()


class ChangeSpeed(Command):
  def execute(self):
    if self.action == 'accelerate':
      self.command.accelerate()

    elif self.action == 'stop':
      self.command.halt()

    else:
      self.command.invalid()


class ChangeDirection(Command):
  def execute(self):
    if self.action == 'right':
      self.command.right()

    elif self.action == 'left':
      self.command.left()

    else:
      self.command.invalid()

# receiver this class
class Drive(object):
  def forward(self):
    print 'going forward'

  def reverse(self):
    print 'going backwards'

  def accelerate(self):
    print 'going up to high speed'

  def halt(self):
    print 'stoping the vehicule'

  def right(self):
    print 'turning right'

  def left(self):
    print 'going left'

  def invalid(self):
    print 'command not allowed!!'


#invoker, I need to remember - using a metaclass
class Driver(Invoke):

  def perform(self):
    for action in self.queue:
      action.execute()


if __name__ == '__main__':
  drive = Drive()
  rev = ShiftGear(drive, 'reverse')
  fwd = ShiftGear(drive, 'forward')
  acc = ChangeSpeed(drive, 'accelerate')
  left = ChangeDirection(drive, 'left')
  right = ChangeDirection(drive, 'right')
  stop = ChangeSpeed(drive, 'stop')
  up = ChangeDirection(drive, 'up')

  driver = Driver()

  driver.add_cmd(rev)
  driver.add_cmd(fwd)
  driver.add_cmd(acc)
  driver.add_cmd(left)
  driver.add_cmd(right)
  driver.add_cmd(stop)
  driver.add_cmd(up)

  driver.perform()





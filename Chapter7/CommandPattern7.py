from abc import ABCMeta, abstractmethod


# Command interface
class Command(object):
  def __init__(self, command, action):
    self.command = command
    self.action = action

  @abstractmethod
  def execute(self):
    pass


# The concrete commands are below
class Futbol(Command):
  def execute(self):
    if self.action == 'kick':
      self.command.kick()

    elif self.action == 'head':
      self.command.head()


class VoleyBall(Command):
  def execute(self):
    if self.action == 'serve':
      self.command.server()

    elif self.action == 'pass':
      self.command.set_ball()


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


# receiver this class
class Play(object):
  def kick(self):
    print 'kicking the ball'

  def head(self):
    print 'scoring a goal with head'

  def serve(self):
    print 'Good serve and point'

  def set_ball(self):
    print 'pass ball to teammate'


# Who invokes the command?
class Player(Invoke):
  def perform(self):
    for action in self.queue:
      action.execute()

if __name__ == '__main__':
  # Receiver

  play = Play()
  head = Futbol(play, 'head')
  kick = Futbol(play, 'kick')

  Maradona = Player()
  Maradona.add_cmd(head)
  Maradona.add_cmd(kick)

  Maradona.perform()
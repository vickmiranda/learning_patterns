from abc import ABCMeta, abstractmethod


class Command(object):
  __metaclass__ = ABCMeta

  def __init__(self, rcv):
    self.rcv = rcv

  @abstractmethod
  def execute(self):
    pass


class ReceiverOne(Command):
  def execute(self):
    self.rcv.action()


class ReceiverTwo(Command):
  def execute(self):
    self.rcv.action()


class ReceiverClass(object):
  def action(self):
    print 'receiver taking this action'


class Agent(object):
  def __init__(self):
    self._cmdQueue = []

  def add_commands(self, action):
    self._cmdQueue.append(action)

  def execute(self):
    for cmd in self._cmdQueue:
      cmd.execute()

if __name__ == '__main__':
    action = ReceiverClass()
    execute1 = ReceiverOne(action)
    execute2 = ReceiverTwo(action)
    agent = Agent()
    agent.add_commands(execute1)
    agent.add_commands(execute2)
    agent.execute()




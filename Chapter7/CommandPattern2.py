from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class Receiver(object):
    def action(self):
        print 'receiver action'


class Invoker(object):
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    inv = Invoker()
    inv.command(cmd)
    inv.execute()



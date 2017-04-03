from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class Launch(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.launch()


class Land(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.land()


class Orbit(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.orbite()


class Operation(object):
    def launch(self):
        print 'operation launch rocket'

    def land(self):
        print 'landing rocket'

    def orbite(self):
        print 'orbiting the device'


# Invoker is the one controlling the thing
class ControlCommand(object):
    def __init__(self):
        self.queue = []

    def operate_rocket(self, operation):
        self.queue.append(operation)
        operation.execute()


# The client
if __name__ == '__main__':
    # basic commands object
    execute = Operation()
    # create which cmd to execute
    launch = Launch(execute)
    gravitate = Orbit(execute)

    # finally, pass those to the invoker
    control = ControlCommand()
    control.operate_rocket(launch)
    control.operate_rocket(gravitate)






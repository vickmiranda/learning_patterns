from abc import ABCMeta, abstractmethod
import threading
import Queue

my_queue = Queue.Queue()

# My base command
class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


# Concrete command 1
class Axis1(Command):
    def __init__(self, move, side):
        self.move = move
        self.side = side

    def execute(self):
        if self.side == 'left':
            self.move.left()
        elif self.side == 'right':
            self.move.right()
        else:
            print 'move not allowed'


# Concrete command 2
class Axis2(Command):
    def __init__(self, move, side):
        self.move = move
        self.side = side

    def execute(self):
        if self.side == 'up':
            self.move.up()
        elif self.side == 'down':
            self.move.down()
        else:
            print 'move not allowed'


# This is the receiver, represents the final interaction
class Motion(object):
    def left(self):
        print 'moving left'

    def right(self):
        print 'moving right'

    def up(self):
        print 'moving up'

    def down(self):
        print 'moving down'


# The invoker is the controller of course
class Joystick(object):
    def __init__(self):
        self.queue = []

    def move_bot(self, move):
        self.queue.append(move)
        move.execute()


if __name__ == '__main__':
    motion = Motion()
    left = Axis1(motion, 'left')
    right = Axis1(motion, 'right')
    joystick = Joystick()

    joystick.move_bot(left)
    joystick.move_bot(right)

    up = Axis2(motion, 'up')
    down = Axis2(motion, 'down')
    # to create a bad move
    left = Axis2(motion, 'left')

    joystick.move_bot(up)
    joystick.move_bot(down)
    joystick.move_bot(left)




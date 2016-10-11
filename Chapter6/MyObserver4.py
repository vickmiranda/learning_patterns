from abc import ABCMeta, abstractmethod


class TVBroadcast(object):
    def __init__(self):
        self.channels = []

    def register(self, channel):
        self.channels.append(channel)

    def notify_all(self, *args, **kwargs):
        for channel in self.channels:
            print 'Notifying all channels'
            channel.notify(*args, **kwargs)


class Channel(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self):
        pass


class NBC(Channel):
    def __init__(self, broadcast):
        self.broadcast = broadcast
        self.broadcast.register(self)

    def notify(self, *args, **kwargs):
        print (type(self).__name__,
               'got: ', args, kwargs, 'from', type(self.broadcast).__name__)


class CBS(Channel):
    def __init__(self, broadcast):
        self.broadcast = broadcast
        self.broadcast.register(self)

    def notify(self, *args, **kwargs):
        print (type(self).__name__,
               'got: ', args, kwargs, 'from', type(self.broadcast).__name__)
        if kwargs:
            for val in kwargs.values():
                print val


class HBO(Channel):
    def __init__(self, broadcast):
        self.broadcast = broadcast
        self.broadcast.register(self)

    def notify(self, *args, **kwargs):
        print (type(self).__name__,
               'got: ', args, kwargs, 'from', type(self.broadcast).__name__)


if __name__ == '__main__':
    broadcast = TVBroadcast()

    for ch in [NBC, HBO, CBS]:
        ch(broadcast)

    broadcast.notify_all("Weather storm", "Please be advise bla bla", 5,
                         notify='this alert', code='yellow code')

    print

    broadcast.notify_all("Presidential election")


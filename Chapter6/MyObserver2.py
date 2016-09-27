from abc import ABCMeta, abstractmethod


class Linkedin(object):
    def __init__(self):
        self._membership = []

    def register(self, observer):
        self._membership.append(observer)

    def email_all(self, *args, **kwargs):
        for member in self._membership:
            member.notify(self, *args, **kwargs)
    
    def maintenance(self, *args, **kwargs):
        for member in self._membership:
            member.notify(self, *args, **kwargs)


class People(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass

    @abstractmethod
    def maintenance(self, *args):
        pass


class Person1(People):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, *args, **kwargs):
        print (type(self).__name__, 'got:', args, 'from',
               type(self.subject).__name__)

    def maintenance(self, *args):
        print (type(self).__name__, 'got', args, 'from',
               type(self.subject).__name__)


class Person2(People):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, *args, **kwargs):
        print (type(self).__name__, 'got:', args, 'from',
               type(self.subject).__name__)

    def maintenance(self, *args):
        print (type(self).__name__, 'got', args, 'from',
               type(self.subject).__name__)

linkeding = Linkedin()
lulu = Person1(linkeding)
paco = Person2(linkeding)

linkeding.email_all('Send email')
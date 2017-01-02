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
    def notify(self, *args):
        pass

    @abstractmethod
    def maintenance(self, *args):
        pass


class Person1(People):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, *args):
        print (type(self).__name__, 'got:', args, 'from',
               type(self.subject).__name__)

    def maintenance(self, *args):
        print (type(self).__name__, 'got', args, 'from',
               type(self.subject).__name__)


class Person2(People):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, *args):
        print (type(self).__name__, 'got:', args, 'from',
               type(self.subject).__name__)

    def maintenance(self, *args):
        print (type(self).__name__, 'got', args, 'from',
               type(self.subject).__name__)

linkedin = Linkedin()
lulu = Person1(linkedin)
paco = Person2(linkedin)

linkedin.email_all('Send email')
print
linkedin.maintenance('This coming Sunday there will be a server shutdown')
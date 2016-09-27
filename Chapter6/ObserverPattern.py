class Subject(object):
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notifyall(self, *args, **kwargs):
        for observer in self._observers:
            print 'broadcasting \n'
            observer.notify(self, *args, **kwargs)


class Observer1(object):
    def __init__(self, Subject):
        Subject.register(self)

    def notify(self, Subject, args):
        print(type(self).__name__, ':: Got', args, 'From', Subject)


class Observer2(object):
    def __init__(self, Subject):
        Subject.register(self)

    def notify(self, Subject, args):
        print(type(self).__name__, '::Got', args, 'From', Subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyall('notification')



from abc import ABCMeta, abstractmethod


class GitHub(object):
    def __init__(self):
        self._programmers = []
        self.send_message = None

    def add(self, programmer):
        self._programmers.append(programmer)

    def remove(self, programmer):
        self._programmers.remove(programmer)

    def notify(self):
        for member in self._programmers:
            member.update()

    def add_news(self, news):
        self._send_message = news

    def get_news(self):
        return self._send_message


class Subscriber(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def update(self):
    pass


class PythonProgramer(Subscriber):
    def __init__(self, platform):
        self.platform = platform
        self.platform.add(self)

    def update(self):
        print (type(self).__name__ , ' got news: {} from '.format(self.platform.get_news()), type(self.platform).__name__)


if __name__ == '__main__':
    platform = GitHub()
    member = PythonProgramer(platform)
    platform.add_news("My excellent news")
    platform.notify()
   

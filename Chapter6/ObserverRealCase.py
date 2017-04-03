from abc import ABCMeta, abstractmethod


class NewsPublisher(object):
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def attached(self, subscriber):
        self._subscribers.append(subscriber)

    def detached(self):
        self._subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self._subscribers]

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        self._latest_news = news

    def get_news(self):
        return self._latest_news


class Subscriber(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attached(self)

    def update(self):
        print (type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attached(self)

    def update(self):
        print (type(self).__name__, self.publisher.get_news())


class AnotherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attached(self)

    def update(self):
        print (type(self).__name__, self.publisher.get_news())

if __name__ == '__main__':
    news_publisher = NewsPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnotherSubscriber]:
        Subscribers(news_publisher)
    print("Subscribers:", news_publisher.subscribers())

    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()

    print("Detached:", type(news_publisher.detached()).__name__)
    print("Subscribers:", news_publisher.subscribers())

    news_publisher.add_news('My second news!')
    news_publisher.notify_subscribers()
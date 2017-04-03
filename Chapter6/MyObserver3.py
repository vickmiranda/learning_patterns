from abc import ABCMeta, abstractmethod


class StudentMedia(object):
    def __init__(self):
        self._students = []
        self._news = None

    def register(self, student):
        self._students.append(student)

    def notify(self):
        for student in self._students:
            student.update()

    def news(self, publish):
        self._news = publish

    def get_news(self):
        return self._news


class Student(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class FirstGraders(Student):
    def __init__(self, media):
        self.media = media
        self.media.register(self)

    def update(self):
        print (type(self).__name__, self.media.get_news())


class SecondGraders(Student):
    def __init__(self, media):
        self.media = media
        self.media.register(self)

    def update(self):
        print (type(self).__name__, self.media.get_news())


class ThirdGraders(Student):
    def __init__(self, media):
        self.media = media
        self.media.register(self)

    def update(self):
        print (type(self).__name__, self.media.get_news())


if __name__ == '__main__':
    media = StudentMedia()
    # registering observers
    first = FirstGraders(media)
    sec = SecondGraders(media)

    # Broadcasting updates to all
    media.news('Good morning students!')
    media.notify()
    print
    media.news('Today we celebrate the school anniversary')
    media.notify()
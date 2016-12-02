from abc import ABCMeta, abstractmethod


class Facebook(object):
  def __init__(self):
    self._members = []
    self._send_message = None

  def add(self, member):
    self._members.append(member)

  def remove(self):
    self._members.pop()

  def members(self):
    return [type(x).__name__ for x in self._members]

  def notify(self):
    for member in self._members:
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


class Male(Subscriber):
  def __init__(self, member):
    self.member = member
    self.member.add(self)

  def update(self):
    print (type(self).__name__, self.member.get_news())


class Female(Subscriber):
  def __init__(self, member):
    self.member = member
    self.member.add(self)

  def update(self):
    print (type(self).__name__, self.member.get_news())


class Teen(Subscriber):
  def __init__(self, member):
    self.member = member
    self.member.add(self)


class Young_adult(Subscriber):
  def __init__(self, member):
    self.member = member
    self.member.add(self)
    

  def update(self):
    print (type(self).__name__, self.member.get_news())


if __name__ == '__main__':
  user = Facebook()

  for member in [Male, Female, Teen]:
    member(user)
  print("Subscribers:", user.members())

  user.add_news("Welcome to facebook!")
  user.notify()

  user.add_news("Sending you a sticker")
  user.notify()

  user.add_news("Happy birthday to you")
  user.notify()


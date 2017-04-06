class MySingleton(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not MySingleton._instance:
      MySingleton._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
    return MySingleton._instance

  def __init__(self):
    self._servers = []


  def get_servers(self):
    return self._servers

  def set_servers(self, value):
    self._servers.append(value)


m1 = MySingleton()
m2 = MySingleton()

m1.set_servers(1)
m1.set_servers(2)

m2.set_servers(5)
m2.set_servers(6)

print m1
print m1.get_servers()
print m2


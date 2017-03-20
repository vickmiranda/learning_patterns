class MySingleton(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not MySingleton._instance:
      MySingleton._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
    return MySingleton._instance


m1 = MySingleton()
m2 = MySingleton()

print m1
print
print m2


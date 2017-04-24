class MySingleton(object):
  _my_instance = None
  def __new__(cls, *args, **kwargs):
    if not MySingleton._my_instance:
      MySingleton._my_instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
    return MySingleton._my_instance
  def __init__(self):
    self.li = []


single1 = MySingleton()
single2 = MySingleton()

print single1
single1.li.append(1)
print
print single2.li[0]


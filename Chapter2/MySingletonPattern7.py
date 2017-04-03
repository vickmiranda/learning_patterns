class MySingle(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not MySingle._instance:
      MySingle._instance = super(MySingle, cls).__new__(cls, *args, **kwargs)
    return MySingle._instance


a = MySingle()
b = MySingle()

print a
print b

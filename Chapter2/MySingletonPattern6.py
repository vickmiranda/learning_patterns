class MySingleton(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not MySingleton._instance:
      MySingleton._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
    return MySingleton


if __name__ == '__main__':
    c = MySingleton()
    c1 = MySingleton()

    print c
    print c1


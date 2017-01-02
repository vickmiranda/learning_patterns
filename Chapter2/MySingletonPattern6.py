class MySingleton(object):
    _instance = None

    def __init__(self):
        print 'start singleton init'

    def __new__(cls, *args, **kwargs):
        if not MySingleton._instance:
            MySingleton._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
            print 'start instance'
        return MySingleton._instance


new_year = MySingleton()
old_year = MySingleton()

print new_year
print
print new_year.__class__



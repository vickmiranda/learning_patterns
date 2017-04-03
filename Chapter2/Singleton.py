# Use __new__ when the one needs to control the creation of the new instance
class Singleton(object):
    # Overwriting the __new__ method to check if attr exists
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)


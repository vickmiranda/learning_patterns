'''
Let's start with a brief introduction to metaclasses. A metaclass is a class
of a class, which means that the class is an instance of its metaclass. With
metaclasses, programmers get an opportunity to create classes of their own type
from the predefined Python classes. For instance, if you have an object,

'''

class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)


class int(object):
    __metaclass__ = MyInt
    def __init__(self, MirrorCal, SystemCal, Final):
        self.MirrorCal = MirrorCal
        self.SystemCal = SystemCal
        self.Final = Final

class MyString(type):
    def __call__(cls, *args, **kwargs):
        print ("This is mystring class ", args)
        return type.__call__(cls, *args, **kwargs)

class str(object):
    __metaclass__ = MyString
    def __init__(self, MirrorCal, SystemCal, Final):
        self.MirrorCal = MirrorCal
        self.SystemCal = SystemCal
        self.Final = Final

    def count_vowels(self):
        count = 0
        for item in self.__dict__.values():
            for letter in item:
                if letter in ['a', 'e', 'i', 'o', 'u']:
                    count += 1
        return count

station_name = str('MirrorCal', 'SysCal', 'Final')

print station_name.Final
print [x for x in station_name.__dict__]
print station_name.count_vowels()

# try this
StationType = int(1, 2, 3)
print [x for x in StationType.__dict__]
print StationType.Final



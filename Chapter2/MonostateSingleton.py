'''
Singleton design pattern says that there should be one and only one object of a
class. However, as per Alex Martelli, typically what a programmer needs is to
have instances sharing the same state. He suggests that developers should be
bothered about the state and behavior rather than the identity. As the concept
is based on all objects sharing the same state, it is also known as the
Monostate pattern
'''


class Borg:
    __shared_state = {'a': 1}

    def __init__(self):
        self.x = 1
        self.y = 5
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4
b1.y = 600


# b and b1 are distinct objects

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)

# b and b1 share same state
print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__)

# Notice attribute a has not been resolved until runtime
print b1.a

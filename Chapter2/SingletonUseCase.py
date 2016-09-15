'''
One of the use cases for the Singleton pattern is lazy instantiation.
For example, in the case of module imports, we may accidently create an
object even when it's not needed. Lazy instantiation makes sure that the ' \
object gets created when it's actually needed
'''



class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() ## class initialized, but object not created
print("Object created", Singleton.getInstance()) # Object gets created here
s1 = Singleton() ## instance already created

'''
Note

All modules are Singletons by default because of Python's importing behavior.
Python works in the following way:

Checks whether a Python module has been imported.
If imported, returns the object for the module. If not imported,
imports and instantiates it.
So when a module gets imported, it is initialized. However, when the same
module is imported again, it's not initialized again, which relates to the
Singleton behavior of having only one object and returning the same object.
'''
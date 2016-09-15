from abc import ABCMeta, abstractmethod


class Animal(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class Pig(Animal):
    def do_say(self):
        print("Oinc oinc")


# forest factory defined, eval does not work for 2.7
class ForestFactory(object):
    def make_sound(self, object_type):
        return object_type().do_say()

# client code
if __name__ == '__main__':

    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat or Pig?")
    ff.make_sound(animal)
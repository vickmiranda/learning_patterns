from abc import abstractmethod, ABCMeta
from collections import defaultdict


# Abstract interface
class Food(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Burger(Food):
    def get(self):
        print 'Buy meat and bread to prepare it\n'

    def prepare(self):
        print 'Make sure you put mayonnaise on it\n'

    def serve(self):
        print 'Humm I like this burger\n'


class Pizza(Food):
    def get(self):
        print 'Buy italian ingredients too!\n'

    def prepare(self):
        print 'Do you know how to prepare the dough!\n'

    def serve(self):
        print 'You are good preparing pepperoni pizza\n'


class Mole_Poblano(Food):
    def get(self):
        print 'Get pepper, cacao, tomatoes, cinammon, peanuts and almonds\n'

    def prepare(self):
        print 'Use my mom\'s receipe and follow the directions\n'

    def serve(self):
        print 'It has been years since I don\'t test something so delicious\n'


# Creator
class Meal(object):
    __metaclass__ =  ABCMeta

    def __init__(self):
        self.type_food = []
        self.create_plates()

    @abstractmethod
    def create_plates(self):
        pass

    def add_food(self, food):
        self.type_food.append(food)

    def get_food(self):
        return self.type_food


# Follow by concrete creators
class Picnic(Meal):
    def create_plates(self):
        self.add_food(Burger)


class Party(Meal):
    def create_plates(self):
        self.add_food(Mole_Poblano)
        self.add_food(Pizza)


class Restaurant(Meal):
    def create_plates(self):
        self.add_food(Burger)
        self.add_food(Mole_Poblano)
        self.add_food(Pizza)


class MrChef(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not MrChef._instance:
            MrChef._instance = super(MrChef, cls).__new__(cls, *args, **kwargs)
        return MrChef._instance

    def __init__(self):
        self.waiter = defaultdict(dict)

    def add_shift_one(self):
        self.waiter['Tom']
        self.waiter['Vick']
        self.waiter['Mary']

    def add_shift_two(self):

        self.waiter.pop('Tom')
        self.waiter.pop('Mary')
        self.waiter['Alex']
        self.waiter['Rene']
        self.waiter['Lily']

if __name__ == '__main__':
    print 'Mr Chef we need you!!\n'

    # Using singleton, same restaurant anyway!
    Pablo = MrChef()
    Manolo = MrChef()

    Pablo.add_shift_one()
    print 'AM Shift:'
    print '\n'.join(Pablo.waiter.keys())

    Manolo.add_shift_two()
    print 'PM Shift:'
    print '\n'.join(Manolo.waiter.keys())

    # Vick in action
    print 'Pablo says: Vick get things ready for the customers!!\n\n'
    vick = Pablo.waiter['Vick']
    vick = Restaurant()

    for i in range(len(vick.type_food)):
        vick.type_food[i]().prepare()
        vick.type_food[i]().serve()

    # Alex is in action
    print 'Alex please prepare things for the Party!!\n\n'

    alex = Manolo.waiter['Alex']
    alex = Party()

    for i in range(len(alex.type_food)):
        alex.type_food[i]().get()
        alex.type_food[i]().prepare()
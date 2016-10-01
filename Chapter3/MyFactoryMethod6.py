from abc import ABCMeta, abstractmethod, abstractproperty

# Interface
class Car(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, style=None):
        self.style = style
        self.doors = None
        self.max_speed = 0

    @abstractproperty
    def top_speed(self, speed):
        self.max_speed = speed


# Concrete interface
class Sedan(Car):

    def __init__(self):
        super(Sedan, self).__init__(style='Sedan')
        self.set_doors(4)
        self.top_speed(100)
        self._speed = 0
        print 'creating sedan'

    def top_speed(self, speed):
        self.max_speed = speed

    def set_doors(self, doors):
        self.doors = doors

    def accelerate(self, current):
        self._speed = current
        print 'speed is now {}'.format(self._speed)

    def get_speed(self):
        return self._speed


class Truck(Car):
    def __init__(self):
        super(Truck, self).__init__(style='Truck')
        self.set_doors(2)
        self.top_speed(80)
        self._speed = 0
        print 'creating truck'

    def top_speed(self, speed):
        self.max_speed = speed

    def set_doors(self, doors):
        self.doors = doors

    def accelerate(self, current):
        self._speed = current
        print 'speed is now {}'.format(self._speed)

    def get_speed(self):
        return self._speed


class Sport(Car):
    def __init__(self):
        super(Sport, self).__init__(style='Sporty')
        self.doors = 2
        self.top_speed(180)
        self._speed = 0
        print 'creating sporty car'

    def top_speed(self, speed):
        self.max_speed = speed

    def accelerate(self, current):
        self._speed = current
        print 'speed is now {}'.format(self._speed)

    def get_speed(self):
        print 'current speed {}'.format(self._speed)
        return self._speed


# creator
class CarMaker(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.cars = []
        self.create_lot()

    @abstractmethod
    def create_lot(self):
        pass

    def add_cars(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars


# concrete creator
class Ford(CarMaker):
    def create_lot(self):
        self.add_cars(Truck)
        self.add_cars(Sport)


class Tesla(CarMaker):
    def create_lot(self):
        self.add_cars(Sport)
        self.add_cars(Sedan)


# usage
if __name__ == '__main__':
    print 'Factory for cars'
    tesla = Tesla()
    ford = Ford()

    # Careful to instantiate only once
    all_cars = [car() for car in tesla.cars]
    cheap_cars = [car() for car in ford.cars]

    for x in all_cars:
        print 'tesla style {}'.format(x.style)
        x.accelerate(90)
        print x.get_speed()

    for y in cheap_cars:
        y.accelerate(40)
        print y.get_speed()
        print y.doors





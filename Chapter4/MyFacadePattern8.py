"""Building a car with the facade pattern."""


class Car(object):
  def __init__(self):
    print 'Initializing system'

  def select_exterior(self):
    chassis = Chassis()
    chassis.build_chassis()
    tires = Tires()
    tires.build_tires()

  def select_mechanism(self):
    motor = Motor()
    motor.build_motor()
    cylinder = Cylinder()
    cylinder.build_cylinder()

  def select_interiors(self):
    seat = Seats()
    seat.build_seats()
    dash = Dashboard()
    dash.build_dashboard()

  def building_car(self):
    self.select_exterior()
    self.select_interiors()
    self.select_mechanism()


class Chassis(object):
  def __init__(self):
    print 'chassis constructor'

  def build_chassis(self):
    print 'constructing chassis'


class Tires(object):
  def __init__(self):
    print 'tires constructor'

  def build_tires(self):
    print 'setting tires'


class Motor(object):
  def __init__(self):
    print 'motor constructor'

  def build_motor(self):
    print 'build the motor'


class Cylinder(object):
  def __init__(self):
    print 'cylinder constructor'

  def build_cylinder(self):
    print 'four cylinders'


class Seats(object):
  def __init__(self):
    print 'seats constructor'

  def build_seats(self):
    print 'seat for five'


class Dashboard(object):
  def __init__(self):
    print 'dashboard constructor'

  def build_dashboard(self):
    print 'build the dashboard'


if __name__ == '__main__':
    print 'testing the car build'
    car = Car()
    car.select_exterior()
    car.select_mechanism()
    car.select_interiors()

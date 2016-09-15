from abc import ABCMeta, abstractmethod


# I am the product interface
class StationPlan(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run_process_plan(self):
        pass


# Concrete products
class ClosedLoopAll(StationPlan):
    def run_process_plan(self):
        print 'running closed loop all'


class OpenLoopAll(StationPlan):
    def run_process_plan(self):
        print 'running open loop all'


class Continuity(StationPlan):
    def run_process_plan(self):
        print 'run continuity'


class StraightThrough(StationPlan):
    def run_process_plan(self):
        print 'running straight through'


# Now create the creator
class ProcessPlan(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.process_plans = []
        self.create_plan()

    @abstractmethod
    def create_plan(self):
        pass

    def add_process_plan(self, process_plan):
        self.process_plans.append(process_plan)

    def get_process_plan(self):
        return self.process_plans


class Final(ProcessPlan):
    def create_plan(self):
        self.add_process_plan(Continuity)
        self.add_process_plan(ClosedLoopAll)
        self.add_process_plan(OpenLoopAll)


class Calibration(ProcessPlan):
    def create_plan(self):
        self.add_process_plan(StraightThrough)
        self.add_process_plan(ClosedLoopAll)
        self.add_process_plan(OpenLoopAll)

if __name__ == '__main__':
    station = input("Give me the station to build? [Final, Calibration]")
    station_type = station()
    print ("Creating station..", eval(type(station_type).__name__))
    print("Profile has section --", station_type.get_process_plan())
    station_type.process_plans[0]().run_process_plan()
from abc import ABCMeta, abstractmethod


# I am the product interface
class StationPlan(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run_process_plan(self):
        pass


# Concrete products
class DCPower(StationPlan):
    def run_process_plan(self):
        print 'running dc power loop all'


class FrequencyTest(StationPlan):
    def run_process_plan(self):
        print 'running frequency test 1'


class MicrophoneTest(StationPlan):
    def run_process_plan(self):
        print 'run microphone test'


class NoiseFigure(StationPlan):
    def run_process_plan(self):
        print 'running Noise figure through'


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
        self.add_process_plan(MicrophoneTest)
        self.add_process_plan(DCPower)
        self.add_process_plan(FrequencyTest)


class Calibration(ProcessPlan):
    def create_plan(self):
        self.add_process_plan(NoiseFigure)
        self.add_process_plan(DCPower)
        self.add_process_plan(FrequencyTest)

if __name__ == '__main__':
    station = input("Give me the station to build? [Final, Calibration]")
    station_type = station()
    print ("Creating station..", eval(type(station_type).__name__))
    print("Profile has section --", station_type.get_process_plan())
    for i in range(len(station_type.process_plans)):
        station_type.process_plans[i]().run_process_plan()
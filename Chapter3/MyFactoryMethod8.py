from abc import ABCMeta, abstractmethod

# Interface
class Test(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_up(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


# Concrete interface
class OOB(Test):
    def start_up(self):
        print 'settings for oob'

    def run(self):
        print 'run test for oob'

    def cleanup(self):
        print 'complete test for oob'


# Concrete interface
class InBand(Test):
    def start_up(self):
        print 'settings for ib'

    def run(self):
        print 'run test for ib'

    def cleanup(self):
        print 'complete test for ib'


# Concrete interface
class Diagnostics(Test):
    def start_up(self):
        print 'settings for diags'

    def run(self):
        print 'run test for diags'

    def cleanup(self):
        print 'complete test for diags'


# creator
class TestAggregation(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.test_plan = []
        self.create_test()

    @abstractmethod
    def create_test(self):
        pass

    def add_plan(self, test):
        self.test_plan.append(test)

    def get_plan(self):
        return self.test_plan


# concrete creator
class PreliminaryTest(TestAggregation):
    def create_test(self):
        self.add_plan(OOB)
        self.add_plan(InBand)


class FunctionalTest(TestAggregation):
    def create_test(self):
        self.add_plan(OOB)
        self.add_plan(Diagnostics)


# usage
if __name__ == '__main__':
    # Functional tests
    func_plan = FunctionalTest()
    for test in func_plan.test_plan:
        step = test()
        # test contains the test obj running at real time
        step.start_up()
        step.run()
        step.cleanup()


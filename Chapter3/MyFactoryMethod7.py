from abc import ABCMeta, abstractmethod


# Interface
class Test(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


# Concrete interface
class Video(Test):
    def __init__(self):
        print 'init video'

    def setup(self):
        print 'setup video'

    def run(self):
        print 'run video'

    def cleanup(self):
        print 'cleanup video'


# Concrete interface
class Audio(Test):
    def __init__(self):
        print 'init audio'

    def setup(self):
        print 'setup audio'

    def run(self):
        print 'run audio'

    def cleanup(self):
        print 'cleanup audio'


# Concrete interface
class Diagnostics(Test):
    def __init__(self):
        print 'init diags'

    def setup(self):
        print 'setup diag'

    def run(self):
        print 'run diag'

    def cleanup(self):
        print 'cleanup diag'


# Concrete interface
class HDD(Test):
    def __init__(self):
        print 'init hdd'

    def setup(self):
        print 'setup hdd'

    def run(self):
        print 'run hdd'

    def cleanup(self):
        print 'cleanup hdd'


# creator
class TestCreator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.test_type = []
        self.create_tests()

    @abstractmethod
    def create_tests(self):
        pass

    def add_test(self, test):
        self.test_type.append(test)

    def get_tests(self):
        return self.test_type


# concrete creator
class ForRack1(TestCreator):
    def create_tests(self):
        self.add_test(Video)
        self.add_test(Audio)


class ForRack2(TestCreator):
    def create_tests(self):
        self.add_test(Diagnostics)
        self.add_test(HDD)

# usage
if __name__ == '__main__':
    print 'create racks'
    rack1 = ForRack1()
    rack2 = ForRack2()
    for test in rack1.test_type:
        # use step to avoid instantiating twice
        step = test()
        step.setup()
        step.run()
        step.cleanup()

    print

    for test in rack2.test_type:
        step = test()
        step.setup()
        step.run()
        step.cleanup()





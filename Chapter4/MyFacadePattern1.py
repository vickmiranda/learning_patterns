# Facade
class Dut(object):
    def __init__(self):
        print 'initializing dut\n'
        diagnostics = Diags()
        diagnostics.connect()

        hardware = Hardware()
        hardware.configure()

    def run_test(self):

        ports = Ports()
        ports.load_ports()

        connections = Connections()
        connections.make_connections()

        measure = Measure()
        measure.read_voltages()
        measure.read_frequencies()

    def cleanup(self):

        output = Reports()
        output.save()


# Sub-system1
class Diags(object):
    def __init__(self):
        print 'diagnostic initialization\n'

    def connect(self):
        print 'connectting to diagnostic menus\n'


# Sub-system2
class Hardware(object):
    def __init__(self):
        print 'Initializing hardware\n'

    def configure(self):
        print 'configuring voltages\n'
        print 'configuring current\n'


# Sub-system3
class Ports(object):
    def __init__(self):
        print 'init ports'

    def load_ports(self):
        print 'Now loading ports\n'


# Sub-system4
class Connections(object):
    def __init__(self):
        print 'connect ports\n'

    def make_connections(self):
        print 'all connections have been made\n'


# Sub-system5
class Measure(object):
    def __init__(self):
        print 'starting measurements\n'

    def read_voltages(self):
        print 'reading dc voltages\n'

    def read_frequencies(self):
        print 'now reading frequencies\n'


# Sub-system6
class Reports(object):
    def __init__(self):
        print 'Generating reports\n'

    def save(self):
        print 'saving csv reports\n'


# Client
class TestDevice(object):
    def __init__(self):
        print 'Start testing dut'

    def Run(self):
        dut = Dut()
        dut.run_test()
        dut.cleanup()

    def __del__(self):
        print 'Testing device is now completed!'

# Usage
if __name__ == '__main__':
    test = TestDevice()
    test.Run()
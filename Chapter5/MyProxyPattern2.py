from abc import ABCMeta, abstractproperty


class Customer(object):
    def __init__(self):
        print 'init customer and proxy too\n'
        self.security = Security()

    def is_server_on(self):
        if self.security.get_state():
            print 'Server is protected!\n'
        else:
            print 'Server is vulnerable\n'
            res = raw_input('Do you want to protected?\n')
            if res[0].upper() == 'Y':
                self.security.set_state(True)
            else:
                print 'Good luck procrastinating!\n'


class Firewall(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print 'Start my protection\n'

    @abstractproperty
    def set_state(self, value):
        pass

    @abstractproperty
    def get_state(self):
        pass


# This is the object not seeing by customer
class Server(Firewall):
    def __init__(self):
        print 'Server initializing\n'
        self._state = False

    def set_state(self, value):
        self._state = value

    def get_state(self):
        return self._state


# This is the proxy
class Security(Firewall):
    def __init__(self):
        print 'start checking my server\n'
        self.response = {False: 'Off', True: 'On'}
        self.server = Server()

    def set_state(self, value):
        print 'setting firewall {}\n'.format(self.response[value])
        self.server.set_state(value)

    def get_state(self):
        return self.server.get_state()


if __name__ == '__main__':
    print 'Checking security\n'
    customer = Customer()
    customer.is_server_on()
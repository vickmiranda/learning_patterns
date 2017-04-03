class RadioBroadcast(object):
    def __init__(self):
        self._stations = []

    def register(self, station):
        self._stations.append(station)

    def national_anthem(self, *args, **kwargs):
        print 'Time to sing\n'
        for station in self._stations:
            station.notify(self, *args, **kwargs)

    def red_alert(self, *args, **kwargs):
        for station in self._stations:
            station.notify(self, *args, **kwargs)


class StationFM1(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print (type(self).__name__, ' got ', args, 'from', type(subject).__name__)


class StationFM2(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print (type(self).__name__, ' got ', args, 'from', type(subject).__name__)


class StationFM3(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print (type(self).__name__, ' got ', args, 'from', type(subject).__name__)

if __name__ == '__main__':
    subject = RadioBroadcast()
    for station in [StationFM1, StationFM2, StationFM3]:
        station(subject)

    subject.national_anthem('Time to go home', 'Sing National Anthem\n')
    print
    print 
    subject.red_alert('Child abduction\n')
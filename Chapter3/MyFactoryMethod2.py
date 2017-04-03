from abc import ABCMeta, abstractmethod


# Product interface
class ReportType(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute_process(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


# Concrete interfaces
class NewsReport(ReportType):
    def execute_process(self):
        print 'Executing news report'

    def cleanup(self):
        print 'Cleaning up news report'


class WorldReport(ReportType):
    def execute_process(self):
        print 'Executing world report'

    def cleanup(self):
        print 'Cleaning up world report'


class WeatherReport(ReportType):
    def execute_process(self):
        print 'Executing weather report'

    def cleanup(self):
        print 'Cleaning up weather report'


# This is the creator
class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.reports = []
        self.create_reports()

    @abstractmethod
    def create_reports(self):
        pass

    def add_reports(self, report):
        self.reports.append(report)

    def get_reports(self):
        return self.reports


class ReportOne(Report):
    def create_reports(self):
        self.add_reports(NewsReport)


class ReportTwo(Report):
    def create_reports(self):
        self.add_reports(NewsReport)
        self.add_reports(WeatherReport)


class ReportThree(Report):
    def create_reports(self):
        self.add_reports(NewsReport)
        self.add_reports(WeatherReport)
        self.add_reports(WorldReport)


if __name__ == '__main__':
    # Generate Report for BurnIn
    for_final = ReportThree()
    for i in range(len(for_final.reports)):
        for_final.reports[i]().execute_process()

    for i in range(len(for_final.reports)):
        for_final.reports[i]().cleanup()

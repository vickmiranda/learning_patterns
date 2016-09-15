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
class ConnectionReport(ReportType):
    def execute_process(self):
        print 'Executing connection report'

    def cleanup(self):
        print 'Cleaning up connection report'


class DataReport(ReportType):
    def execute_process(self):
        print 'Executing data report'

    def cleanup(self):
        print 'Cleaning up data report'


class PortReport(ReportType):
    def execute_process(self):
        print 'Executing Port report'

    def cleanup(self):
        print 'Cleaning up port report'


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


class ReportCalibration(Report):
    def create_reports(self):
        self.add_reports(ConnectionReport)


class ReportsFinal(Report):
    def create_reports(self):
        self.add_reports(ConnectionReport)
        self.add_reports(PortReport)


class ReportsBurnIn(Report):
    def create_reports(self):
        self.add_reports(ConnectionReport)
        self.add_reports(PortReport)
        self.add_reports(DataReport)


if __name__ == '__main__':
    # Generate Report for BurnIn
    for_final = ReportsBurnIn()
    for i in range(len(for_final.reports)):
        for_final.reports[i]().execute_process()

    for i in range(len(for_final.reports)):
        for_final.reports[i]().cleanup()

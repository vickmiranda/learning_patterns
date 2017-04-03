class DataTool(object):
  def __init__(self):
    print 'data tool running'

  def gathering(self):
    extract = Extract()
    extract.GetInformation()

  def processing(self):
    analysis = Analysis()
    statistics = Statistical()
    analysis.analyse_data()
    statistics.regression()

  def reports(self):
    plot = PlotData()
    report = SendtoReports()

    plot.plot()
    report.format_html()

  def cleanup(self):
    print 'data tool complete analsys'


class Extract(object):
  def __init__(self):
    print 'start extracting info'

  def GetInformation(self):
    print 'Gather information'


class Analysis(object):
  def __init__(self):
    print 'start analysis section'

  def analyse_data(self):
    print 'format data and analyse'


class Statistical(object):
  def __init__(self):
    print 'start statistical process'

  def regression(self):
    print 'regression model'


class PlotData(object):
  def __init__(self):
    print 'start plotting data'

  def plot(self):
    print 'plotting data'


class SendtoReports(object):
  def __init__(self):
    print 'start reporting tools'

  def format_html(self):
    print 'format into html'


if __name__ == '__main__':
  tool = DataTool()
  tool.gathering()
  tool.processing()
  tool.reports()
  tool.cleanup()



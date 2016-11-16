from abc import ABCMeta, abstractmethod


class Compiler(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def collection_source(self):
    pass

  @abstractmethod
  def compile_to_object(self):
    pass

  @abstractmethod
  def run(self):
    pass

  def compile_and_run(self):
    self.collection_source()
    self.compile_to_object()
    self.run()


class iOSCompiler(Compiler):
  def collection_source(self):
    print 'collecting swift source code'

  def compile_to_object(self):
    print 'compiling swift code to bitcode'

  def run(self):
    print 'Program running in RT environment'


if __name__ == '__main__':
  ios = iOSCompiler()
  ios.compile_and_run()

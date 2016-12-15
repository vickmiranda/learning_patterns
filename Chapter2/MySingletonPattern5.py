class MyTest(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not MyTest._instance:
      MyTest._instance = super(MyTest, cls).__new__(cls, *args, **kwargs)
    return MyTest._instance

  def __init__(self):
    self.test_list = []

  def add_video_tests(self):
    self.test_list.append('video1')
    self.test_list.append('video2')

  def add_audio_tests(self):
    self.test_list.append('audio1')
    self.test_list.append('audio2')
    self.test_list.append('audio3')

  def add_other_tests(self):
    self.test_list.append('voltage')
    self.test_list.append('current')
    self.test_list.append('frequency')

  def get_test_list(self):
    return self.test_list


test1 = MyTest()

test2 = MyTest()


test1.add_video_tests()
test2.add_audio_tests()
test1.add_other_tests()

for test in test1.get_test_list():
  print test

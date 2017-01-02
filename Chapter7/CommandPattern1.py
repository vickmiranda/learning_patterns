class Wizard(object):
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print ('copying binaries --', self.src, 'to ', self.rootdir)
            else:
                print 'no operation'


if __name__ == '__main__':

    wizard = Wizard('python3.5.gzip', 'usr/bin')

    wizard.preferences({'python': True})
    wizard.preferences({'java': False})

    wizard.execute()



from abc import ABCMeta, abstractmethod

class Customer(object):
    def __init__(self):
        print('Talk to the asian gentlemen\n')
        self.translator = Translator()

    def talk_to_translator(self):
        self.response = self.translator.talk()

    def listen(self):
        self.response = self.translator.listen()

    def __del__(self):
        if self.response:
            print ('Thank you Mr translator\n')
        else:
            print ('Maybe I need to hire someone else\n')


class Japanese(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print ('Please start translating this sentence\n')

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def listen(self):
        pass


class Asian(Japanese):
    def __init__(self):
        self.available = None
        self.audible = None

    def is_available(self, check):
        if check[0].upper() == 'Y':
            self.available = True
        else:
            self.available = False

    def talk(self):
        print 'Konichiwa, Moshi moshi.. I don\'t speak english ...\n'
        return True and self.audible

    def listen(self):
        print ('kiku\n')
        return True and self.audible

    def set_tone(self, audible):
        self.audible = audible


class Translator(Japanese):
    def __init__(self):
        self.asian = Asian()
        
    def talk(self):
        self.asian.set_tone(True)
        print ('Hey Mr Asian good morning..\n')
        free = raw_input('Are you listening? [Y,N]\n')
        self.asian.is_available(free)
        if self.asian.available:
            print ('Thank you, Mr american says bla bla bla\n')
            response = self.asian.listen()
        else:
            response = False
            print ('Oh sorry maybe we can talk next time\n')
        return response

    def listen(self):
        self.asian.set_tone(False)
        print ('Please tell me what you think?\n')
        response = self.asian.talk()
        return response

if __name__ == '__main__':
    englishman = Customer()
    englishman.talk_to_translator()
    englishman.listen()
        

# Facade
class DigestiveSystem(object):
    def __init__(self):
        print ('Complex digestive system\n')

    def ingesting(self):
        print ('I am so hungry!')
        mouth = Mouth()
        mouth.chowing()
        esophagus = Esophagus()
        esophagus.swallowing()

    def digesting(self):
        stomach = Stomach()
        stomach.process_food()

        small_instestine = Small_Intestine()
        small_instestine.break_down_process()

    def completing_process(self):
        big_guy = Colon()
        big_guy.process_waste()


# Sub-system1
class Mouth(object):
    def __init__(self):
        print ('Do I have food here?\n')

    def chowing(self):
        print ('This is yummy!!\n')


# Sub-system2
class Esophagus(object):
    def __init__(self):
        print ('Food is going down\n')

    def swallowing(self):
        print ('Please break the food into small pieces\n')


# Sub-system3
class Stomach(object):
    def __init__(self):
        print ('Ok time to sleep brain\n')

    def process_food(self):
        print ('Are there enough enzymes to digest this burger?\n')

    def send_to_instestine(self):
        print ('Sending semi-processed food to the next guy\n')


class Small_Intestine(object):
    def __init__(self):
        print 'Dividing nutrients from food'

    def break_down_process(self):
        print ('Liver and biles taking some nutrients! some left over not '
               'needed!\n')


class Colon(object):
    def __init__(self):
        print ('I am the big instenstine!\n')

    def process_waste(self):
        print ('Ok time to go to the bathroom!\n')


# Client
class MrHungry(object):
    def __init__(self):
        print('What do you want for dinner!\n')

    def having_dinner(self):
        ds = DigestiveSystem()
        ds.ingesting()
        ds.digesting()
        ds.completing_process()

    def __del__(self):
        print 'Bye\n'

# Usage
if __name__ == '__main__':
    print ('Let\'s go and have something to eat!')
    answer = raw_input('Are you hungry? [Y/N]')

    if answer[0].upper() == 'Y':
        vicente = MrHungry()
        vicente.having_dinner()
    else:
        print ('Ok maybe next time')

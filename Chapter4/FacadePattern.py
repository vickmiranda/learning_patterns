# Fachada
class DepartmentStore(object):
    def __init__(self):
        print 'Checking items in the store'

    def WalkOut(self):
        produce = Produce()
        produce.check_inventory()

        sports = SportingGoods()
        sports.BikeStlyle()
        sports.Outdoors()

        decor = Decor()
        decor.cloth_style()


# Sub-system1
class Produce(object):
    def __init__(self):
        print ('Let\'s check quantities \n')

    def check_inventory(self):
        if self.is_available():
            print('Inventory is full\n')

    def _is_available(self):
        return True


# Sub-system2
class SportingGoods(object):
    def __int__(self):
        print 'starting sporting goods\n'

    def BikeStlyle(self):
        print 'Check bikes models\n'

    def Outdoors(self):
        print 'What type of activity?\n'

# Sub-system3
class Decor(object):
    def __int__(self):
        print ('Start checking decor deparment\n')

    def cloth_style(self):
        print 'Checking new style of pants\n'

    def curtains_style(self):
        print ('Check what type of curtains\n')



# Client
class Buyer(object):
    def __init__(self):
        print ('Let\s go shopping!!\n')

    def buying_stuff(self):
        store = DepartmentStore()

# Usage
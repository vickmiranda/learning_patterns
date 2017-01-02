class MemoryManagement(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not MemoryManagement._instance:
            MemoryManagement._instance = super(MemoryManagement, cls).__new__(
                cls, *args, **kwargs)
        return MemoryManagement._instance

    def __init__(self):
        self.address = []

    def allocate_ram(self):
        self.address.append("from 0x0 to 0x100")

    def allocate_rom(self):
        self.address.append("from 0x101 to 0x200")

    def allocate_eeprom(self):
        self.address.append("from 0x201 to 0x1000")
        self.address.append("from 0x2000 to 0x2500")
        self.address.pop(1)

if __name__ == '__main__':
    mem1 = MemoryManagement()
    mem2 = MemoryManagement()

    mem1.allocate_ram()
    mem2.allocate_rom()
    mem1.allocate_eeprom()

    for section in mem1.address:
        print 'memory allocated: {}'.format(section)

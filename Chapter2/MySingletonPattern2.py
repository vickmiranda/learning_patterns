class Cell(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not Cell._instance:
            Cell._instance = super(
                Cell, cls).__new__(cls, *args, **kwargs)
        return Cell._instance


c = Cell()
c1 = Cell()

print type(c).__name__, c
print type(c1).__name__, c1


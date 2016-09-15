'''
Composition
'''
class A(object):
    def a1(self):
        print ('a1')

class B(object):
    def b(self):
        print ('b')
        A().a1()

class C(object):
    def c(self):
        print
        print ('c')
        B().b()

# Notice that calling other member is possible w/o inheritance
ObjectB = B()
ObjectB.b()

ObjectC = C()
ObjectC.c()

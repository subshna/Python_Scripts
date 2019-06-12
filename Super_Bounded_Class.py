class Base(object):
    def __init__(self, x):
        self.a = x
    def calc(self):
        print 'calc of base executed'
    def display(self):
        print 'display of base is executed', self.a

class derived(Base):
    def __init__(self, x):
        super(derived, self).__init__(x)
        self.b = 20
    def calc(self):
        super(derived, self).calc()
        print 'calc of derived executed'
    def display(self):
        super(derived , self).display()
        print 'display of derived executed'

ob = derived(10)
ob.calc()
ob.display()
print 'member of variable object is: ', ob.a, ob.b

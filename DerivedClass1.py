class Base:
    def __init__(self):
        print 'Base class contructor', self
    def calcBase(self):
        print 'Calc of Base'
    def displayBase(self):
        print 'Display of Base'

class Derived(Base):
    def __init__(self):
        print 'Derived Constructor', self
    def calcDerived(self):
        print 'Derived calc'
    def displayDerived(self):
        print 'Display Derived'

ob = Derived()
ob.calcDerived()
ob.calcBase()
ob.displayDerived()
ob.displayBase()

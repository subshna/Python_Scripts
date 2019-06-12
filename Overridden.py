class base:
    def __init__(self):
        print 'Base class constructoe executed'
    def calcbase(self):
        print 'calc of base executed'
    def displaybase(self):
        print 'display of base executed'
class derived(base):
    def __init__(self):
        base.__init__(self)
        print 'Derived class constructor executed'
    def calcderived(self):
        print 'calc of derived executed'
    def displayderived(self):
        print 'display of derived executed'

ob = derived()
ob.calcderived()
ob.calcbase()
ob.displayderived()
ob.displaybase()

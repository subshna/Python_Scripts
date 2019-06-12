class Base:
    def calcbase(self):
        print 'Calc of Base executed'
    def displaybase(self):
        print 'display of Base executed'

class derived(Base):
    def calcderived(self):
        print 'calc of Derived executed'
    def displayderived(self):
        print 'display of Derived executed'

ob = derived()
ob.calcderived()
ob.displayderived()

ob.calcbase()
ob.displaybase()

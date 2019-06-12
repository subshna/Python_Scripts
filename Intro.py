class First:
    def calcfirst(self):
        print 'Calc of first executed'
    def displayfirst(self):
        print 'display of first executed'

class Second:
    def calcsecond(self):
        print 'calc of second executed'
    def displaysecond(self):
        print 'display of second executed'

ob1 = First()
ob2 = Second()

ob1.calcfirst()
ob1.displayfirst()

ob2.calcsecond()
ob2.displaysecond()

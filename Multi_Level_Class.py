class First:
    def displayFirst(self):
        print 'display of First executed'

class Second(First):
    def displaySecond(self):
        print 'display of Second executed'

class Third(Second):
    def displayThird(self):
        print 'display of Third executed'

ob = Third()
ob.displayThird()
ob.displaySecond()
ob.displayFirst()

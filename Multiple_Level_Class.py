class First:
    def First(self):
        print 'display of First executed'

class Second:
    def Second(self):
        print 'display of Second executed'

class Third(First, Second):
    def Third(self):
        print 'display of Third executed'

ob = Third()
ob.First()
ob.Second()
ob.Third()

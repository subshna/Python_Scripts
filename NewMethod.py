class base:
    res = 10 # static variable
    @classmethod
    def calc(self):
        base.res+=10
        print 'Calc of base executed', base.res
    @staticmethod
    def display(self):
        print 'display of base executed', self

ob1 = base()
ob2 = base()

ob1.calc()
ob1.display()

print 'class ref: ', base
print 'object ref: ', ob1
print 'Method ref: ', ob1.calc, ob1.display, ob2.calc, ob2.display
print 'contents of base: ', dir(base)
print 'contents of object: ', dir(ob1)
print 'Dictionary contents is: ', base.__dict__

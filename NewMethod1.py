class base:
    res = 10 # static variable
    @staticmethod
    def calc(self):
        base.res+=10
        print 'Calc of base executed', base.res
    @staticmethod
    def display(self):
        print 'display of base executed', self

print 'class ref: ', base
print 'Method ref: ', base.calc, base.display
print 'contents of base: ', dir(base)
print 'Dictionary contents is: ', base.__dict__
print 'Type method is :',type(base.calc), type(base.display)
#print 'Content ', dir(base)
base.calc()
base.display()

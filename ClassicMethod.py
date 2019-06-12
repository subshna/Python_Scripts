class Base:
    res = 10
    def calc(self):
        Base.res+=10
        print 'Calc base executed', Base.res
    def display(self):
        print 'Display of base executed', self

ob1 = Base()
ob2 = Base()

ob1.calc()
ob2.calc()

ob1.display()
ob2.display()

print 'Class reference(Handle of Base class): ', Base
print 'Object Ref: (Handle of Object)', ob1, ob2
print 'Method ref: (Method handle)', ob1.calc, ob2.calc, ob1.display, ob2.display
print 'Content of base: (Accessible member of base namespace)', dir(Base)
print 'Content of object: (Accessible member of object namespace)', dir(ob1), dir(ob2)
print 'Dictionary content is: (Actual memebr of base class)', Base.__dict__
print 'The type(display): (Object Type)', type(ob1.calc), type(ob1.display)

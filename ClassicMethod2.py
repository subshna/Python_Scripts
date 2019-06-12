class Base:
    res = 10
    def display(self):
        print 'Display of base executed', self
    display = classmethod(display)

ob1 = Base()
ob1.display()

print 'Class Ref :', Base, 'Object Ref: ', ob1
print 'Method Ref :', ob1.display
print 'Contents of base is: ', dir(Base)
print 'Contents of Object is: ', dir(ob1)
print 'Dictionary of contents is: ', Base.__dict__

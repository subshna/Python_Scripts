class wipro:
    res = 0
    def __init__(self, x=0, y=0):
        self.a = x; self.b = y
        print 'Constructor executed'

    def calc(self):
        wipro.res = self.a + self.b
        return wipro.res

ob1 = wipro(10,20)
ob2 = wipro(30,40)

x = ob1.calc()
y = ob2.calc()

print x
print y
print wipro.res
print ob1.__dict__
print ob2.__dict__
print wipro.__dict__

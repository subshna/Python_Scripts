class wipro:
    def __init__(self, x, y):
        self.a = x; self.b = y
        print 'Constructor executed'
    def display(self):
        print 'Display method is executed', self, self.a, self.b
    def __del__(self):
        print 'Destructor executed', self

m = wipro(1,2)
n = wipro(3,4)
m.display()
n.display()
print 'Object attributes of M is ', m.a, m.b
print 'Object attributes of N is ', n.a, n.b
print 'Component class ', dir(wipro)
print 'Component object ', dir(m)
del m
print 'Destructor manually executed'
print 'Default container component ', dir()

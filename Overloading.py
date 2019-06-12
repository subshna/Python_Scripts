class first(object):
    def __init__(self, a=0, b=0):
        self.x = a; self.y = b

    def calc(self, m, n):
        self.x = m.x+n.x
        self.y = m.y+n.y

    def display(self):
        print 'Values: ', self.x, self.y

ob1 = first(1, 2)
ob2 = first(3, 4)
ob3 = first()

ob3.calc(ob1, ob2)

ob3.display()

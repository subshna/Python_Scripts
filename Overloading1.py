class first(object):
    def __init__(self, a=0, b=0):
        self.x = a; self.y = b

    def display(self):
        print 'Values: ', self.x, self.y

ob1 = first(5, 7)
ob2 = first(7, 9)
ob3 = first()

ob1.display()
ob2.display()

a = ob1 + 10
b = ob2 + 20

ob3 = ob1 + ob2
print 'ob1 is: ', ob1
print 'ob2 is: ', ob2

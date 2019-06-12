class wipro:
    res = 0
    def __init__(self, x=0, y=0):
        self.a = x; self.b = y
        print 'Constructor executed'

    def calc(self):
        wipro.res = self.a + self.b

    def display(self):
        print 'The atributes of a & b are: ', self.a, self.b

ob1 = wipro(1,2)
ob2 = wipro(3,4)
ob3 = wipro(5)

ob1.calc()
ob2.calc()
ob3.calc()

ob1.display()
ob2.display()
ob3.display()

print wipro.res


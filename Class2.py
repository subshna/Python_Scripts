class wipro:
    def display(self):
        print 'Inside Display : ', self

m = wipro()
n = wipro()
m.display()
n.display()
print 'Address of m %x and n is %x' %(id(m), id(n))
print 'Address of m is', m , 'and n is ', n

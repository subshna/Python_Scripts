class first(object):
    def __init__(self, a=0, b=0):
        self.x = a; self.y = b
        def __add__(ob1, ob2):
            return first(ob1.a + ob2.a, ob1.b + ob2.a)
        def __sub__(ob1, ob2):
            return first(ob1.a - ob2.a, ob1.b - ob2.a)
        def display(self):
            print 'values: ', self.x, self.y

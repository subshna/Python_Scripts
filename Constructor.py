class base:
    def __init__(self):
        self.x = 0; self.y = 0
        print 'Constructor'

class derived(base):
    def __init__(self):
        base.__init__(self)
        self.a = 0; self.b = 0
        print 'Iam constructor'

ob = derived()
print 'Members of object are: ', ob.__dict__

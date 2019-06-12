class first(object):
    def __init__(self):
        print 'First Constructor'
        
class second(first):
    def __init__(self):
        super(second, self).__init__()
        print 'Second Constructor'

class third(second):
    def __init__(self):
        super(third, self).__init__()
        print 'Third constructor'

ob = third()

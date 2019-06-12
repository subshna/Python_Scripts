class sample:
    def First(self):
        print 'Class Method'
    def second():
        print 'Static Method'

    First = classmethod(First)
    second = staticmethod(second)

sample.second()
ob1 = sample()
ob1.First()

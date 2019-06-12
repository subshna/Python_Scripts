class First:
    class_member = 10

class Second(First):
    pass

class Third(First):
    class_member = 20

class Fourth(Second, Third):
    pass

ob = Fourth()
print 'Value of class member: ', ob.class_member

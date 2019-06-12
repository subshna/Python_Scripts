class First:
    class_member = 0

ob1 = First()

ob1.class_member = 10

print 'Static variable', ob1.class_member
print 'class variable', First.class_member

class first(object):
    class_member = 10
class second(first):
    pass
class third(first):
    pass
class fourth(second, third):
    pass

ob = fourth()
print 'value of class member: ', ob.class_member

print 'Base class are: ', fourth.__bases__
print 'contents for class: ', dir(fourth)
print 'content given namespace: ', fourth.__dict__
print 'name of namespace: ', fourth.__name__
print 'module name: ', fourth.__module__
print 'document string: ', fourth.__doc__
print 'MRO path: ', fourth.__mro__

from collections import namedtuple

named
Cat = namedtuple('Cat', 'fur claws name')
c= Cat(fur='Fuzzy', claws=False, name='Meow')
print c.fur
print c.claws
print c.name
print c[0], c[1], c[2]
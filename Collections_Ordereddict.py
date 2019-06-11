# with normal dictionary
d ={}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print ('Normal Dictionary')
for k, v in d.items():
    print (k,v)

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print ('Ordered Dictionary')
for k, v in d.items():
    print (k,v)
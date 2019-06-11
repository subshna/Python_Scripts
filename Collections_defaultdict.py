from collections import defaultdict
# with lambda
d = defaultdict(lambda :0)
print (d['one'])
d['two'] = 2
print (d)

# With object
dit = defaultdict(object)
print (dit)

def switch_dict(d1, d2):
    dout = {}

    for d1keys, d2values in zip(d1, d2.itervalues()):
        dout[d1keys] = d2values
    return dout

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'x': 10, 'y':20, 'z':30}

print (switch_dict(d1, d2))
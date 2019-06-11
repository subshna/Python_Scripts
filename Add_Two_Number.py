lst1 = [2,3,4,5]
lst2 = [6,8,1,4]
res = []

lst1.reverse()
lst2.reverse()

strlst1 = ''.join(map(str, lst1))
strlst2 =''.join(map(str, lst2))

sumoflst = int(strlst1) + int(strlst2)

for x in str(sumoflst):
    res.append(x)
res.reverse()
strres =''.join(map(str, res))
print strres

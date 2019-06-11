import datetime
import random
import time

def main():
    file = open('./ListAccessTime.xml', 'w')
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title="Average List Element Access Time">\n')

    # Test list of size from 1000 to 20000
    xmin = 1000
    xmax = 20000

    # Record the list sizes in xList and the average access time within
    # a list that size in yList for 1000 retrievals.
    xList = []
    yList = []

    for x in range(xmin, xmax+1, 1000):
        xList.append(x)
        prod = 0
        lst = [0] * x
        time.sleep(1)
        starttime = datetime.datetime.now()

        for v in range(1000):
            index = random.randint(0, x-1)
            val = lst[index]
            prod = prod * val

        endtime = datetime.datetime.now()

        deltatime = endtime - starttime
        accesstime = deltatime.total_seconds()

        yList.append(accesstime)

    file.write('    < Axes >\n')
    file.write('        < XAxis min = "'+str(xmin)+'" max = "'+str(xmax)+'" > List Size < / XAxis >\n')
    file.write('        < YAxis min = "'+str(min(yList))+'" max = "'+str(60)+'" > Microseconds < / YAxis >\n')
    file.write('    < / Axes >\n')

    file.write('    < Sequence title = "Average Access Time vs List Size" color = "red" >\n')

    for i in range(len(xList)):
        file.write('    < DataPoint x = "'+str(xList[i])+'" y = "'+str(yList[i])+'" / >\n')

    file.write('    </Sequence>\n')

    xList = lst
    yList = [0] * 200000
    time.sleep(2)

    for i in range(100):
        starttime = datetime.datetime.now()
        index = random.randint(0, 200000-1)
        xList[index] = xList[index] + 1
        endtime = datetime.datetime.now()
        deltatime = endtime - starttime
        yList[index] = yList[index] + deltatime * 1000000

    file.write('    <Sequence title="Access Time Distribution" color="blue">\n')

    for i in range(len(xList)):
        if xList[i] > 0:
            file.write('    <DataPoint x="'+str(i)+'" y="'+str(yList[i]/xList[i])+'"/>\n')

    file.write('    </Sequence>\n')
    file.write('</Plot>\n')
    file.close()

if __name__ == '__name__':
    main()
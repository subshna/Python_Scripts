x, y = input('First Number: '), input('Last Number: ')
m = min(x, y)
n = max(x, y)
for num in range(m, n+1):
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                break
        else:
            print '%d is a Prime Number' %num
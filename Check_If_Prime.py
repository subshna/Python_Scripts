def Check_Prime(num):
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                print('%d Not a Prime Number' % num)
                break
        else:
            print('%d is a prime Number' % num)
    else:
        print('Number Should be greater than One')

Check_Prime(11)
number = [45, 22, 14, 65, 97, 72]

for i, num in enumerate(number):
    if num % 3 == 0 and num % 5 == 0:
        number[i] = 'fizzbuzz'
    elif num %3 == 0:
        number[i] = 'fizz'
    elif num % 5 == 0:
        number[i] = 'buzz'

print (number)

for j, n in enumerate(number, start=10):
    print ('Element start {} and value {}'.format(j, n))
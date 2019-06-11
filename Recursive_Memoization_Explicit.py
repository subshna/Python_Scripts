fibonacci_cache={}

def fibonacci_num(n):
    '''To find the fibonacci numbers for the given number n'''
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_num(n-1) + fibonacci_num(n-2)

    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(fibonacci_num(n))
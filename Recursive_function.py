'''This function would return the fibonacci number
But the issue with this code is that for larger number it would take more time'''
def fibonacci_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (fibonacci_number(n-1) + fibonacci_number(n-2))

for n in range(1, 10):
    print (fibonacci_number(n))
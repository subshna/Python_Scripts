def addition(n):
    return n + n

numbers = (1,2,3,4,5)
result = map(addition, numbers)
print list(result)

# Using lambda
num1 = [1,2,3]
num2 = [4,5,6]

result = map(lambda x, y: x + y, num1, num2)
print list(result)

# map function on string list
lst = ['cat', 'rat', 'map', 'list']

res = map(list, lst)
print list(res)

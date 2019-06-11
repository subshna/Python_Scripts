from itertools import combinations

def Two_Sum(lst, target):
    collected = {}
    for i, x in enumerate(lst):
        diff = target - x
        if diff in collected:
            return (collected[diff], i)
        collected[x] = i                    


lst = [2,7,5,5,11]
target = 10

print(Two_Sum(lst, target))

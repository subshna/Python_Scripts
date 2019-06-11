print (sorted([2,5, 1, 7, 8, 9, 3, 7, 10]))

print (sorted(['cat', 'bat', 'man', 'hat'], reverse=True))

animals = [
    {'type': 'peguin', 'name':'stephaine', 'age':5},
    {'type': 'elephant', 'name':'king', 'age':3},
    {'type': 'rhino', 'name':'rhino', 'age':7}
]

print (sorted(animals, key=lambda animal: animal['age']))
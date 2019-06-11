import random

def random_walk_2(n):
    x , y = 0, 0
    for i in range(n):
        dx, dy  = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return(x, y)
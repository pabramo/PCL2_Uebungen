import random

def sample(iterable, k):
"""
Returns @param k random items from @param iterable.
"""
reservoir = []
for t, item in enumerate(iterable):
    if t < k:
        reservoir.append(item)
    else:
        m = random.randint(0,t)
        if m < k:
            reservoir[m] = item
    return reservoir

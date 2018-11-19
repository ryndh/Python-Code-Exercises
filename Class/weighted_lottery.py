#Build a weighted lottery

weights = {
        'winning': 1,
        'losing': 1
    }



other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
    }

import random

def weighted_func(library):
    total_data = list()
    for key, value in library.items():
        while value > 0:
            total_data.append(key)
            value -= 1

    randomizer = random.choice(total_data)
    print(randomizer)


weighted_func(other_weights)

###Jordan's Solution
import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

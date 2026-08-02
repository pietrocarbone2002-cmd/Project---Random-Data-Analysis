#Random Data generated through a random walk
import numpy as np
import matplotlib.pyplot as plt

def random_walk(start:int, steps:int, bias:float):

    #Input Validation
    if not isinstance(start, int):
        raise ValueError("The start point has to be a number!")
    
    if not isinstance(steps, int):
        raise ValueError("The number of steps has to be an integer!")
    
    if not isinstance(bias, float) or bias > 1.0 or bias < 0:
        raise ValueError("The series bais has to be a number between 0 and 1!")

    #Random Walk generation
    y = start

    time = np.arange(steps + 1)
    walk = [y]
    prob = bias

    for i in range(1, steps + 1):
        if np.random.uniform(0,1) < prob:
            y += 1
        else:
            y -= 1
        walk.append(y)

    return time, walk
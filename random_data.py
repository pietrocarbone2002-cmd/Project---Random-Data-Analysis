#Random Data generated through a random walk
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------------------
#Random Walk
#-------------------------------------------------------------------------------------------------------------

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
    values = [y]

    for i in range(1, steps + 1):
        if np.random.uniform(0,1) < bias:
            y += 1
        else:
            y -= 1
        values.append(y)

    return time, values

#-------------------------------------------------------------------------------------------------------------
#Mean Reversion using the Ornstein Uhlenbeck Method
#-------------------------------------------------------------------------------------------------------------

def random_mean_reverting(start:int, steps:int, sigma:float,
        theta:int = 2, mu:int = 0 #theta = reversion rate / mu = mean value / sigma = noise strength
        ): 

    tau = 1/theta #Characteristic time scale
    dt = 0.01 * tau
    y = start

    time = np.arange(steps + 1)
    values = [y]

    for i in range(1, steps + 1):
        x_curr = values[i - 1]

        mean = x_curr * np.exp(-theta * dt) + mu * (1 - np.exp(-theta * dt))
        var = sigma**2/(2*theta) * (1 - np.exp(-2*theta*dt))
        sd = np.sqrt(var)

        x_next = np.random.normal(loc = mean, scale = sd)
        x_curr = x_next

        values.append(x_next)

    return time, values

data_random_walk = random_walk(0, 5000, 0.5)
data_random_mr = random_mean_reverting(0, 5000, 5)

plt.plot(data_random_walk[0], data_random_walk[1], '-', label="Random Walk Data", color = "orange", linewidth = 1)
plt.plot(data_random_mr[0], data_random_mr[1], '-', label="Random Mean Reverting", color = "blue", linewidth = 1)

plt.title("Random Data Series")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.legend()
plt.grid()
plt.show()
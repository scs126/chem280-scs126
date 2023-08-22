#this code applies numpy to compute the value of pi via MC integration

import math
import time
import random
import numpy as np

start = time.time() #start timer

# Start by using 100 samples.
n_samples = 100000

random_numbers = np.random.random(size=(n_samples,2)) #generate a 100 x 2 array of random numbers
#these pairs will serve as the randomly generated (x,y) coordinated for this MC simulation

vals = np.sum(random_numbers**2, axis=1) #executes the x**2 + y**2 distance equation to give a vector of sums
vals = np.sqrt(vals) #takes square root of sums to obtain a vector of radii
num_inside = np.sum(vals < 1) #create and fill an array that effectively acts as a counter
#for the number of radii that are < 1, i.e. fall within the bounds of the unit circle

pi = 4 * num_inside / n_samples # 4 * the MC integration for one quarter of a unit circle

end = time.time() #stop timer

elapsed_time = end - start
print(pi)
print(elapsed_time)
#this script applies MC integration to evaluate the integral of (1/(1+x^2))dx from [0,1]

import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

N = 1000 #define the total number of random samples to be generated for MC integration
Efxi = 0 #start summed f(xi) values at zero
a = 0 #define bounds of integral [a, b]
b = 1

for i in range(N):
    x = random.random() #generate random xi value
    if x <= b:
        fxi = (1 / (1 + x ** 2)) #computes f(xi)
        Efxi = Efxi + fxi #add f(xi) to sum

FN = (b - a) * Efxi / (N - 1) #compute MC integral
calcpi = 4 * FN #calculate pi from obtained integrand since the actual result is pi/4
print(FN)
print(calcpi)


#to solve this assignment problem I first wrote out the MC integration equation (line 19)
#by hand and identified each variable I needed to define. Then I identified the order
#in which the variables needed to be defined and modified. The for loop approach was basically
#taken from the calculate pi execercise with appropriate changes to run the assignment's f(x)

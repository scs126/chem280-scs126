import random
import math
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111)
fig.show()

start = time.time() #start timer

n_samples = 100000 #number of randomly generated (x,y) coordinates
num_inside = 0 #initial counter is zero

#for j in range(6): #to run through 10, 100, 1000, 10000, 100000, 10000000 sample sizes
    
    #generate random coordinates
for i in range(n_samples):
    x = random.random()
    y = random.random()
    r = math.sqrt(x ** 2 + y ** 2) #use pythagorean theorem to calculate radius at point i
    if r < 1:
        num_inside += 1 #counter increases by 1
        ax.plot(x,y, 'ob') #add point to plot
    else:
        ax.plot(x,y, 'r*') #add point to plot in red
    #picalc = 4 * num_inside / n_samples
    #percent_error = 100 * abs(picalc - 3.14) / 3.14
    #print(picalc)
    #print(percent_error)
    #plt.savefig(n_samples)
    #n_samples = n_samples * 10 #so we go up an order of magnitude in sample size for the next iteration


#calculate pi
picalc = 4 * num_inside / n_samples
percent_error = 100 * abs(picalc - 3.14) / 3.14

end = time.time() #stop timer
elapsed_time = end - start #calculated time it took code to run
print(elapsed_time)

print(picalc) 
print(percent_error)
      
#plot random points w unit circle outline
ax.set_xlim(0,1) #set displayed x bounds
ax.set_ylim(0,1) #set displayed y bounds
#plt.savefig('calcpiplt') #save generated plot to same folder as this script file
circle = Circle((0, 0), 1, color = 'k', alpha = 0.2) #defining circle appearance on plot
ax.add_patch(circle)
plt.show() #displays generate plot in new window


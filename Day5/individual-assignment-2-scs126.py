import csv
import random
import math
import matplotlib.pyplot as plt
import os




#define any constants
epsilon = 120 / (1.3806 * 10 ** 23) # Kelvin / (J/Kelvin)
sigma = 3.4 * 10 ** -8 # Angstrom * 10 ** -8 cm / Angstrom
Na = 6.022 * 10 ** 23 # number / mol

#define function to convert reduced pressure to unit pressure
def reduced_pressure_to_real(reduced_value, sigma, epsilon):
    """
    Convert a reduced pressure to a real value based on sigma and epsilon.
    
    Parameters
    ----------
    reduced_value : float
        The reduced pressure
    
    sigma : float
        The sigma value in SI units (meters)
    
    epsilon : float
        The epsilon value in SI units (joules)
    
    Returns
    -------
    float
        The pressure value in real units.
    """
    converted_pressure = []

    for i in range(len(reduced_pressure)):
        P = reduced_pressure[i] * epsilon / sigma ** 3
        converted_pressure.append(float(P))
    
    return(converted_pressure)


#define function to convert reduced temperature to units
def reduced_temperature_to_real(reduced_value, epsilon):
    """
    Convert a reduced temperature to a real value based on epsilon
    
    Parameters
    ----------
    reduced_value : float
        The reduced temperature
    
    epsilon : float
        The value for epsilon  
        
    Returns
    -------
    float
        The system temperature in K
    """

    converted_temperature = []

    for i in range(len(reduced_temperature)):
        T = reduced_pressure[i] * 120
        converted_temperature.append(float(T))
    
    return(converted_temperature)



#define function converting reduced density to unit density
def reduced_density_to_real(reduced_value, sigma):
    """
    Convert a reduced density to a real density.
    
    Parameters
    ----------
    reduced_value : float
        The reduced value for the density
    
    sigma : float
        The value for sigma in meters
        
    Returns
    -------
    float
        The density of the system in mol/L
    """

    converted_density = []

    for i in range(len(reduced_density)):
        rho = 1000 * reduced_density[i] / (Na * (sigma ** 3))
        converted_density.append(float(rho))
    
    return(converted_density)




#defining reduced units of interest we want to load from the reduced unit datasheet
reduced_temperature = []
reduced_pressure = []
reduced_density = []
reduced_volume = []

#import reduced unit datasheet and assign columns of interest to appropriate variables
with open(os.path.join('nist_data.csv'), "r") as f:
    reader = csv.reader(f)
    
    for count, row in enumerate(reader):
        if count > 0:
            reduced_temperature.append(float(row[0]))
            reduced_density.append(float(row[1]))
            reduced_pressure.append(float(row[4]))
#now we have the reduced unit data of interest loaded into their respective variable arrays

#now define the unit variables
temperature = [] #Kelvin
pressure = [] #MPa
density = [] #mol/L

#import the unit data spreadsheet and assign columns of interest to appropriate variables
with open(os.path.join('nist_tabulated_argon.csv'), "r") as f:
    reader = csv.reader(f)
    
    for count, row in enumerate(reader):
        if count > 0:
            temperature.append(float(row[0]))
            density.append(float(row[2]))
            pressure.append(float(row[1]))



#plot density vs pressure, overlay MC generated values and actual values reported by NIST

plt.plot(reduced_pressure_to_real(reduced_pressure , sigma , epsilon) , reduced_density_to_real(reduced_density , sigma) , 'ro') #plot LJ values as markers
plt.plot(pressure , density , color = 'b') #plot NIST data as a line
plt.show() #display generated plot



"""
Reflection: How accurate is the MC simulation?
The MC simulation does a pretty good job of predicting the actual tabulated data, it seems to be consistently within +/-5mol/L of the actual data.
THis exercise helped illustrate the utility of Monte Carlo simulations in modelling complex molecular systems.

"""

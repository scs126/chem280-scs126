import math
import random
import csv
import os

#define constants
pi = 3.1415
U_LRC = -1.9849 * 10 ** 2 #NIST-reported U_LRC for configuration 1 rc* = 3.0



#define function to read coordinates from file
def read_xyz(filepath):
    """
    Reads coordinates from an xyz file.

    Parameters
    -----------
    filepath : str
        The path to the xyz file to be processed

    Returns
    --------
    atomic_coordinates : list
        A two dimensional list containing atomic coordinates

    """

    #with open(os.path.join(filepath) , "r") as f:
    #
    #   x = []
    #   y = []
    #   z = []
    #
    #    reader = txt.reader(f)
    #
    #    for count , row in enumerate(reader):
    #        if count > 0:
    #            x.append(float(row[0]))
    #            y.append(float(row[1]))
    #            z.append(float(row[2]))
    
    #return x , y , z

    with open(filepath) as f:
        box_length = float(f.readline().split()[0])
        print(box_length)
        num_atoms = float(f.readline())
        coordinates = f.readlines()
    
    atomic_coordinates = []
    
    for atom in coordinates:
        split_atoms = atom.split()
        
        float_coords = []
        
        # We split this way to get rid of the atom label.
        for coord in split_atoms[1:]:
            float_coords.append(float(coord))
            
        atomic_coordinates.append(float_coords)

    
    return atomic_coordinates , box_length , num_atoms


#define function to calculate distance between two points
def calculate_distance(coordinate1 , coordinate2 , box_length):
    distance = math.sqrt(coordinate1 ** 2 + coordinate2 ** 2)

    return distance

#define function to calculate tail correction
#tail correction value will be used as the cutoff value in subsequent LJ calculation
def calculate_tail_correction(box_length , n_particles):
    rc = 3 #cutoff distance considered for this exercise

    const = (8 * pi * n_particles **2) / (3 * box_length ** 3) #define first term of LJ w tail correction
    r3rd_term = math.pow(1 / rc , 3)
    r9th_term = math.pow(r3rd_term , 3)

    tail_correction = const * (1 / 3 * r9th_term - r3rd_term)

    return tail_correction



#define function to calculate the LJ potential for a pair of atoms
def calculate_LJ(r_ij):
    """
    The LJ interaction energy between two particles
    
    Computes the pairwise LJ interaction energy based on the separation distance in reduced units.

    Parameters
    -----------
    r_ij : float
        The distance between the particles in reduced units.
    
    Returns
    ---------
    pairwise_energy : float
        The pairwise Lennard-Jones interaciton energy in reduced units.
    
    Examples
    ----------
    >>> calculated_LJ(1)
        0

    """
    r6_term = math.pow(1/r_ij, 6) #math.pow(x, y) -> x^y
    r12_term = math.pow(r6_term, 2) #takes (r_ij^6)^2 = r_ih^12
    pairwise_energy = 4 * (r12_term - r6_term)
    
    
    return pairwise_energy


#define tail correction function
def calculate_total_energy(coordinates , box_length , n_particles , cut_off):
    """
    Calculate the total LJ energy of a system of particles.

    Parameters
    -----------
    coordinates : list
        Nested list containing particle coordinates.
    
    Returns
    -------
    total_energy : float
        The total pairwise energy LJ energy of the system of particles.

    """

    total_energy = 0

    
    for i in range(n_particles):
        for j in range(i + 1 , n_particles):
            dist_ij = calculate_distance(coordinates[i] , coordinates[j] , box_length)

            if dist_ij < cut_off: #applying boundary condition
                interaction_energy = calculated_LJ(dist_ij)
                total_energy += interaction_energy
    

    return total_energy



#reading in coordinate file
config_file = "sample_config1.txt"

sample_coords , box_length , num_atoms = read_xyz(config_file) #run coordinate file through coordinate reading function, also get box length

#assertion statements to check file read-in function worked properly
# We expect this file to have 800 particles
assert len(sample_coords) == 800

# We expect the first line to be:
first_line = [-1.126362593256E-01, 1.385093082507E+00, -8.842035145736E-01]

for i in range(3):
    assert first_line[i] == sample_coords[0][i]
    
# We expect the last line to be:
last_line = [3.497455843197, 0.3754925406415, 4.393398690912]

for i in range(3):
    assert last_line[i] == sample_coords[-1][i]







#setting up for LJ tail correction function
N = num_atoms #pull number of atoms from xyz function

length = box_length #define unit length based on xyz file function


tail_correction = calculate_tail_correction(length , N)

assert math.isclose(tail_correction , U_LRC , rel_tol = 0.05) #assert checks against configuration 1 from class

total_energy_with_cutoff = calculate_total_energy(atomic_coordinates , length)


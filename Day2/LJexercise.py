# exerceise using Lennard-Jones equation to model a nobel gas (e.g. argon)

#define function to run Lennard-Jones calculation
def calculate_LJ(r_ij):
    #adding numpy style docstrings to this function (docstrings must always appear on the first line after def function():)
    # headings are denoted as text with ------ on the line below (e.g. see Parameters below)
    # """" denotes beginning and end of a docstrings section
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

# use assert function to check your function for specific cases or outputs
assert calculate_LJ(1) == 0 #checks if LJ calculation is 0 (i.e. r = 1)
assert calculated_LJ(math.pow(2, (1/6))) == -1 # checks if the minimum interatomic energy potential occurs at -1 (for dimensionless form of the LJ equation)

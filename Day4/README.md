# Day 4 Repository

This repository contains files relevant to Day 4 content and the second individual assignment (described below).

## Individual Assignment 2

The primary objective of this assignment is to compare predictive data generated via MC simulation to actual tabulated data to get an idea of how accurate MC methodology can be in application to modelling complex systems. Here, we consider the Lennard Jones equation, which describes the pair-wise, distance-dependent (for our purposes) interatomic energy:

$U(r) = 4\epsilon[(\sigma/r)^12 - (\sigma/r)^6]$

Where $\sigma$ is the interatomic distance at which the interatomic potential is zero and $\epsilon$ is the energetic depth of the interatomic potential well. For this assignment, consider the values for argon: $\sigma = 3.4*10^-8$ cm and $\epsilon / k_B =$ 120K. The predicted data, found in nist_data.csv, contains parameter values in reduced units, which we first have to scale back to real units that match the units of the tabulated data in nist_tabulated_argon.csv using the following equations:

pressure in MPa:  $P = \epsilon P* /\sigma$


temperature in K:  $T = \epsilon T* / k_B$

number density in mol/L:  $\rho = 1000\rho* / N_A \sigma^3$

Following this dimensional analysis of the reduced data, we use matplotlib features to generate an overlayed plot of pressure vs number density displaying the converted reduced data as red points and the tabulated data as a continuous blue line.

To run the code in individual-assignment-2-scs126.py just run the file froma terminal window with the referenced  excel files present in the same directory as the code file. The code will generate the above-described overlayed plot to visualize the predicted and tabulated datasets.


## How accurate is the MC simulation?
Based on the overlayed data, it appears MC simulation offers a feasible method for predicting gaseous atomic behavior in a simple environment. Here, we neglected all interatomic interactions except interatomic potential as a function of pair-wise distances. It will be interesting to see how MC simulation error propagates as additional parameters are accounted for and how we can adjust the simulation to reduce/control the error propagation in upcoming coursework.

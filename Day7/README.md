# Day 7 Repository
This repository contains files relevent to Day 7 content and the third individual assignment (described below).


# Individual Assignment 3
The primary objective of this assignment is to convert the python script from Individual Assignment 1 into C++. To reiterate, the integral of interest we want to run through a Monte Carlo integration is:

F = $\int_1^{100}{1 / (1+x^2)dx}$

where the actual answer is $\pi / 4$, but we want to see how close we can get with MC integration.

The secondary objective of this assignment is to look at how efficient different script types are; we want to compare the time it takes the python script, an non-optimized C++ script, and an optimized C++ script to run the same MC integration. To do this:

- the python file was run from the terminal window command line as "time python assignment.py"
- the non-optimized C++ file was run from the terminal command line as "g++ -O0 montecarlo.cpp -O montecarlo" -> "./montecarlo"
- the optimized C++ file was run from the terminal command line as "g++ -O3 montecarlo.cpp -O montecarlo" -> "./montecarlo"

## Notes on Converting Python to C++

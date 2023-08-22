# Day 2 Repository

This repository contains files relevant to the first individual assignment (described below) and files for exercises from Day 2.
#
# 
# Individual Assignment 1

The first task in this assignment is to apply Monte Carlo integration to estimate the following integral:

F = $\int_1^{100}{1 / (1+x^2)dx}$

The actual integration yields F = $\pi/4$ and we want to see how close we can get depending on the sample size applied to the MC integration.

## Running assignment.py
Here, the only input you really need to mess with is the number of samples. which is assigned to integer variable N (line 8). Increasing the number of samples applied to the integration should yield progressively more accurate integration results (i.e. closer to $\pi/4$). A few case tests varying the sample size by orders of magnitude are below, where both $\pi/4$ and $\pi$ were calculated.

Having to manually change the sample size each time you want to test a different size can get tedious and could be remedied with a for loop around the for loop currently in the assignment.py code such that you are able to automatically iterate through several sample sizes that vary by a desired interval. 

## Testing Different N Sample Sizes
Since the numerical equivalent of $\pi/4$ = 0.785... doesn't come to mind quite as quickly as $\pi$ = 3.1415... the quick check to highlight how accurate the MC integration was to multiply $\pi/4$ by 4 to get the predicted value for $\pi$.

For N = 10 we got F = 0.8905619467226261 
- This yields $\pi$ = 3.5622477868905045

Not bad for such a small sample size, but we can definitely do better by increasing the sample size.

For N = 100 we got F = 0.799918043175418
- This yields $\pi$ = 3.199672172701672

So we're getting closer, but still not as close as we can be.

For N = 1000 we got F = 0.7859085656323321
- This yields $\pi$ = 3.1436342625293285

This is accurate to the hundredths digit, about as precise as most people typically write pi when they have to manually enter pi into a calculator.

The observed increased accuracy of the predicted value for pi with increasing sample size N demonstrates the Monte Carlo integration is working. By increasing the sample size, you're effectively averaging over finer incremental areas, which allows you to better capture the true shape of the function we're integrating over. Also, at larger sample sizes, the probability of having regions of low sampling density reduces, i.e. you're more likely to obtain more evenly spaced x-values within the specified domain of integration.
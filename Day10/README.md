# Day 10 Repository
This repository contains files relevant to Day content and the fourth individual assignment (described below).

## Individual Assignment 4
The primary objectives of this assignment are to practice vector manipulation and reading to/from a text file. The assignment was divided into five parts to be followed chronologically as described below:

1. Create a std::vector<double> containing 20 random numbers in the range (-10.0 , 10.0).

    The random number generator function was the same as what was used in Indivdual Assignment 3. To generate the vector, a vector of size 0 was initially defined, then each iteration of a for loop added a new double to the end of the vector.

2. Write a function that writes a std::vector<double> to a file. Hint you likely want to write the size() of the vector to the file first, so the reader knows how many numbers to read.

    For this part of the assignment, I opted to write each vector element to the file in the same iteration of the for loop it was generated in rather than generating the entire vector and then reading it into a new file. This allowed me to avoid pre-defining the size of the vector I would be reading into the new file.


3. Write a function that reads that file and returns the std::vector<double> of file contents. Use this function to re-read the data written in the previous step, storing into a different std::vector<double>.

    The vector elements were read from the file into a new vector in a similar iterative manner where a while loop was used to append each subsequent vector element to the end of the generated vector.


4. Check that the sizes of the vector are the same. What might be a good way to make sure this is true?

    An assert statement was used to check if the original vector and the vector read back from the file were the same size (using.size()).


5. Loop over the numbers of both vectors and compare all the elements. Are they equal?

    A for loop was used to compare the elements at corresponding positions in the two vectors to check if the vectors matched within accepted error. For this exercise, I checked if the two vectors' elements matched to 0.01% of the original vector elements' values and all elements in the two vectors passed this acceptance test.

    On a side note, I didn't see the .precision(n) suggestion in step 6. until after I had made the for loop. However, I went back and tried appending this part of the code with lines using this feature but I couldn't get it to work. Namely, I tried a for loop within the for loop already in the code where each iteration of the inner loop would increase the degree of precision by +1, then compare the value of each vectors' element with an if statement. If  the two elements matched, the code would simply loop to the next degree of precision. If the two elements did not match, a else statement first included a statement to print the max degree of precision where the two elements matched, followed by an assert statement intended as a fail-stop for the code because it asserted the two elements matched, which we already know they don't match since they failed the If statement's condition. The main two issues I kept running into were: 1. the computer being unhappy with me trying to use the iteration value i of the for loop to specify degree of precision as precision(i); 2. I didn't want the whole statement of "x precision yielded this double" to be printed and I couldn't figure out the proper syntax to first assign the element of each vector with x precision to a variable that would allow them to then be directly compared with an assert statement, where their difference would == 0 if the two elements still matched at x degree of precision.
#include <iostream>
#include <random>
#include <chrono> // for generating the seed
#include <vector>
#include <fstream> //for reading/writing files
#include <string>
#include <iomanip> //for precision features

// Global! Probably shouldn't be used in real code
std::default_random_engine re;

/*! Generate a random double within a given range */
double random_double(double lower_bound, double upper_bound)
{
   std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
   return dist(re);
}

using namespace std;

int main(void)
{
    // Initialize based on time
    re.seed(std::chrono::system_clock::now().time_since_epoch().count());

    //create a double vector containing 20 random numbers [-10.0 , 10]
    std::vector<double> random;
    int size_vec = 20; //specify size of vector to make writing to a new file easier
    //std::ofstream out_file("randomvector.txt");
    //out_file << random.size() << std::endl;
    fstream file;
    {
        file.open("randomvector.txt" , ios_base::out); //create/open file to write vector to

    
        for(int i = 0; i < size_vec; i++)
        {
            double random_number = random_double(-10 , 10); //call random number generator function to get a number
            random.push_back(random_number); //append new random double to vector

            file << random_number << " "; //writes new random element to file
        }


    }

    file.close(); //close file you wrote the vector to

    //now we want to read the vector from the generated file into a new vector in this file
    // input stream - can only read from the file
    std::ifstream in_file("randomvector.txt");
    /*
    int j;
    std::string read_vector;
    std::cout << j << std::endl;

    // use stream extraction operator >>
    in_file >> read_vector >> j;

    std::cout << "read from file: " << read_vector << " " << j << std::endl;

    in_file.close(); //close file now that we've read what we want from it
    */

    std::ifstream fin("randomvector.txt");
    
    std::vector<double> read_vector;
    
    double element;
    while (fin >> element)
    {
        read_vector.push_back(element); //adds element at ith position to ith position of new vector
    }


    //now we want to check that the vector read from file matches the original vector we generated
    //let's take the size of each vector to check the size of each vector matches
   assert(random.size() == read_vector.size());


    //now let's compare the values for each vector side-by-side to check they match
    for(int j = 0; j < random.size(); j++)
    {
        //I wrote this assert check before reading step 6. on the assignment document
        //this assert check also works but doesn't exactly indicate the degree of precision the same way that .precision(n) would
        double tolerance = abs(0.0001 * random[j]); //set a tolerance of 0.01% for accepting if corresponding vector elements are ~equal
        assert(abs(random[j] - read_vector[j]) < tolerance);
    }


    return 0;
}
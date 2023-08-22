#include <iostream>
#include <random> // for random numbers
#include <chrono> // for generating the seed


/* Other include files here */

// Global! Probably shouldn't be used in real code
std::default_random_engine re;


/*! Generate a random double within a given range */
double random_double(double lower_bound, double upper_bound)
{
   std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
   return dist(re);
}




int main(void)
{
    // Initialize based on time
    re.seed(std::chrono::system_clock::now().time_since_epoch().count());

    int N = 100000; //number of randomly generated samples
    double Efxi = 0; //initialize summed f(xi) values at zero
    int a = 0; //define bounds of integration [a , b]
    int b = 1;

    for(int i = 0; i < N; i++)
    {
        double x = random_double(a , b); //call random number generator function
        if(x <= b)
        {
            double fxi = (1 / (1 + x * x)); //computes f(xi)
            Efxi = Efxi + fxi; //add f(xi) to sum
        }

    }

    double FN = (b - a) * Efxi / (N - 1); //compute MC integral
    double calcpi = 4 * FN; //calculate pi from obtained integrand since the actual result is pi/4
    std::cout << "integral = " << FN << " (is actually pi/4)" << std::endl;
    std::cout << "calculated pi = " << calcpi << " (sanity check is pi ~ 4 * integral)" << std::endl;

    return 0;
}
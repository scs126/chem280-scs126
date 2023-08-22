#include <iostream> //load necessary libraries at beginning of code


//define say_hello(s):
void say_hello(std::string name , int count) // std::string defines inputted argument type, name defines the name of the variable the argument will be assigned in the function
{
    //make this function print "hello name" to the screen
    std::cout << "Hello " << name << std::endl; //since name variable is a string you can insert it into the cout function
    
    if (name == "there")
    {
        std::cout << "it's sunny out" << std::endl;
    }

    else if (name == "their" || name == "they're") // || denotes "or" in an if statement
    {
        std::cout << "it's going to rain later" << std::endl;
    }

    else
    {
        std::cout << "what day is it?" << std::endl;
    }

    //return 0; //by convention, have C++ return zero/void if a function runs successfully
    //nonzero return values are assumed to mean failure by C++
    //the return 0 functions similar to how assert functions are used in Python
}


int main(void) //define function main() where void denotes this function does not take any arguments
//note how you have to specify the integer type this function returns as the very first thing in the first line
{
    int i = 0;
    for(int i = 0; i < 10; i++) //equivalent to Python for loop for i in range(10);
    //i++ is equivalent to i = i + 1 i.e. it specifies the increment of increase for each iteration of the for loop is +1
    {
        std::cout << i << std::endl;
    }
    
    std::cout << "Hello world" << std::endl << "Hello again" << std::endl;
    //this function highlights how multiple statements can be ona single line of code
    //this can also be two lines, where one line specifies the Hello world and the second line specifies the Hello again
    //cout is an object that represents your output, and then the hello world string is the block that becomes your output
    //endl is end current line, go to new line
    //std is the standard library
    // :: is the "scope resolution operator"
    // in C++ " " denotes string and ' ' denotes character, while in Python " " and ' ' both denote string
    say_hello("they're" , i); //calling a function in C++ is done the same way you call functions in Python
    return 0;
}
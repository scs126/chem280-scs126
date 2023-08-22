#include <iostream>

int main(void)
{
    int count = 0;
    for(int i = 0; i < 10; i++)
    {
        count += 1;
        std::cout << count << std::endl;
    }

    return 0;
}
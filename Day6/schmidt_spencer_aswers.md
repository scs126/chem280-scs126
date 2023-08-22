## Answer the following questions:

1. What does an assignment statement look like in  Python? In C++? What are the differences?

    Assignment statments create new variables and give them a name.
    In Python: 
- message = 'some string' creates a string variable with the assigned name message
- n = 17 creates an integer variable with the name n
- pi = 3.1415926 creates a double variable with the name pi

    In C++:
- int variable1 = 4 creates an integer variable with the name variable1
- double Na = 6.022 creates a double variable with the name Na
- string hello = "hello world" creates a string variable with the name hello

2. The chapter says that Python variable names can not start with a number. Is the same true for C++ variable names?

    This is also true for C++. I tried making a variable named 1stnumber and the following error message was returned:
    error: expected unqualified-id
    int 1stnum = 4


3. What is an expression? Give an example of an expression Python and in C++.

    An expression is a combination of values, variables, and operators, as well as, a variable assignment statement, or a value all by itself that represents a single result.

4. Compare using code a for loop that counts to 10 in Python and C++. Write at least three sentences about how the loops are the same or different.

    For both languages, you have to first load the requisite libraries at the top of your code. To count to 10, an easy way to do this in both languages is a for loop, where the counter variable is assigned and initialized before the loop. Overall, you can count to 10 in a very similar manner for both languages, where within the for loops you just increase the counter by +1 each iteration and print the current value of the counter to the terminal output. The differences mainly come up in the different syntaxes used for the two languages, like specifying value type in C++.

5. Is there an interactive interpreter for C++? Why or why not?

    C++ on its own doesn't have an interactive interpreter as it is a compiler language, which allows it to be run directly through a compiler without first going through an interpreter. However, Python has an interactive interpreter because Python itself requires an interpreter before it can be run through a compiler.

6. Complete Exercise 1 from chapter 2 with both Python and C++.

    Exercise 1:
- 42 = n is not a legal statement because variable names cannot start with a number
- x = y = 1 is a legal statement because your variable names do not start with a number and you're effectively just defining two variables, x and y, that both have an assigned value of 1.
- A semi colon at the end of a Python statement just allows you to write another statement on the same line as it denotes separation, not termination. However, formatting Python code in this manner is not conventional as most people just denote statement separation with line breaks.
- A period at the end of a Python statement results in a syntax error because periods are typically used to access different methods/functions so a period with nothing after it doesn't follow Python syntax.

    Exercise 2:
- V = 523.58 for a sphere of r = 5
- the cost of the books is $647.01
- you get home at 7:30am (the run was 38min and some change)
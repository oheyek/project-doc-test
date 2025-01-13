C++ Module Documentation
=========================

This is the documentation for the C++ module.

Function: addNumbers
--------------------

.. code-block:: cpp

    /**
     * Adds two numbers.
     * 
     * @param a The first number.
     * @param b The second number.
     * @return The sum of a and b.
     */
    int addNumbers(int a, int b) {
        return a + b;
    }

Description:
    Adds two integers and returns their sum.

Parameters:
    - **a**: The first integer.
    - **b**: The second integer.

Returns:
    - **int**: The sum of `a` and `b`.

Example Usage
-------------

.. code-block:: cpp

    #include <iostream>

    int main() {
        std::cout << "Sum: " << addNumbers(3, 5) << std::endl;
        return 0;
    }

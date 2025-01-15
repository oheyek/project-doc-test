/**
 * Example Program
 * ---------------
 * Demonstrates the use of comments for documentation.
 */

#include <iostream>

/**
 * Subtracts one number from another.
 * 
 * @param a The first number.
 * @param b The second number.
 * @return The result of subtracting b from a.
 */
int subtractNumbers(int a, int b) {
    return a - b;
}

int main() {
    std::cout << "Difference: " << subtractNumbers(10, 4) << std::endl;
    return 0;
}

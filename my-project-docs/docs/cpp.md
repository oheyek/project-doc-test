# Dokumentacja C++

## Kod źródłowy: example.cpp

```cpp
/**
 * Example Program
 * ---------------
 * Demonstrates the use of comments for documentation.
 */

#include <iostream>

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

int main() {
    std::cout << "Sum: " << addNumbers(3, 5) << std::endl;
    return 0;
}

```


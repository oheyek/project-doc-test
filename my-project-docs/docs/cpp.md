# Program przykładowy: Dodawanie dwóch liczb

## Opis
Ten program w języku C++ demonstruje, jak używać komentarzy do dokumentacji. Program dodaje dwie liczby i wyświetla ich sumę.

## Kod źródłowy

```cpp
#include <iostream>

/**
 * Dodaje dwie liczby.
 * 
 * @param a Pierwsza liczba.
 * @param b Druga liczba.
 * @return Suma liczb a i b.
 */
int addNumbers(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Suma: " << addNumbers(3, 5) << std::endl;
    return 0;
}
```
#include <stdio.h>

// Function to calculate factorial
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int n;

    // Input from user
    n=5;

    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Calculate and display factorial
        printf("Factorial of %d = %d\n", n, factorial(n));
    }

    return 0;
}


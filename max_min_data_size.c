#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    printf("Maximum and Minimum values for data types:\n");

    printf("char:\n");
    printf("Max: %d\n", CHAR_MAX);
    printf("Min: %d\n", CHAR_MIN);

    printf("\nint:\n");
    printf("Max: %d\n", INT_MAX);
    printf("Min: %d\n", INT_MIN);

    printf("\nlong int:\n");
    printf("Max: %ld\n", LONG_MAX);
    printf("Min: %ld\n", LONG_MIN);

    printf("\nfloat:\n");
    printf("Max: %g\n", FLT_MAX);
    printf("Min: %g\n", FLT_MIN);

    printf("\ndouble:\n");
    printf("Max: %lg\n", DBL_MAX);
    printf("Min: %lg\n", DBL_MIN);

    return 0;
}


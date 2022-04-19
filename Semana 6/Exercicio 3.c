#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
    int x = 5;
    int *ptr;

    ptr = &x;

    printf("a) %d\n", *ptr);
    printf("b) %d\n", ptr);
    printf("c) %d\n", &ptr);
    printf("d) %d\n", &*ptr);
    printf("e) %d\n", **&ptr);

    return 0;
}
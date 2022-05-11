#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    int tam = 1001;
    float v[tam];
    float valores = 1.000;
    for (i = 0; i < tam; i++)
    { 
        valores = valores + 0.01;
        v[i] = valores;
    }
    for (i = 0; i < tam; i++)
    {
        printf("%.3f, ", v[i]);
    }
    return 0;
}
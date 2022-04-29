#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double maior = 0;
    int indice = 0;
    FILE *fr;
    fr = fopen("maioR.txt", "r");


    
    printf("Maior: %.4f na posicao %d\n", maior, indice);
    printf("Total de Elementos: %d", fscanf(fr);
    fclose(fr);
    return 0;
}

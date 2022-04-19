#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.13159265358979323846

double graus(double rad){
    float angulo;
    angulo = rad * 180/PI;
    printf("%.4f", angulo);
}

int main(){
    float rad;
    scanf("%f", &rad);
    graus(rad);
}

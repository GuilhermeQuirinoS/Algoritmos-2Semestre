#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double ps(double x[], double y[], int tam){
    double a=0,b=0,c=0;
    for(int i=0;i<tam;i++){
        a = x[i]*y[i];
        b += a;
    }
    printf("%.2lf", b);
}

int main(){
    int tam;
    scanf("%d", &tam);
    double x[tam];
    double y[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%lf", &x[i]);
    }
    for(i=0;i<tam;i++){
        scanf("%lf", &y[i]);
    }
    ps(x,y,tam);
}    
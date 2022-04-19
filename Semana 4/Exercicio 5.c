#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int conta(double v[], int tam){
    double a=0,b=0,c=0;
    for(int i=0;i<tam;i++){
        a = v[i]*v[i]; 
        b += a;
    }
    c = sqrt(b);
    printf("%.2f", c);
}

int main(){
    int tam;
    scanf("%d", &tam);
    double v[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%lf", &v[i]);
    }
    conta(v,tam);
}
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int media(double v[], int tam){
    float m=0,s=0;
    for(int i=0;i<tam;i++){
        s += v[i];
    }
    m = s/tam;
    printf("%.2f", m);   
    return 0;  
}

int main(){
    int tam;
    scanf("%d", &tam);
    double v[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%lf", &v[i]);
    }
    media(v,tam);
}
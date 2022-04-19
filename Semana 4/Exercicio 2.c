#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int maior(double v[], int tam){
    int m=v[0];
    int indice, aux=0;
    for(int i=0;i<tam;i++){
        if(m<v[i]){
            m = v[i];
            indice = i;
        }   
    } 
    printf("%d", m);
}

int main(){
    int tam;
    scanf("%d", &tam);
    double v[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%lf", &v[i]);
    }
    maior(v,tam);
}
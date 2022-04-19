#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int inverter(int v[], int tam){
    int j, tam2, aux;
    tam2 = tam/2;
    for(j=0;j<tam2;j++){
        aux = v[((tam-1)-j)];
        v[((tam-1)-j)] = v[j];
        v[j] = aux;
    }
}

int main(){
    int tam;
    scanf("%d", &tam);
    int v[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%d", &v[i]);
    }
}
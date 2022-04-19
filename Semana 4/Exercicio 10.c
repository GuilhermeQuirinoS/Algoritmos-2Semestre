#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void maior(double vx[],int tam,double vy[]){
    float maiorx, maiory, menorx, menory;
    float distma=0, distme=0;
    maiorx = menorx = vx[0];
    maiory = menory = vy[0];
    for(int i=0;i<tam;i++){
        if(menorx > vx[i]){
            menorx = vx[i];
        }    
        if(maiorx < vx[i]){
            maiorx = vx[i];
        }
    }
    for(int i=0;i<tam;i++){
        if(menory > vy[i]){
            menory = vy[i];
        }    
        if(maiory < vy[i]){
            maiory = vy[i];
        }
    }
    distma = maiory - menorx;
    distme = (-1*menory) - (-1*maiorx);
    printf("Menor distancia: %.2f", distme);
    printf("\nMaior distancia: %.2f", distma);
    
}

int main(){
    int tam;
    scanf("%d", &tam);
    double vx[tam];
    double vy[tam];
    int i;
    for(i=0;i<tam;i++){
        scanf("%lf", &vx[i]);    
    }

    for(i=0;i<tam;i++){
        scanf("%lf", &vy[i]);    
    }
    maior(vx,tam,vy);
}   


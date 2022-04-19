#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int desvio(double v[],int tam){
	double x,s,media,som=0;
	for(int i=0;i<tam;i++){
		x += v[i];		
  	}
	media = x/tam;
	for(int i=0;i<tam;i++){
		som += (v[i] - media)*(v[i] - media);
		s = sqrt(som/tam);
	}
    printf("Variancia Amostral = %.2lf", s);
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
  desvio(v,tam);
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (){
    int tam;
    int *v;

    printf("Digite a quantidade de alunos na sala: \n");
    scanf("%d", &tam);
    v = malloc(tam*sizeof(int));
    printf("Digite a nota de cada aluno: \n");
    for(int i = 0; i<tam; i++){
        scanf("%d", (v+i));
    }
    double soma,media = 0;
    for(int i = 0; i<tam; i++){
       soma = soma + *(v+i); 
    }
    media = soma/tam;
    printf("Media: %.0lf", media);
    free (v);
}


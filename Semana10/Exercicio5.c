#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fr = fopen("empresaR.txt", "r");
    int tam = sizeof(fr)+2;
    char nome[tam];
    char genero;
    int idade; 

    int total25 = 0;
    int totalf = 0;

    
    printf("Total de funcionarios: %d\n\n", tam);

    for (int i = 0; i < tam; i++){
        fscanf(fr, "%s %c %d", nome, &genero, &idade);
        if(idade>25){
            total25 = total25 + 1;
            printf("Nome do funcionario +25: %s idade: %d\n", nome, idade);
        }
        if(genero == 'f'){
            totalf = totalf + 1;
        }    
    }
    printf("\nTotal de funcionarios +25: %d\n", total25);
    printf("\nTotal de funcionarias: %d", totalf);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void troca(char *frase)
{
    for (int i = 0; i < strlen(frase); i++)
    {
        switch (*frase)
        {
        case 'a':
            *frase = 'u';
            break;
        case 'e':
            *frase = 'o';
            break;
        case 'i':
            *frase = 'u';
            break;
        case 'o':
            *frase = 'a';
            break;
        case 'u':
            *frase = 'e';
            break;
        }
        frase++;
    }
}
void imprime(char *frase){
    for (int i = 0; i < strlen(frase); i++){
        printf("%c", *frase++);
    }
}
int main()
{
    char frase[100];
    fgets(frase, sizeof(frase), stdin);
    troca(frase);
    imprime(frase);
}

/*
int main(){
    double nota [3][2];
    double soma, media;
    for(int i=0; i<3; i++){
        for(int j=0; j<2; j++){
            scanf("%lf", (*(nota + i) + j));
        }
    }
    for(int i=0; i<3; i++){
        soma=0;
        for(int j=0; j<2; j++){
            soma += *(*(nota + i) + j );
        }
        media = soma/2;
        printf("media do aluno %d = %.2lf\n", i, media);
    }
}
*/
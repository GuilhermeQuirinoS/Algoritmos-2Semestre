#include<stdio.h>
#include<stdlib.h>
#define TAM 100

int main(){
    int tamanhoVetor = 0;
    printf("Digite o tamanho do vetor:\n");
    scanf("%d", &tamanhoVetor);
    int metade;
    metade = tamanhoVetor/2;
    char msgOrig[TAM];
    int vetor[2][2];
    fgets(msgOrig, TAM, stdin);
    printf("Matriz A:\n"); // Entrada Matriz A.
     for(int l = 0; l < 2; l++){
         for(int k = 0; k < 2; k++){
             scanf("%d", &vetor[l][k]);
         }
     } // Entrada Matriz A.

    int mensagemCifrada[metade][2];
    // Entrada mensagem cifrada
    printf("Mensagem cifrada:\n");
    for(int linha = 0; linha < metade; linha++){
        for(int coluna = 0; coluna < 2; coluna++){
            scanf("%d", &mensagemCifrada[linha][coluna]);
        }
    }// Fim entrada mensagem cifrada

    //Mensagem decifrada
    int matrizC[metade][2], aux = 0;
    for(int linha = 0; linha < metade; linha++){
        for(int k = 0; k < 2; k++){
            matrizC[linha][k] = 0;
            for(int l = 0; l < 2; l++){
                aux += mensagemCifrada[linha][l] * vetor[k][l];
            }
            matrizC[linha][k] = aux;
            aux = 0;
        }
      }
      printf("Mensagem decifrada:\n");
      for (int i = 0; i < metade; i++){
        for(int k = 0; k < 2; k++){
            printf("%c", matrizC[i][k]);
        }
      }
}
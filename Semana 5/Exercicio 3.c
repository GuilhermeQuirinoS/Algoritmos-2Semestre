#include<stdio.h>
#include<stdlib.h>
#define TAM 100

int main(){
    printf("Mensagem:\n");
    char msgOrig[TAM];
    int vetor[2][2];
    fgets(msgOrig, TAM, stdin);
    printf("Matriz A:\n");
     for(int l = 0; l < 2; l++){
         for(int k = 0; k < 2; k++){
             scanf("%d", &vetor[l][k]);
         }
     }

  int i = 0, y = 0 ;
  while(msgOrig[i] != 10){i++;} // Conta a qtd de caracteres.
  if(i % 2 != 0){
    msgOrig[i] = 32;
    i++;
  }
  int metade = i/2;
  printf("Tamanho da mensagem: %d", i);
  int matrix[i/2][2];
  for(int linha = 0; linha < metade; linha++){
    for(int k = 0; k < 2; k++){
      matrix[linha][k] = msgOrig[y++];
    }
  }

// criptografia
    y = 0;
    int aux = 0;
    int matrizC[metade][2];
    printf("\nMensagem Cifrada:");
    for(int linha = 0; linha < metade; linha++){
        for(int k = 0; k < 2; k++){
            matrizC[linha][k] = 0;
            for(int l = 0; l < 2; l++){
                aux += matrix[linha][l] * vetor[k][l];
            }
            matrizC[linha][k] = aux;
            aux = 0;
        }
      }
      for (int i = 0; i < metade; i++){
        for(int k = 0; k < 2; k++){
            printf("\n%d ", matrizC[i][k]);
        }
      }
}
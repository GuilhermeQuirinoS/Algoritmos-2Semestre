#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int i,j,a,b,c,d=0;
    printf("Tamanho da matriz A:\n");
    scanf("%d %d", &a, &b);
    float ma[a][b];
    printf("Tamanho da matriz B:\n");
    scanf("%d %d", &d, &c);
    float mb[d][c];
  if(b == d){
    printf("Matriz A:\n");
    for(i=0;i<a;i++){
        for(j=0;j<b;j++){
            scanf("%f", &ma[i][j]);
        }
    }
    printf("Matriz B:\n");
    for(i=0;i<d;i++){
        for(j=0;j<c;j++){
            scanf("%f", &mb[i][j]);
        }
    }

    float mc[a][c];
    float aux;
    printf("Matriz AB:");
    for(i=0;i<a;i++){ 
        for(j=0;j<c;j++){
            mc[i][j]=0;
            for(int z=0;z<b;z++){
                aux += ma[i][z]*mb[z][j];
            }
            mc[i][j] = aux;
            aux = 0;
        }  
    }
    for(i=0;i<a;i++){
      printf("\n");
      for(j=0;j<c;j++){
        printf(" %.4f ", mc[i][j]);    
      }  
    }
  }  
  else  {
      printf("Dados incorretos.");
    }
}
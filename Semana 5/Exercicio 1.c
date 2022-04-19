#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int lin, col=0;
    printf("Tamanho da matriz A: \n");
    scanf("%d %d", &lin, &col);
    float m[lin][col];
    float v[col];
    float m2[col];
    printf("Matriz A:\n");
    for(int i=0;i<lin;i++){
        for(int j=0;j<col;j++){
            scanf("%f", &m[i][j]);
        }
    }
    printf("Digite o vetor com %d coordenadas:\n", col);
    for(int j=0;j<col;j++){       
        scanf("%f", &v[j]);  
    }
    printf("Produto de A por v:\n");
    for(int i=0;i<lin;i++){
        m2[i] = 0;
        for(int j=0;j<col;j++){
            m2[i] += m[i][j]*v[j];
        }
    printf("%.4f\n", m2[i]);    
    }
    return 0;
}
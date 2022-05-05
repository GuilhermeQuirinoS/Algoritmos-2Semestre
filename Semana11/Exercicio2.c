#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*DEU NÃO*/ 
int main(){
    int tam;
    int result;
    scanf("%d",& tam);
    int v[tam];
    for(int i=0; i < tam; i++){
        scanf("%d", &v[i]);
    }
    
    recursive(v,tam, 1);
    return 0;
}

int recursive(int v[], int tam, int rep){
    organiza(v,tam);
    
   
    return rep;
}
void organiza(int v[],int tam){
    int aux;
    int i, j;
    for(i=0; i < tam; i++){
        for(j=i+1; j < tam; j++){
            if(v[i] > v[j]){
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
}


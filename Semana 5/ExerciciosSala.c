#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void maiores(int m[4][4]){
    int conta10=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(m[i][j]>10){
                conta10++;
            }
        }
    }
    printf("%d", conta10);
}

int main(){
    int m[4][4];
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            scanf("%d", &m[i][j]);
        }
    }
    maiores(m);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int count=0;
int res = 1;
int hanoi(int x){
    if(count == x){
        return res-1;
    }else{
        count ++;
        res *= 2;
        return hanoi(x);
    }
}
int main(){
    int x;
    printf("Digite o numero de discos:\n");
    scanf("%d", &x);
    printf("Numero de movimentos com %d discos: %d.\n", x, hanoi(x));
}
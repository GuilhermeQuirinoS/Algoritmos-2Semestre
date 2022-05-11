#include <stdio.h>
#include <stdlib.h>

int count = 0;
int res = 1;
int C(int n){
    if (count == n || n == 1){
        printf("%d ", n);
        return n;
    }else{
        count++;
        printf("%d ", n);
        if (n%2==0){
            n= n / 2;
        }else if(n%2==1){
            n= (3 *n) + 1;
        }
        return C(n);
    }
}
int main(){
    int n;
    scanf("%d", &n);
    C(n);
}
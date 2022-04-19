#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int tamx,tamy;
    scanf("%d", &tamx, &tamy);
    double x[tamx];
    double y[tamy];
    int i;
    for(i=0;i<tamx;i++){
        scanf("%lf", &x[i]);
    }
    for(i=0;i<tamy;i++){
        scanf("%lf", &y[i]);
    }    
}
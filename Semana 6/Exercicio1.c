#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double modulo(double *v, int n){
    double x,y,soma=0;
    int i;
    for(i=0;i<n;i++){
        x = *(v+i) * *(v+i);
        soma += x;
    }
    y = sqrt(soma);
    printf("Modulo = %.4lf", y);
    return 0;
}

int main()
{
    int n, i;
    scanf("%d", &n);
    double v[n];
    for (i = 0; i < n; i++)
    {
        scanf("%lf", v + i);
    }
    modulo(v,n);   
    return 0;
}
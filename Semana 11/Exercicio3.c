#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double x=0;
double valor=0;

double sh(int);

int main(void) {
  int n;
  scanf("%d", &n);
  printf("%.4lf",sh(n));
}
double sh(int n){
  if(x==n){
    return valor;
  }
  else{
    x++;
    valor+=1/x;
    return sh(n);
  }
}
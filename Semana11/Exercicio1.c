#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    double Pot(double x, int n);
    double x, result = 0;
    int n = 0;

    scanf("%lf %d", &x, &n);
    
    result = Pot(x, n);
    printf("%.4lf", result);  
}

double Pot(double x, int n)
{
    if (n == 0)
    {
        return 1;
        
    }
    else if (n > 0)
    {
        return x * Pot(x, n-1);
    }
    else{
        return 1 / Pot(x, -n);
    }
    return x;
}

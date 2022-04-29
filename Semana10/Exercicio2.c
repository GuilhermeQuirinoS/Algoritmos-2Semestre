#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fr = fopen("quadradoR.txt", "r");

    float z;
    float x, y; 

    for(int i = 0; i < 8; i++){
        fscanf(fr, "%f %f", &x, &y);
        z = (x * x) + (y * y);
        printf("%.4f %.4f %.4f\n", x, y, z);
    }
    
    return 0;
}
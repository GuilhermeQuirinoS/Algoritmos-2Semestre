#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fr = fopen("notasR.txt", "r");

    char Nome[500];
    float Nota;
    

    for (int i = 0; i < 500; i++){
        fscanf(fr, "%s %f", Nome, &Nota);
        if(Nota >= 5){
            printf("%s %.1f\n", Nome, Nota);
        }       
    }
    return 0;
}
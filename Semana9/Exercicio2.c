#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void maiusculas(char *s){
    int caps = 0;
    for(int i=0; i < strlen(s); i++){
        char letter = s[i];
        if(65 <= letter && letter <= 90){
            caps++; 
        }
    }
    printf("%d", caps);
}

int main(){
    char s[51];
    fgets(s, 51, stdin);
    maiusculas(s);
    return 0;
}

 
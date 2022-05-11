#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void inverteMaiusMinus(char *s)
{   
    for(int i=0; i < strlen(s); i++){
        if(97 <= s[i] && s[i] <= 122){
            s[i] = s[i] - 32;
        }
        else if (65 <= s[i] && s[i] <= 90)
        {
            s[i] = s[i] + 32;
        }
    }
    printf("%s", s);
}

int main()
{
    char s[51];
    fgets(s, 51, stdin);
    inverteMaiusMinus(s);
    return 0;
}

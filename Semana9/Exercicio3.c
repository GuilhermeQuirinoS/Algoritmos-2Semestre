#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void minuscula(char *s)
{
    int mins = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        char letter = s[i];
        if (97 <= letter && letter <= 122)
        {
            mins++;
        }
    }
    printf("%d", mins);
}

int main()
{
    char s[51];
    fgets(s, 50, stdin);
    minuscula(s);
    return 0;
}

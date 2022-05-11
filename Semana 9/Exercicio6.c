#include <string.h>
#include <stdio.h>
#include <stdlib.h>
void numeros(char *str1, char *str2)
{
    int *n, *n2;
    for (int i = 0; i < strlen(str1); i++)
    {
        char snumber = str1[i];
        if (48 <= snumber && snumber <= 57)
        {
            n[i] = snumber - 48;
            printf("%d", n[i]);
        }
    }
    for (int i = 0; i < strlen(str2); i++)
    {
        char snumber = str2[i];
        if (48 <= snumber && snumber <= 57)
        {
            n2[i] = snumber - 48;
            printf("%d", n2[i]);
        }
    }
}

int main()
{
    char str1[51];
    char str2[51];
    fgets(str1, 51, stdin);
    fgets(str2, 51, stdin);
    numeros(str1, str2);
    return 0;
}
